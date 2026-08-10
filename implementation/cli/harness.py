#!/usr/bin/env python3
"""
LLM SSOT Harness - 메인 CLI
회의 자동화, SSOT 관리, ADR 추적 통합 도구
"""

import sys
import argparse
import json
from datetime import datetime
from pathlib import Path

# 엔진 import (상위 폴더에서)
sys.path.insert(0, str(Path(__file__).parent.parent))
from engines.meeting_engine import MeetingEngine
from engines.ssot_engine import SSOTEngine


class HarnessCLI:
    """메인 CLI 클래스"""

    def __init__(self, vault_path: str = "./llm-ssot"):
        self.vault_path = vault_path
        self.meeting_engine = MeetingEngine(vault_path)
        self.ssot_engine = SSOTEngine(vault_path)

    def run(self, args):
        """메인 실행 함수"""
        parser = self._create_parser()
        parsed_args = parser.parse_args(args)

        if not hasattr(parsed_args, 'func'):
            parser.print_help()
            return 1

        try:
            result = parsed_args.func(parsed_args)
            if result is not None:
                if isinstance(result, dict):
                    print(json.dumps(result, indent=2, ensure_ascii=False))
                else:
                    print(result)
            return 0
        except Exception as e:
            print(f"❌ 에러: {e}", file=sys.stderr)
            return 1

    def _create_parser(self):
        """CLI 파서 생성"""
        parser = argparse.ArgumentParser(
            description="LLM SSOT Harness - 회의 자동화 및 SSOT 관리",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
예제:
  # 회의 생성
  harness meeting:create --date 2026-08-17 --title "모델 선택 논의"

  # 회의록 처리
  harness meeting:process /path/to/meeting.md

  # SSOT 상태 확인
  harness status

  # 액션 아이템 확인
  harness action-items

  # SSOT 링크 검증
  harness ssot:validate
            """
        )

        subparsers = parser.add_subparsers(title='명령어', dest='command')

        # ===== meeting 명령어 그룹 =====
        meeting_parser = subparsers.add_parser('meeting:create', help='새 회의 생성')
        meeting_parser.add_argument('--date', required=True, help='회의 날짜 (YYYY-MM-DD)')
        meeting_parser.add_argument('--title', required=True, help='회의 제목')
        meeting_parser.add_argument('--description', default='', help='회의 설명')
        meeting_parser.add_argument('--participants', nargs='+', help='참석자 목록')
        meeting_parser.add_argument('--duration', type=int, default=60, help='소요시간 (분)')
        meeting_parser.add_argument('--location', default='온라인', help='장소')
        meeting_parser.set_defaults(func=self.cmd_meeting_create)

        meeting_process = subparsers.add_parser('meeting:process', help='회의록 자동 처리')
        meeting_process.add_argument('file', help='회의록 파일 경로')
        meeting_process.add_argument('--auto-adr', action='store_true', help='ADR 자동 생성')
        meeting_process.add_argument('--notify', action='store_true', help='Slack 알림 (기본: off)')
        meeting_process.set_defaults(func=self.cmd_meeting_process)

        meeting_list = subparsers.add_parser('meeting:list', help='최근 회의록 목록')
        meeting_list.add_argument('--limit', type=int, default=10, help='개수 제한')
        meeting_list.set_defaults(func=self.cmd_meeting_list)

        # ===== ssot 명령어 그룹 =====
        ssot_update = subparsers.add_parser('ssot:update', help='SSOT 섹션 업데이트')
        ssot_update.add_argument('section', help='섹션명 (model-selection, prompt-engineering 등)')
        ssot_update.add_argument('--file', required=True, help='새 콘텐츠 파일')
        ssot_update.add_argument('--reason', required=True, help='변경 사유')
        ssot_update.add_argument('--author', required=True, help='작성자')
        ssot_update.set_defaults(func=self.cmd_ssot_update)

        ssot_validate = subparsers.add_parser('ssot:validate', help='SSOT 링크 검증')
        ssot_validate.set_defaults(func=self.cmd_ssot_validate)

        ssot_history = subparsers.add_parser('ssot:history', help='SSOT 변경 이력')
        ssot_history.add_argument('--section', help='특정 섹션만 조회')
        ssot_history.add_argument('--limit', type=int, default=10, help='개수 제한')
        ssot_history.set_defaults(func=self.cmd_ssot_history)

        # ===== 일반 명령어 =====
        status = subparsers.add_parser('status', help='하네스 상태 확인')
        status.set_defaults(func=self.cmd_status)

        action_items = subparsers.add_parser('action-items', help='진행 중인 액션 아이템')
        action_items.set_defaults(func=self.cmd_action_items)

        report = subparsers.add_parser('report', help='리포트 생성')
        report.add_argument('--type', choices=['daily', 'weekly', 'monthly'], default='daily')
        report.set_defaults(func=self.cmd_report)

        version = subparsers.add_parser('version', help='하네스 버전')
        version.set_defaults(func=self.cmd_version)

        return parser

    # ===== Meeting Commands =====

    def cmd_meeting_create(self, args):
        """meeting:create 커맨드"""
        path = self.meeting_engine.create_meeting(
            date=args.date,
            title=args.title,
            description=args.description,
            participants=args.participants,
            duration_minutes=args.duration,
            location=args.location
        )
        return {
            "status": "success",
            "message": f"✅ 회의 생성됨",
            "file": path,
            "created_at": datetime.now().isoformat()
        }

    def cmd_meeting_process(self, args):
        """meeting:process 커맨드"""
        result = self.meeting_engine.process_meeting_record(args.file)

        output = {
            "status": "success",
            "file": args.file,
            "summary": {
                "action_items_count": len(result['action_items']),
                "decisions_count": len(result['decisions']),
                "ssot_impact": result['ssot_impact'],
                "needs_adr": result['needs_adr']
            },
            "details": result
        }

        # ADR 자동 생성 옵션
        if args.auto_adr and result['needs_adr']:
            output['adr_suggestion'] = self._generate_adr_suggestion(result)

        return output

    def cmd_meeting_list(self, args):
        """meeting:list 커맨드"""
        meetings = self.meeting_engine.list_meetings(args.limit)
        return {
            "status": "success",
            "count": len(meetings),
            "meetings": meetings
        }

    # ===== SSOT Commands =====

    def cmd_ssot_update(self, args):
        """ssot:update 커맨드"""
        # 파일에서 새 콘텐츠 읽기
        with open(args.file, 'r', encoding='utf-8') as f:
            new_content = f.read()

        result = self.ssot_engine.update_section(
            section_name=args.section,
            new_content=new_content,
            reason=args.reason,
            author=args.author
        )

        if 'error' not in result:
            # 영향 분석
            impact = self.ssot_engine.get_impact_analysis(args.section)
            result['impact_analysis'] = impact

        return result

    def cmd_ssot_validate(self, args):
        """ssot:validate 커맨드"""
        validation = self.ssot_engine.validate_links()

        status = "✅" if not validation['broken_links'] else "⚠️"
        return {
            "status": "success",
            "validation_result": status,
            "details": validation
        }

    def cmd_ssot_history(self, args):
        """ssot:history 커맨드"""
        history = self.ssot_engine.get_change_history(args.section)
        return {
            "status": "success",
            "count": len(history),
            "history": history[:args.limit]
        }

    # ===== General Commands =====

    def cmd_status(self, args):
        """status 커맨드"""
        vault_path = Path(self.vault_path)

        return {
            "status": "operational",
            "timestamp": datetime.now().isoformat(),
            "vault": {
                "path": str(vault_path),
                "exists": vault_path.exists()
            },
            "ssot": {
                "version": self.ssot_engine.get_current_version(),
                "links": self.ssot_engine.validate_links()
            },
            "meetings": {
                "total": len(list(vault_path.glob("Meetings/*.md"))),
                "pending_actions": len(self.meeting_engine.get_pending_action_items())
            }
        }

    def cmd_action_items(self, args):
        """action-items 커맨드"""
        items = self.meeting_engine.get_pending_action_items()

        # 마감일 기준으로 정렬
        items_sorted = sorted(items, key=lambda x: x.get('deadline', ''))

        return {
            "status": "success",
            "count": len(items_sorted),
            "action_items": items_sorted
        }

    def cmd_report(self, args):
        """report 커맨드"""
        meetings = self.meeting_engine.list_meetings(limit=100)
        action_items = self.meeting_engine.get_pending_action_items()

        return {
            "status": "success",
            "report_type": args.type,
            "period": datetime.now().isoformat(),
            "summary": {
                "total_meetings": len(meetings),
                "pending_action_items": len(action_items),
                "overdue_items": len([
                    item for item in action_items
                    if item.get('deadline') < datetime.now().isoformat()
                ])
            }
        }

    def cmd_version(self, args):
        """version 커맨드"""
        return {
            "harness_version": "v2.0.0",
            "ssot_version": self.ssot_engine.get_current_version(),
            "python_version": sys.version
        }

    # ===== Helper Methods =====

    def _generate_adr_suggestion(self, meeting_result: dict) -> str:
        """ADR 제안 생성"""
        decisions = meeting_result['decisions']
        if not decisions:
            return ""

        suggestion = f"""
제안된 ADR:

제목: {decisions[0].get('decision', 'TBD')}
의사결정자: {decisions[0].get('owner', 'TBD')}
마감일: {decisions[0].get('deadline', 'TBD')}

→ ADR 파일을 Decisions/ 폴더에 생성하세요.
"""
        return suggestion.strip()


def main():
    """메인 진입점"""
    cli = HarnessCLI()
    return cli.run(sys.argv[1:])


if __name__ == "__main__":
    sys.exit(main())
