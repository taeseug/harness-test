#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🤖 회의 자동화 시스템 (Claude API)

목표: 회의 노트를 Claude로 처리하여 요약, 액션, 결정 자동 추출
사용: python meeting-processor.py <회의_파일_경로>

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

class MeetingProcessor:
    def __init__(self, meeting_file):
        self.meeting_file = Path(meeting_file)
        self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.vault_dir = self.meeting_file.parent.parent
        self.results = {
            'summary': '',
            'actions': [],
            'decisions': [],
            'ssot_impact': []
        }

    def log(self, msg, color=Colors.END):
        """로깅"""
        print(f"{color}{msg}{Colors.END}")

    def read_meeting(self):
        """회의 노트 읽기"""
        try:
            with open(self.meeting_file, 'r', encoding='utf-8') as f:
                content = f.read()
            self.log(f"✅ 회의 노트 읽음: {self.meeting_file.name}", Colors.GREEN)
            return content
        except Exception as e:
            self.log(f"❌ 파일 읽기 실패: {e}", Colors.RED)
            return None

    def analyze_with_claude(self, meeting_content):
        """Claude API로 회의 분석"""
        self.log("\n🤖 Claude로 분석 중...", Colors.CYAN)

        prompt = f"""다음 회의 노트를 분석하고 JSON 형식으로 결과를 제공하세요:

회의 노트:
{meeting_content}

다음을 추출하세요:

1. **summary**: 회의 요약 (3-5문장)
2. **actions**: 액션 아이템 리스트
   각 항목: {{"item": "작업 내용", "owner": "담당자", "due_date": "YYYY-MM-DD", "priority": "높음/중간/낮음"}}
3. **decisions**: 의사결정 사항
   각 항목: {{"decision": "결정 내용", "reason": "근거", "owner": "담당자"}}
4. **ssot_impact**: SSOT 영향도 (해당하는 SSOT 규칙 명시)

JSON 형식으로 정확히 반환하세요:
{{
  "summary": "...",
  "actions": [...],
  "decisions": [...],
  "ssot_impact": [...]
}}"""

        try:
            message = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=2000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            response_text = message.content[0].text

            # JSON 추출 (```json ...``` 형식일 수도 있음)
            if "```json" in response_text:
                json_start = response_text.find("```json") + 7
                json_end = response_text.find("```", json_start)
                json_text = response_text[json_start:json_end].strip()
            elif "```" in response_text:
                json_start = response_text.find("```") + 3
                json_end = response_text.find("```", json_start)
                json_text = response_text[json_start:json_end].strip()
            else:
                json_text = response_text

            result = json.loads(json_text)
            self.log("✅ Claude 분석 완료", Colors.GREEN)
            return result

        except Exception as e:
            self.log(f"❌ Claude 분석 실패: {e}", Colors.RED)
            return None

    def format_actions_markdown(self, actions):
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

    def update_action_items(self):
        """ACTION_ITEMS.md 자동 갱신"""
        action_items_file = self.vault_dir / "Meetings" / "ACTION_ITEMS.md"

        if not action_items_file.exists():
            self.log(f"⚠️ ACTION_ITEMS.md 찾을 수 없음", Colors.YELLOW)
            return

        try:
            with open(action_items_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # 새 액션 섹션 생성
            new_actions = self.format_actions_markdown(self.results['actions'])

            # 기존 ACTION_ITEMS 섹션 찾아 업데이트 (간단한 버전)
            # 실제로는 더 정교한 파싱 필요

            # 마지막에 추가
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            content += f"\n\n---\n\n## 🔄 {timestamp} 추가\n\n{new_actions}"

            with open(action_items_file, 'w', encoding='utf-8') as f:
                f.write(content)

            self.log(f"✅ ACTION_ITEMS.md 갱신됨", Colors.GREEN)

        except Exception as e:
            self.log(f"❌ ACTION_ITEMS.md 갱신 실패: {e}", Colors.RED)

    def save_results(self):
        """분석 결과 저장"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        results_file = self.vault_dir / "Meetings" / f"analysis_{timestamp}.json"

        try:
            with open(results_file, 'w', encoding='utf-8') as f:
                json.dump(self.results, f, indent=2, ensure_ascii=False)
            self.log(f"✅ 분석 결과 저장: {results_file}", Colors.GREEN)
        except Exception as e:
            self.log(f"❌ 결과 저장 실패: {e}", Colors.RED)

    def print_summary(self):
        """결과 요약 출력"""
        print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.BLUE}📊 회의 분석 결과{Colors.END}")
        print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.END}\n")

        # 요약
        print(f"{Colors.CYAN}📝 요약:{Colors.END}")
        print(f"  {self.results['summary']}\n")

        # 액션
        print(f"{Colors.CYAN}📌 액션 아이템 ({len(self.results['actions'])}개):{Colors.END}")
        for action in self.results['actions']:
            print(f"  • {action.get('item')}")
            print(f"    담당: {action.get('owner')}, 마감: {action.get('due_date')}\n")

        # 결정
        print(f"{Colors.CYAN}✅ 의사결정 ({len(self.results['decisions'])}개):{Colors.END}")
        for decision in self.results['decisions']:
            print(f"  • {decision.get('decision')}")
            print(f"    담당: {decision.get('owner')}\n")

        # SSOT 영향
        if self.results['ssot_impact']:
            print(f"{Colors.CYAN}🔗 SSOT 영향:{Colors.END}")
            for impact in self.results['ssot_impact']:
                print(f"  • {impact}\n")

        print(f"{Colors.BOLD}{Colors.GREEN}{'='*60}{Colors.END}")
        print(f"{Colors.GREEN}✅ 분석 완료! 결과는 JSON 파일로 저장되었습니다.{Colors.END}\n")

    def run(self):
        """전체 실행"""
        print(f"\n{Colors.BOLD}{Colors.BLUE}")
        print("🤖 회의 자동화 시스템 (Claude API)")
        print(f"{'='*60}{Colors.END}\n")

        # 1. 회의 노트 읽기
        meeting_content = self.read_meeting()
        if not meeting_content:
            return

        # 2. Claude로 분석
        analysis = self.analyze_with_claude(meeting_content)
        if not analysis:
            return

        # 결과 저장
        self.results = analysis

        # 3. ACTION_ITEMS.md 갱신
        self.update_action_items()

        # 4. 결과 저장
        self.save_results()

        # 5. 결과 출력
        self.print_summary()


def main():
    """메인 함수"""
    if len(sys.argv) < 2:
        print(f"{Colors.RED}❌ 사용법: python meeting-processor.py <회의_파일_경로>{Colors.END}")
        print(f"\n예시: python meeting-processor.py ./obsidian-vault/Meetings/2026-08-17-first-test.md")
        sys.exit(1)

    meeting_file = sys.argv[1]

    if not os.path.exists(meeting_file):
        print(f"{Colors.RED}❌ 파일을 찾을 수 없음: {meeting_file}{Colors.END}")
        sys.exit(1)

    processor = MeetingProcessor(meeting_file)
    processor.run()


if __name__ == "__main__":
    main()
