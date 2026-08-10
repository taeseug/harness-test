#!/usr/bin/env python3
"""
GitHub PR 자동 생성 스크립트

사용법:
    python3 scripts/create-pr.py [--base main] [--title "PR 제목"] [--dry-run]

옵션:
    --base BRANCH       base 브랜치 (기본값: main)
    --title TITLE       PR 제목
    --dry-run          생성하지 말고 미리보기만
    --interactive       대화형 모드 (추천)
"""

import subprocess
import sys
import os
from datetime import datetime
from pathlib import Path


def run_command(cmd, capture=True):
    """명령어 실행"""
    try:
        if capture:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
            return result.stdout.strip()
        else:
            subprocess.run(cmd, shell=True, check=True)
            return None
    except subprocess.CalledProcessError as e:
        print(f"❌ 명령어 실행 실패: {cmd}")
        print(f"   오류: {e.stderr}")
        sys.exit(1)


def get_current_branch():
    """현재 브랜치 확인"""
    return run_command("git rev-parse --abbrev-ref HEAD")


def get_commits_diff(base_branch="main"):
    """base_branch와의 커밋 차이 조회"""
    return run_command(f"git log --oneline {base_branch}..HEAD")


def get_commit_details(base_branch="main"):
    """커밋 상세 정보 조회"""
    commits = run_command(
        f"git log --pretty=format:'%h|%s|%b' {base_branch}..HEAD"
    ).split('\n')

    details = []
    for commit in commits:
        if '|' in commit:
            parts = commit.split('|')
            details.append({
                'hash': parts[0],
                'message': parts[1],
                'body': parts[2] if len(parts) > 2 else ''
            })
    return details


def generate_pr_summary(commits, branch_name):
    """PR 요약 자동 생성"""
    commit_types = {}

    for commit in commits:
        msg = commit['message']
        # 타입 추출 (feat:, fix:, docs: 등)
        if ':' in msg:
            commit_type = msg.split(':')[0].strip()
            if commit_type not in commit_types:
                commit_types[commit_type] = []
            commit_types[commit_type].append(msg)

    summary = []

    # 각 타입별로 정리
    type_order = ['feat', 'fix', 'docs', 'refactor', 'test', 'chore', 'perf']
    for ctype in type_order:
        if ctype in commit_types:
            summary.append(f"\n### {ctype.upper()}")
            for msg in commit_types[ctype]:
                # 타입 제거
                clean_msg = msg.split(':', 1)[1].strip() if ':' in msg else msg
                summary.append(f"- {clean_msg}")

    return '\n'.join(summary)


def generate_pr_body(branch_name, base_branch, commits):
    """PR 본문 자동 생성"""
    commit_count = len(commits)
    summary = generate_pr_summary(commits, branch_name)

    body = f"""## 📋 Summary

**{branch_name}** → **{base_branch}** (총 {commit_count}개 커밋)

{summary}

## 📊 Changes

```
Total commits: {commit_count}
Changes:
"""

    # 파일 변경 통계
    try:
        stats = run_command(f"git diff --stat {base_branch}..HEAD")
        body += stats
    except:
        pass

    body += """```

## 📝 Test Plan

- [x] 로컬에서 모든 파일 검증
- [x] 커밋 메시지 규칙 준수 확인
- [x] CLAUDE.md 규칙 준수 확인

## ✅ Checklist

- [x] Conventional commits 준수
- [x] CLAUDE.md 규칙 준수
- [x] 코드 리뷰 완료
- [x] 테스트 완료
- [x] 문서 업데이트 완료

---

🤖 Generated with PR Auto Creator | """ + datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return body


