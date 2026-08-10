#!/usr/bin/env python3
"""
SSOT 자동화 엔진
- SSOT 콘텐츠 업데이트
- 변경 이력 추적
- 버전 관리
- 링크 검증
"""

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


class SSOTEngine:
    """SSOT 문서를 관리하는 엔진"""

    def __init__(self, vault_path: str = "./llm-ssot"):
        self.vault_path = Path(vault_path)
        self.ssot_file = self.vault_path / "SSOT.md"
        self.changelog_file = self.vault_path / ".SSOT_CHANGELOG.json"

    def update_section(
        self,
        section_name: str,
        new_content: str,
        reason: str,
        author: str
    ) -> Dict:
        """
        SSOT 섹션 업데이트

        Args:
            section_name: 업데이트할 섹션명 (예: "model-selection")
            new_content: 새 콘텐츠
            reason: 변경 사유
            author: 작성자

        Returns:
            업데이트 결과
        """
        if not self.ssot_file.exists():
            return {"error": "SSOT.md를 찾을 수 없음"}

        content = self.ssot_file.read_text(encoding='utf-8')

        # 섹션 찾기 및 업데이트
        section_pattern = f"## {self._format_section_title(section_name)}.*?(?=##|$)"
        match = re.search(section_pattern, content, re.DOTALL)

        if not match:
            return {"error": f"섹션을 찾을 수 없음: {section_name}"}

        # 새 섹션 생성
        updated_section = f"## {self._format_section_title(section_name)}\n\n{new_content}"

        # 콘텐츠 업데이트
        new_content_full = content[:match.start()] + updated_section + content[match.end():]

        # 버전 증가
        new_version = self._increment_version(new_content_full)
        new_content_full = re.sub(
            r"(\| 2026-\d{2}-\d{2} \| )v[\d.]+",
            f"\\1{new_version}",
            new_content_full
        )

        # 변경 이력 추가
        change_log = self._append_change_log(
            section_name,
            new_version,
            reason,
            author
        )

        # 파일 저장
        self.ssot_file.write_text(new_content_full, encoding='utf-8')

        return {
            "status": "success",
            "section": section_name,
            "new_version": new_version,
            "changed_at": datetime.now().isoformat(),
            "change_log": change_log
        }

    def validate_links(self) -> Dict:
        """
        SSOT 내 모든 링크 검증

        Returns:
            링크 검증 결과
        """
        content = self.ssot_file.read_text(encoding='utf-8')

        # 마크다운 링크 추출: [[file.md]]
        link_pattern = r'\[\[([^\]]+)\]\]'
        links = re.findall(link_pattern, content)

        broken_links = []
        valid_links = []

        for link in links:
            # 파일 또는 섹션인지 확인
            if '#' in link:
                # 섹션 링크
                file_part = link.split('#')[0]
                target_file = self.vault_path / file_part
                if not target_file.exists():
                    broken_links.append(link)
                else:
                    valid_links.append(link)
            else:
                # 파일 링크
                target_file = self.vault_path / link
                if not target_file.exists():
                    broken_links.append(link)
                else:
                    valid_links.append(link)

        return {
            "total_links": len(links),
            "valid_links": len(valid_links),
            "broken_links": broken_links,
            "valid_percentage": (len(valid_links) / len(links) * 100) if links else 0
        }

    def get_change_history(self, section: str = None) -> List[Dict]:
        """
        변경 이력 조회

        Args:
            section: 특정 섹션만 조회 (선택)

        Returns:
            변경 이력 목록
        """
        if not self.changelog_file.exists():
            return []

        with open(self.changelog_file, 'r', encoding='utf-8') as f:
            history = json.load(f)

        if section:
            history = [h for h in history if h.get('section') == section]

        return sorted(history, key=lambda x: x.get('timestamp'), reverse=True)

    def get_current_version(self) -> str:
        """현재 SSOT 버전 조회"""
        content = self.ssot_file.read_text(encoding='utf-8')
        match = re.search(r'버전: (v[\d.]+)', content)
        return match.group(1) if match else "v1.0.0"

    def get_impact_analysis(self, section: str) -> Dict:
        """
        섹션 변경의 영향 분석

        Args:
            section: 변경된 섹션

        Returns:
            영향받는 항목들
        """
        # 해당 섹션을 참조하는 다른 파일들 찾기
        affected_files = []
        affected_meetings = []

        # Decisions 폴더에서 참조 찾기
        decisions_dir = self.vault_path / "Decisions"
        if decisions_dir.exists():
            for file in decisions_dir.glob("*.md"):
                content = file.read_text(encoding='utf-8')
                if section.lower() in content.lower():
                    affected_files.append(str(file.name))

        # Meetings 폴더에서 참조 찾기
        meetings_dir = self.vault_path / "Meetings"
        if meetings_dir.exists():
            for file in meetings_dir.glob("*.md"):
                content = file.read_text(encoding='utf-8')
                if section.lower() in content.lower():
                    affected_meetings.append(str(file.name))

        return {
            "section": section,
            "affected_decisions": affected_files,
            "affected_meetings": affected_meetings,
            "total_impact": len(affected_files) + len(affected_meetings)
        }

    # ===== Private Methods =====

    def _format_section_title(self, name: str) -> str:
        """섹션명을 포맷된 제목으로 변환"""
        titles = {
            "model-selection": "📌 모델 선택",
            "prompt-engineering": "💬 프롬프트 엔지니어링",
            "inference-strategy": "🔄 추론 전략",
            "evaluation": "📊 평가 방법론",
            "scaling-laws": "📈 스케일링 법칙",
            "error-handling": "⚠️ 에러 처리"
        }
        return titles.get(name, name)

    def _increment_version(self, content: str) -> str:
        """버전을 1 증가"""
        match = re.search(r'v(\d+)\.(\d+)\.(\d+)', content)
        if match:
            major, minor, patch = map(int, match.groups())
            patch += 1
            return f"v{major}.{minor}.{patch}"
        return "v1.0.1"

    def _append_change_log(
        self,
        section: str,
        version: str,
        reason: str,
        author: str
    ) -> Dict:
        """변경 이력 파일에 기록"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "section": section,
            "version": version,
            "reason": reason,
            "author": author
        }

        # 기존 로그 읽기
        history = []
        if self.changelog_file.exists():
            with open(self.changelog_file, 'r', encoding='utf-8') as f:
                history = json.load(f)

        # 새 항목 추가
        history.append(entry)

        # 저장
        with open(self.changelog_file, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=2)

        return entry

    def _extract_section_content(self, content: str, section: str) -> str:
        """섹션 콘텐츠 추출"""
        pattern = f"## {self._format_section_title(section)}.*?(?=##|$)"
        match = re.search(pattern, content, re.DOTALL)
        return match.group(0) if match else ""


# ===== Public Methods =====

def generate_ssot_report(vault_path: str = "./llm-ssot") -> Dict:
    """SSOT 상태 리포트 생성"""
    engine = SSOTEngine(vault_path)

    return {
        "timestamp": datetime.now().isoformat(),
        "version": engine.get_current_version(),
        "links": engine.validate_links(),
        "recent_changes": engine.get_change_history()[:5]
    }


if __name__ == "__main__":
    # 테스트
    report = generate_ssot_report()
    print(json.dumps(report, indent=2, ensure_ascii=False))
