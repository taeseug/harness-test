#!/usr/bin/env python3
"""
병합된 액션 아이템을 마크다운 파일로 생성하는 스크립트

사용법:
  python3 generate-action-items-md.py
  python3 generate-action-items-md.py --input <JSON파일> --output <마크다운파일>
"""

import json
import logging
from datetime import datetime
from typing import Dict, List
from pathlib import Path


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ActionMarkdownGenerator:
    """액션 아이템 JSON을 마크다운으로 변환합니다."""

    def generate(self, input_file: str, output_file: str) -> str:
        """JSON → 마크다운 변환"""
        logger.info(f"입력 파일 읽기: {input_file}")

        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 마크다운 생성
        markdown = self._generate_markdown(data)

        # 파일 저장
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown)

        logger.info(f"✅ 마크다운 생성 완료: {output_file}")
        return markdown

    def _generate_markdown(self, data: Dict) -> str:
        """마크다운 콘텐츠 생성"""
        logger.info("마크다운 생성 중...")

        lines = []

        # 헤더
        lines.append("# 📌 액션 아이템 추적 (자동 생성)")
        lines.append("")
        lines.append(f"**최종 업데이트**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append(f"**총 아이템**: {data['total_actions']}개")
        lines.append("")
        lines.append("---")
        lines.append("")

        # 통계
        stats = data.get('stats', {})
        lines.append("## 📊 요약")
        lines.append("")
        lines.append("| 상태 | 수량 | 비율 |")
        lines.append("|------|------|------|")

        total = data['total_actions']
        by_status = stats.get('by_status', {})

        for status, count in sorted(by_status.items()):
            if total > 0:
                percentage = (count / total) * 100
                lines.append(f"| {status} | {count}개 | {percentage:.0f}% |")

        lines.append("")
        lines.append("---")
        lines.append("")

        # 담당자별 통계
        by_owner = stats.get('by_owner', {})
        if by_owner:
            lines.append("## 👥 담당자별 통계")
            lines.append("")
            lines.append("| 담당자 | 액션 수 |")
            lines.append("|--------|--------|")
            for owner, count in sorted(by_owner.items(), key=lambda x: x[1], reverse=True):
                lines.append(f"| {owner} | {count}개 |")
            lines.append("")
            lines.append("---")
            lines.append("")

        # 상태별 액션
        actions_by_status = data.get('actions_by_status', {})

        for status, actions in actions_by_status.items():
            if actions:
                lines.append(f"## {status} ({len(actions)}개)")
                lines.append("")

                for action in actions:
                    lines.extend(self._format_action(action))

                lines.append("")

        lines.append("---")
        lines.append("")
        lines.append("## 📝 메모")
        lines.append("")
        lines.append("이 파일은 자동 생성되었습니다.")
        lines.append("")
        lines.append(f"- 생성 시간: {datetime.now().isoformat()}")
        lines.append(f"- 스크립트: scripts/generate-action-items-md.py")
        lines.append(f"- 소스: scripts/output/merged_actions.json")

        return "\n".join(lines)

    def _format_action(self, action: Dict) -> List[str]:
        """단일 액션 포매팅"""
        lines = []

        title = action.get('title', '제목 없음')
        owner = action.get('owner', '미정')
        status = action.get('status', '불명')
        due_date = action.get('due_date', '미정')
        goal = action.get('goal', '')
        criteria = action.get('criteria', '')
        related_meeting = action.get('related_meeting', '')

        # 체크박스 상태
        checkbox = '- [x]' if status == '완료' else '- [ ]'

        # 제목
        lines.append(f"{checkbox} **[{owner}]** {title}")

        # 상세 정보
        if due_date and due_date != '미정':
            lines.append(f"  - **마감**: {due_date}")
        if goal:
            lines.append(f"  - **목표**: {goal}")
        if criteria:
            lines.append(f"  - **기준**: {criteria}")
        if related_meeting:
            lines.append(f"  - **연관**: [[{related_meeting}]]")

        lines.append("")

        return lines


def main():
    """메인 함수"""
    import argparse

    parser = argparse.ArgumentParser(
        description="액션 아이템을 마크다운으로 생성합니다"
    )
    parser.add_argument(
        "--input",
        help="입력 JSON 파일",
        default="scripts/output/merged_actions.json"
    )
    parser.add_argument(
        "--output",
        help="출력 마크다운 파일",
        default="obsidian-vault/Actions/ACTION_ITEMS.md"
    )

    args = parser.parse_args()

    # 입력 파일 확인
    if not Path(args.input).exists():
        logger.error(f"❌ 입력 파일을 찾을 수 없습니다: {args.input}")
        return 1

    # 출력 디렉토리 생성
    output_dir = Path(args.output).parent
    if not output_dir.exists():
        output_dir.mkdir(parents=True)
        logger.info(f"출력 디렉토리 생성: {output_dir}")

    try:
        generator = ActionMarkdownGenerator()
        markdown = generator.generate(args.input, args.output)

        logger.info("✅ 마크다운 생성 완료!")
        logger.info(f"📝 파일 크기: {len(markdown)} 바이트")
        logger.info(f"📄 저장 위치: {args.output}")

        return 0

    except Exception as e:
        logger.error(f"❌ 오류 발생: {e}")
        return 1


if __name__ == "__main__":
    exit(main())