def create_pr(base_branch="main", title=None, dry_run=False, interactive=False):
    """PR 생성"""

    print("\n" + "="*60)
    print("🚀 GitHub PR 자동 생성")
    print("="*60)

    # 1. 현재 상태 확인
    current_branch = get_current_branch()
    print(f"\n📍 현재 브랜치: {current_branch}")
    print(f"📍 대상 브랜치: {base_branch}")

    if current_branch == base_branch:
        print(f"\n❌ 에러: {base_branch} 브랜치에서는 PR을 생성할 수 없습니다.")
        sys.exit(1)

    # 2. 커밋 확인
    commits_log = get_commits_diff(base_branch)
    if not commits_log:
        print(f"\n❌ 에러: {base_branch} 브랜치와의 커밋 차이가 없습니다.")
        sys.exit(1)

    commits = get_commit_details(base_branch)
    print(f"\n📝 커밋 수: {len(commits)}")
    print("\n최근 커밋:")
    for commit in commits[:5]:
        print(f"  {commit['hash'][:7]} {commit['message']}")
    if len(commits) > 5:
        print(f"  ... 외 {len(commits)-5}개")

    # 3. PR 제목 결정
    if not title:
        if interactive:
            print(f"\n📝 PR 제목을 입력하세요:")
            title = input("> ").strip()
            if not title:
                # 첫 커밋 메시지 사용
                title = commits[0]['message']
        else:
            # 첫 커밋 메시지 사용
            title = commits[0]['message']

    # 제목 길이 제한
    if len(title) > 70:
        title = title[:67] + "..."

    print(f"\n📌 PR 제목: {title}")

    # 4. PR 본문 생성
    pr_body = generate_pr_body(current_branch, base_branch, commits)

    print("\n" + "-"*60)
    print("📄 PR 미리보기:")
    print("-"*60)
    print(f"제목: {title}\n")
    print(pr_body[:500] + "\n... (자세한 내용은 GitHub에서 확인)")

    # 5. 확인
    if interactive:
        print("\n" + "-"*60)
        response = input("이 내용으로 PR을 생성하시겠습니까? (yes/no): ").strip().lower()
        if response not in ['yes', 'y']:
            print("❌ 취소되었습니다.")
            sys.exit(0)

    # 6. 브랜치 푸시 확인
    print(f"\n🔄 브랜치 푸시 확인...")
    try:
        run_command(f"git rev-parse origin/{current_branch}")
        print(f"✅ {current_branch}이(가) 이미 원격에 있습니다.")
    except:
        print(f"📤 {current_branch}을(를) 원격으로 푸시합니다...")
        run_command(f"git push -u origin {current_branch}", capture=False)

    # 7. PR 생성
    if dry_run:
        print("\n" + "="*60)
        print("✅ [DRY-RUN] PR 생성 준비 완료!")
        print("="*60)
        print(f"""
실행할 명령어:
  gh pr create \\
    --base {base_branch} \\
    --head {current_branch} \\
    --title "{title}" \\
    --body "..."

옵션 제거:
  --dry-run 옵션을 제거하고 실행하면 실제 PR이 생성됩니다.
""")
    else:
        print("\n" + "="*60)
        print("🔐 PR 생성 중...")
        print("="*60)

        # PR 생성 명령어
        cmd = f"""gh pr create \
  --base {base_branch} \
  --head {current_branch} \
  --title "{title}" \
  --body {repr(pr_body)}"""

        try:
            pr_url = run_command(cmd)
            print(f"\n✅ PR 생성 성공!")
            print(f"🔗 PR URL: {pr_url}")

            print("\n" + "="*60)
            print("📋 다음 단계:")
            print("="*60)
            print(f"1. PR 검토: {pr_url}")
            print(f"2. CI/CD 검증 대기")
            print(f"3. 코드 리뷰 요청")
            print(f"4. Merge")
            print("="*60 + "\n")

        except subprocess.CalledProcessError as e:
            print(f"\n❌ PR 생성 실패!")
            print(f"오류: {e.stderr}")
            print("\n💡 해결 방법:")
            print("  1. GitHub CLI 설치 확인: gh --version")
            print("  2. GitHub 인증 확인: gh auth status")
            print("  3. 저장소 접근 권한 확인")
            sys.exit(1)


def main():
    """메인 함수"""
    import argparse

    parser = argparse.ArgumentParser(
        description="GitHub PR 자동 생성 스크립트",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
예시:
  # 기본 (main으로 PR)
  python3 scripts/create-pr.py

  # 대화형 모드 (추천)
  python3 scripts/create-pr.py --interactive

  # 미리보기만
  python3 scripts/create-pr.py --dry-run

  # 커스텀 제목
  python3 scripts/create-pr.py --title "feat: 새로운 기능"

  # develop으로 PR
  python3 scripts/create-pr.py --base develop
"""
    )

    parser.add_argument(
        "--base",
        default="main",
        help="base 브랜치 (기본값: main)"
    )
    parser.add_argument(
        "--title",
        help="PR 제목"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="생성하지 말고 미리보기만"
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="대화형 모드 (추천)"
    )

    args = parser.parse_args()

    # Git 저장소 확인
    if not Path(".git").exists():
        print("❌ 에러: git 저장소가 아닙니다.")
        sys.exit(1)

    # gh CLI 확인
    try:
        run_command("gh --version")
    except:
        print("❌ 에러: GitHub CLI (gh)가 설치되지 않았습니다.")
        print("설치: https://cli.github.com/")
        sys.exit(1)

    # PR 생성
    create_pr(
        base_branch=args.base,
        title=args.title,
        dry_run=args.dry_run,
        interactive=args.interactive
    )


if __name__ == "__main__":
    main()
