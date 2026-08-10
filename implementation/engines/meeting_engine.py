#!/usr/bin/env python3
"""
회의 자동화 엔진
- 회의 생성
- 아젠다 자동 생성
- 회의록 템플릿 생성
- 회의 메타데이터 관리
"""

import json
import yaml
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional
import re

class MeetingEngine:
    """회의 생명주기를 관리하는 엔진"""

    def __init__(self, vault_path: str = "./llm-ssot"):
        """
        Args:
            vault_path: SSOT vault 루트 디렉토리
        """
        self.vault_path = Path(vault_path)
        self.meetings_dir = self.vault_path / "Meetings"
        self.decisions_dir = self.vault_path / "Decisions"
        self.ensure_directories()

    def ensure_directories(self):
        """필요한 디렉토리 생성"""
        self.meetings_dir.mkdir(parents=True, exist_ok=True)
        self.decisions_dir.mkdir(parents=True, exist_ok=True)

    def create_meeting(
        self,
        date: str,  # YYYY-MM-DD
        title: str,
        description: str = "",
        participants: List[str] = None,
        duration_minutes: int = 60,
        location: str = "온라인"
    ) -> str:
        """
        새 회의 생성

        Args:
            date: 회의 날짜
            title: 회의 제목
            description: 회의 설명
            participants: 참석자 목록
            duration_minutes: 예상 소요시간
            location: 장소

        Returns:
            생성된 파일 경로
        """
        # 파일명 생성: YYYY-MM-DD_title.md
        filename = f"{date}_{self._slugify(title)}.md"
        filepath = self.meetings_dir / filename

        # 메타데이터 생성
        meeting_meta = {
            "date": date,
            "title": title,
            "description": description,
            "participants": participants or [],
            "duration_minutes": duration_minutes,
            "location": location,
            "created_at": datetime.now().isoformat(),
            "status": "scheduled"
        }

        # 회의록 템플릿 생성
        content = self._generate_meeting_template(meeting_meta)

        # 파일 저장
        filepath.write_text(content, encoding='utf-8')

        return str(filepath)

    def generate_agenda_from_previous(
        self,
        previous_meeting_date: str
    ) -> Dict[str, any]:
        """
        이전 회의록을 기반으로 아젠다 생성

        Args:
            previous_meeting_date: 이전 회의 날짜 (YYYY-MM-DD)

        Returns:
            생성된 아젠다 (Type A/B/C로 분류)
        """
        # 이전 회의록 찾기
        prev_meeting = self._find_meeting_by_date(previous_meeting_date)
        if not prev_meeting:
            return {"error": f"회의록을 찾을 수 없음: {previous_meeting_date}"}

        # 파일 읽기
        content = prev_meeting.read_text(encoding='utf-8')

        # 행동항목 추출
        agenda = self._extract_action_items(content)

        return agenda

    def process_meeting_record(
        self,
        meeting_file: str
    ) -> Dict[str, any]:
        """
        회의록을 자동으로 처리

        Args:
            meeting_file: 회의록 파일 경로

        Returns:
            처리 결과 (요약, 액션 아이템, SSOT 영향 등)
        """
        filepath = Path(meeting_file)
        content = filepath.read_text(encoding='utf-8')

        # 1. 회의 메타데이터 추출
        meta = self._extract_meeting_metadata(content)

        # 2. 액션 아이템 추출
        action_items = self._extract_action_items(content)

        # 3. 결정사항 추출
        decisions = self._extract_decisions(content)

        # 4. SSOT 영향 분석
        ssot_impact = self._analyze_ssot_impact(content)

        # 5. ADR 필요여부 판단
        needs_adr = len(decisions) > 0 and ssot_impact["affected_sections"]

        result = {
            "meeting": meta,
            "action_items": action_items,
            "decisions": decisions,
            "ssot_impact": ssot_impact,
            "needs_adr": needs_adr,
            "processed_at": datetime.now().isoformat()
        }

        return result

    # ===== Private Methods =====

    def _generate_meeting_template(self, meta: Dict) -> str:
        """회의록 템플릿 생성"""
        template = f"""# 회의록

**복사 후 사용하기**: 이 파일을 복사해서 실제 회의록으로 작성하세요.

---

## 📋 회의 정보

| 항목 | 내용 |
|------|------|
| **날짜** | {meta.get('date')} |
| **시간** | HH:MM ~ HH:MM (소요시간: {meta.get('duration_minutes')}분) |
| **장소** | {meta.get('location')} |
| **참석자** | {', '.join(meta.get('participants', []))} |
| **의장** | [이름] |
| **기록자** | [이름] |
| **주제** | {meta.get('title')} |

---

## 🎯 안건 (Agenda)

```
[ ] 안건 1
[ ] 안건 2
[ ] 안건 3
```

---

## 📝 논의 내용 (Discussion)

### 안건 1: [주제]

**배경**:
-

**의견**:
- **사람1**:
- **사람2**:

**합의점**:
-

---

## ✅ 결정사항 (Decisions)

| 결정 | 담당자 | 마감일 | 상태 |
|------|--------|--------|------|
| 결정 1 | 이름 | YYYY-MM-DD | ⏳ |

---

## 📌 행동항목 (Action Items)

- [ ] **[담당자]** - [작업] - 마감: YYYY-MM-DD

---

## 🔗 SSOT 영향

이 회의에서 다음 SSOT 항목이 영향을 받음:

- [ ] [[model-selection|모델 선택]]
- [ ] [[prompt-engineering|프롬프트 엔지니어링]]
- [ ] [[inference-strategy|추론 전략]]
- [ ] [[evaluation|평가 방법론]]
- [ ] [[scaling-laws|스케일링 법칙]]
- [ ] [[error-handling|에러 처리]]

**영향 설명**:

---

## 📎 참고자료 (References)

- 링크 1
- 링크 2

"""
        return template

    def _slugify(self, text: str) -> str:
        """텍스트를 slug로 변환"""
        slug = re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')
        return slug[:50]  # 50자 제한

    def _find_meeting_by_date(self, date: str) -> Optional[Path]:
        """날짜로 회의록 찾기"""
        for file in self.meetings_dir.glob(f"{date}_*.md"):
            return file
        return None

    def _extract_meeting_metadata(self, content: str) -> Dict:
        """회의록에서 메타데이터 추출"""
        meta = {}

        # 정규식으로 테이블 파싱
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if '날짜' in line and i + 2 < len(lines):
                parts = lines[i + 2].split('|')
                if len(parts) > 2:
                    meta['date'] = parts[2].strip()

        return meta

    def _extract_action_items(self, content: str) -> List[Dict]:
        """행동항목 추출"""
        action_items = []

        # "## 📌 행동항목" 섹션 찾기
        pattern = r'## 📌 행동항목.*?(?=##|$)'
        match = re.search(pattern, content, re.DOTALL)

        if match:
            section = match.group(0)
            # - [ ] **[담당자]** - [작업] - 마감: YYYY-MM-DD 형식 추출
            item_pattern = r'\- \[ \] \*\*\[?([^\]]*)\]?\*\* - ([^-]+) - 마감: (\S+)'
            for item_match in re.finditer(item_pattern, section):
                action_items.append({
                    "assignee": item_match.group(1).strip(),
                    "task": item_match.group(2).strip(),
                    "deadline": item_match.group(3).strip(),
                    "status": "pending"
                })

        return action_items

    def _extract_decisions(self, content: str) -> List[Dict]:
        """결정사항 추출"""
        decisions = []

        # "## ✅ 결정사항" 섹션 찾기
        pattern = r'## ✅ 결정사항.*?\|.*?\n(.*?)(?=##|$)'
        match = re.search(pattern, content, re.DOTALL)

        if match:
            section = match.group(1)
            # 테이블 행 추출
            row_pattern = r'\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|'
            for row_match in re.finditer(row_pattern, section):
                decisions.append({
                    "decision": row_match.group(1).strip(),
                    "owner": row_match.group(2).strip(),
                    "deadline": row_match.group(3).strip()
                })

        return decisions

    def _analyze_ssot_impact(self, content: str) -> Dict:
        """SSOT 영향 분석"""
        ssot_sections = [
            'model-selection',
            'prompt-engineering',
            'inference-strategy',
            'evaluation',
            'scaling-laws',
            'error-handling'
        ]

        affected = []
        for section in ssot_sections:
            if section in content.lower():
                affected.append(section)

        return {
            "has_impact": len(affected) > 0,
            "affected_sections": affected,
            "requires_update": len(affected) > 0
        }

    # ===== Public Query Methods =====

    def list_meetings(self, limit: int = 10) -> List[Dict]:
        """최근 회의록 목록"""
        meetings = []
        for file in sorted(self.meetings_dir.glob("*.md"), reverse=True)[:limit]:
            if not file.name.startswith('_'):
                meetings.append({
                    "file": file.name,
                    "path": str(file),
                    "modified": file.stat().st_mtime
                })
        return meetings

    def get_pending_action_items(self) -> List[Dict]:
        """진행 중인 액션 아이템"""
        pending = []
        for file in self.meetings_dir.glob("*.md"):
            if not file.name.startswith('_'):
                content = file.read_text(encoding='utf-8')
                items = self._extract_action_items(content)
                pending.extend(items)
        return pending


# ===== CLI 헬퍼 함수 =====

def create_sample_meeting():
    """샘플 회의 생성 (테스트용)"""
    engine = MeetingEngine()
    date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    path = engine.create_meeting(
        date=date,
        title="LLM 모델 선택 논의",
        description="팀에서 사용할 기본 모델을 결정하는 회의",
        participants=["John", "Jane", "Bob"],
        duration_minutes=60,
        location="회의실 A"
    )
    print(f"✅ 회의 생성됨: {path}")
    return path


if __name__ == "__main__":
    # 테스트
    create_sample_meeting()
