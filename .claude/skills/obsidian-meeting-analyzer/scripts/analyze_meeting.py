#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🤖 Obsidian 회의 자동 분석 (Claude API)

목표: Obsidian vault의 회의 노트를 Claude로 처리하여 요약, 액션, 결정 자동 추출
사용: python analyze_meeting.py <회의_파일_경로>

기능:
  1. 회의 노트 읽기
  2. Claude API로 분석
  3. 결과 저장 (JSON)
  4. ACTION_ITEMS.md 자동 갱신
"""

import os
import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List, Any
import anthropic

# 색상 정의
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    END = '\033[0m'
    BOLD = '\033[1m'

# 설정
DEFAULT_MODEL = "claude-3-5-sonnet-20241022"
MEETINGS_FOLDER = "Meetings"
ACTION_ITEMS_FILE = "ACTION_ITEMS.md"

class MeetingProcessor:
    def __init__(self, meeting_file: str, vault_root: Optional[str] = None):
        """
        회의 분석기 초기화

        Args:
            meeting_file: 회의 파일 경로
            vault_root: Obsidian vault 루트 경로 (자동 감지 가능)
        """
        self.meeting_file = Path(meeting_file)

        # Vault 루트 자동 감지 또는 명시
        if vault_root:
            self.vault_root = Path(vault_root)
        else:
            # 회의 파일이 Meetings/ 폴더에 있다고 가정하고 상위 폴더 찾기
            self.vault_root = self._find_vault_root()

        # API 클라이언트 초기화
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY 환경변수가 설정되지 않았습니다.")

        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = DEFAULT_MODEL

        self.results: Dict[str, Any] = {
            'summary': '',
            'actions': [],
            'decisions': [],
            'ssot_impact': []
        }

    def _find_vault_root(self) -> Path:
        """Obsidian vault 루트 찾기"""
        current = self.meeting_file.parent

        # Meetings 폴더가 부모에 있는지 확인
        if current.name == MEETINGS_FOLDER:
            return current.parent

        # 상위 폴더에서 Meetings 찾기
        for parent in self.meeting_file.parents:
            if (parent / MEETINGS_FOLDER).exists():
                return parent

        # 못 찾으면 회의 파일 상위 폴더 사용
        return self.meeting_file.parent.parent

    def log(self, msg: str, color: str = Colors.END) -> None:
        """색상 로깅"""
        print(f"{color}{msg}{Colors.END}")

    def read_meeting(self) -> Optional[str]:
        """회의 노트 읽기"""
        try:
            with open(self.meeting_file, 'r', encoding='utf-8') as f:
                content = f.read()
            self.log(f"✅ 회의 노트 읽음: {self.meeting_file.name}", Colors.GREEN)
            return content
        except FileNotFoundError:
            self.log(f"❌ 파일을 찾을 수 없음: {self.meeting_file}", Colors.RED)
            return None
        except Exception as e:
            self.log(f"❌ 파일 읽기 실패: {e}", Colors.RED)
            return None

    def analyze_with_claude(self, meeting_content: str) -> Optional[Dict[str, Any]]:
        """Claude API로 회의 분석"""
        self.log("\n🤖 Claude로 분석 중...", Colors.CYAN)

        prompt = f"""다음 회의 노트를 분석하고 JSON 형식으로 결과를 제공하세요:

회의 노트:
{meeting_content}

다음을 추출하세요:

1. **summary**: 회의 요약 (3-5문장, 주요 내용만)
2. **actions**: 액션 아이템 리스트 (3개 이상 추출)
   각 항목: {{"item": "작업 내용", "owner": "담당자", "due_date": "YYYY-MM-DD", "priority": "높음/중간/낮음"}}
3. **decisions**: 의사결정 사항
   각 항목: {{"decision": "결정 내용", "reason": "근거", "owner": "담당자"}}
4. **ssot_impact**: SSOT 영향도 (해당하는 규칙이 있으면 명시, 없으면 빈 배열)

JSON 형식으로 정확히 반환하세요. Markdown 포장 없이 순수 JSON만:
{{
  "summary": "...",
  "actions": [...],
  "decisions": [...],
  "ssot_impact": [...]
}}"""

        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            response_text = message.content[0].text

            # JSON 추출 (다양한 포맷 지원)
            json_text = self._extract_json(response_text)

            result = json.loads(json_text)
            self.log("✅ Claude 분석 완료", Colors.GREEN)
            return result

        except json.JSONDecodeError as e:
            self.log(f"❌ JSON 파싱 실패: {e}", Colors.RED)
            return None
        except Exception as e:
            self.log(f"❌ Claude 분석 실패: {e}", Colors.RED)
            return None

    def _extract_json(self, response_text: str) -> str:
        """응답에서 JSON 추출"""
        if "```json" in response_text:
            json_start = response_text.find("```json") + 7
            json_end = response_text.find("```", json_start)
            return response_text[json_start:json_end].strip()
        elif "```" in response_text:
            json_start = response_text.find("```") + 3
            json_end = response_text.find("```", json_start)
            return response_text[json_start:json_end].strip()
        else:
            return response_text.strip()

    def format_actions_markdown(self, actions: List[Dict[str, str]]) -> str:
        """액션 아이템을 마크다운으로 포맷"""
        markdown = "## 📌 액션 아이템\n\n"

        # 우선순위별로 정렬
        priority_order = {'높음': 0, '중간': 1, '낮음': 2}
        sorted_actions = sorted(
            actions,
            key=lambda x: priority_order.get(x.get('priority', '중간'), 1)
        )

        for action in sorted_actions:
            item = action.get('item', '(내용 없음)')
            owner = action.get('owner', '(담당자 미정)')
            due = action.get('due_date', '(마감일 미정)')
            priority = action.get('priority', '중간')

            priority_emoji = {
                '높음': '🔴',
                '중간': '🟡',
                '낮음': '🟢'
            }.get(priority, '🟡')

            markdown += f"- [ ] {priority_emoji} **[[{owner}]]** - {item} (마감: {due})\n"

        return markdown

    def update_action_items(self) -> None:
        """ACTION_ITEMS.md 자동 갱신"""
        action_items_file = self.vault_root / MEETINGS_FOLDER / ACTION_ITEMS_FILE

        if not action_items_file.exists():
            self.log(f"⚠️ {ACTION_ITEMS_FILE} 찾을 수 없음: {action_items_file}", Colors.YELLOW)
            return

        try:
            with open(action_items_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # 새 액션 섹션 생성
            new_actions = self.format_actions_markdown(self.results['actions'])

            # 마지막에 추가
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            content += f"\n\n---\n\n## 🔄 {timestamp} 추가\n\n{new_actions}"

            with open(action_items_file, 'w', encoding='utf-8') as f:
                f.write(content)

            self.log(f"✅ {ACTION_ITEMS_FILE} 갱신됨", Colors.GREEN)

        except Exception as e:
            self.log(f"❌ {ACTION_ITEMS_FILE} 갱신 실패: {e}", Colors.RED)

    def save_results(self) -> None:
        """분석 결과 JSON으로 저장"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        results_file = self.vault_root / MEETINGS_FOLDER / f"analysis_{timestamp}.json"

        try:
            with open(results_file, 'w', encoding='utf-8') as f:
                json.dump(self.results, f, indent=2, ensure_ascii=False)
            self.log(f"✅ 분석 결과 저장: {results_file.name}", Colors.GREEN)
        except Exception as e:
            self.log(f"❌ 결과 저장 실패: {e}", Colors.RED)

    def print_summary(self) -> None:
        """결과 요약 출력"""
        print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.BLUE}📊 회의 분석 결과{Colors.END}")
        print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}\n")

        # 요약
        print(f"{Colors.CYAN}📝 요약:{Colors.END}")
        print(f"  {self.results['summary']}\n")

        # 액션
        print(f"{Colors.CYAN}📌 액션 아이템 ({len(self.results['actions'])}개):{Colors.END}")
        for i, action in enumerate(self.results['actions'], 1):
            priority_emoji = {
                '높음': '🔴',
                '중간': '🟡',
                '낮음': '🟢'
            }.get(action.get('priority', '중간'), '🟡')

            print(f"  {i}. {priority_emoji} {action.get('item')}")
            print(f"     담당: {action.get('owner')}, 마감: {action.get('due_date')}\n")

        # 결정
        if self.results['decisions']:
            print(f"{Colors.CYAN}✅ 의사결정 ({len(self.results['decisions'])}개):{Colors.END}")
            for i, decision in enumerate(self.results['decisions'], 1):
                print(f"  {i}. {decision.get('decision')}")
                print(f"     근거: {decision.get('reason')}")
                print(f"     담당: {decision.get('owner')}\n")

        # SSOT 영향
        if self.results['ssot_impact']:
            print(f"{Colors.CYAN}🔗 SSOT 영향:{Colors.END}")
            for impact in self.results['ssot_impact']:
                print(f"  • {impact}\n")

        print(f"{Colors.BOLD}{Colors.GREEN}{'='*60}{Colors.END}")
        print(f"{Colors.GREEN}✅ 분석 완료! 결과는 JSON 파일로 저장되었습니다.{Colors.END}\n")

    def run(self) -> bool:
        """전체 실행 파이프라인"""
        print(f"\n{Colors.BOLD}{Colors.BLUE}")
        print("🤖 Obsidian 회의 자동 분석 (Claude API)")
        print(f"{'='*60}{Colors.END}\n")

        # 1. 회의 노트 읽기
        meeting_content = self.read_meeting()
        if not meeting_content:
            return False

        # 2. Claude로 분석
        analysis = self.analyze_with_claude(meeting_content)
        if not analysis:
            return False

        # 결과 저장
        self.results = analysis

        # 3. ACTION_ITEMS.md 갱신
        self.update_action_items()

        # 4. 결과 저장
        self.save_results()

        # 5. 결과 출력
        self.print_summary()

        return True


def main() -> None:
    """메인 함수"""
    if len(sys.argv) < 2:
        print(f"{Colors.RED}❌ 사용법: python analyze_meeting.py <회의_파일_경로>{Colors.END}")
        print(f"\n예시:")
        print(f"  python analyze_meeting.py ./obsidian-vault/Meetings/2026-08-17-meeting.md")
        print(f"  python analyze_meeting.py ./path/to/meeting.md\n")
        sys.exit(1)

    meeting_file = sys.argv[1]
    vault_root = sys.argv[2] if len(sys.argv) > 2 else None

    if not os.path.exists(meeting_file):
        print(f"{Colors.RED}❌ 파일을 찾을 수 없음: {meeting_file}{Colors.END}")
        sys.exit(1)

    try:
        processor = MeetingProcessor(meeting_file, vault_root)
        success = processor.run()
        sys.exit(0 if success else 1)
    except ValueError as e:
        print(f"{Colors.RED}❌ 설정 오류: {e}{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print(f"{Colors.RED}❌ 예상치 못한 오류: {e}{Colors.END}")
        sys.exit(1)


if __name__ == "__main__":
    main()
