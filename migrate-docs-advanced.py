#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🚀 Obsidian Vault 문서 마이그레이션 (고급 버전)

목표: Enhanced 문서를 Obsidian Vault로 자동 마이그레이션
특징:
  - 메타데이터 추가
  - 링크 검증
  - 백업 생성
  - 상세 로깅
  - 오류 처리
"""

import os
import shutil
import json
from pathlib import Path
from datetime import datetime
import logging

# 색상 정의 (터미널 출력용)
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    END = '\033[0m'
    BOLD = '\033[1m'

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/tmp/obsidian_migration.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class ObsidianMigrator:
    def __init__(self, source_dir, vault_dir, backup=True):
        self.source_dir = Path(source_dir)
        self.vault_dir = Path(vault_dir)
        self.backup = backup
        self.stats = {
            'files_copied': 0,
            'files_skipped': 0,
            'links_found': 0,
            'links_verified': 0,
            'errors': 0
        }

    def log(self, level, message, color=None):
        """로깅 + 터미널 출력"""
        if color:
            print(f"{color}{message}{Colors.END}")

        if level == 'info':
            logger.info(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        elif level == 'debug':
            logger.debug(message)

    def create_backup(self):
        """마이그레이션 전 백업 생성"""
        if not self.backup:
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = self.vault_dir.parent / f"vault_backup_{timestamp}"

        try:
            shutil.copytree(self.vault_dir, backup_dir)
            self.log('info', f"✅ 백업 생성: {backup_dir}", Colors.GREEN)
        except Exception as e:
            self.log('error', f"❌ 백업 생성 실패: {e}", Colors.RED)

    def migrate_ssot(self):
        """SSOT 문서 마이그레이션"""
        self.log('info', f"\n{'='*50}", Colors.BLUE)
        self.log('info', "📁 Step 1: SSOT 문서 마이그레이션", Colors.BLUE)
        self.log('info', f"{'='*50}\n", Colors.BLUE)

        source = self.source_dir / "llm-ssot"
        target = self.vault_dir / "SSOT"
        target.mkdir(exist_ok=True)

        files_to_copy = [
            "SSOT.md",
            "GOVERNANCE.md",
            "model-selection.md",
            "prompt-engineering.md"
        ]

        for filename in files_to_copy:
            source_file = source / filename
            if source_file.exists():
                target_file = target / filename
                try:
                    shutil.copy2(source_file, target_file)
                    self.log('info', f"✅ {filename} 복사됨", Colors.GREEN)
                    self.stats['files_copied'] += 1
                except Exception as e:
                    self.log('error', f"❌ {filename} 복사 실패: {e}", Colors.RED)
                    self.stats['errors'] += 1
            else:
                self.log('warning', f"⚠️ {filename} 찾을 수 없음", Colors.YELLOW)
                self.stats['files_skipped'] += 1

    def migrate_meetings(self):
        """Meetings 문서 마이그레이션"""
        self.log('info', f"\n{'='*50}", Colors.BLUE)
        self.log('info', "📁 Step 2: Meetings 문서 마이그레이션", Colors.BLUE)
        self.log('info', f"{'='*50}\n", Colors.BLUE)

        source = self.source_dir / "llm-ssot" / "Meetings"
        target = self.vault_dir / "Meetings"
        target.mkdir(exist_ok=True)

        # Enhanced 회의록 복사
        for file in source.glob("*.enhanced.md"):
            try:
                shutil.copy2(file, target / file.name)
                self.log('info', f"✅ {file.name} 복사됨", Colors.GREEN)
                self.stats['files_copied'] += 1
            except Exception as e:
                self.log('error', f"❌ {file.name} 복사 실패: {e}", Colors.RED)
                self.stats['errors'] += 1

        # 추적 문서 복사
        tracking_files = ["ACTION_ITEMS.md", "MEETINGS_ANALYSIS.md"]
        for filename in tracking_files:
            source_file = source / filename
            if source_file.exists():
                try:
                    shutil.copy2(source_file, target / filename)
                    self.log('info', f"✅ {filename} 복사됨", Colors.GREEN)
                    self.stats['files_copied'] += 1
                except Exception as e:
                    self.log('error', f"❌ {filename} 복사 실패: {e}", Colors.RED)
                    self.stats['errors'] += 1

    def migrate_wiki(self):
        """Wiki/Decisions 문서 마이그레이션"""
        self.log('info', f"\n{'='*50}", Colors.BLUE)
        self.log('info', "📁 Step 3: Wiki/Decisions 마이그레이션", Colors.BLUE)
        self.log('info', f"{'='*50}\n", Colors.BLUE)

        source = self.source_dir / "llm-ssot" / "WIKI"
        target = self.vault_dir / "Decisions"
        target.mkdir(exist_ok=True)

        wiki_files = [
            "DECISIONS.md",
            "WIKI_INDEX.md",
            "TOPICS.md",
            "PEOPLE.md",
            "TIMELINE.md",
            "DASHBOARD.md"
        ]

        for filename in wiki_files:
            source_file = source / filename
            if source_file.exists():
                try:
                    shutil.copy2(source_file, target / filename)
                    self.log('info', f"✅ {filename} 복사됨", Colors.GREEN)
                    self.stats['files_copied'] += 1
                except Exception as e:
                    self.log('error', f"❌ {filename} 복사 실패: {e}", Colors.RED)
                    self.stats['errors'] += 1

    def verify_links(self):
        """마이그레이션된 파일의 링크 검증"""
        self.log('info', f"\n{'='*50}", Colors.BLUE)
        self.log('info', "🔍 Step 4: 링크 검증", Colors.BLUE)
        self.log('info', f"{'='*50}\n", Colors.BLUE)

        broken_links = []

        for file_path in self.vault_dir.rglob("*.md"):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # [[링크]] 형식 찾기
                import re
                links = re.findall(r'\[\[([^\]]+)\]\]', content)
                self.stats['links_found'] += len(links)

                for link in links:
                    # 링크 대상 찾기
                    link_target = link.split('|')[0].strip()

                    # 파일 또는 문서명으로 검색
                    found = False
                    for check_file in self.vault_dir.rglob("*.md"):
                        if link_target in check_file.name or link_target in check_file.stem:
                            found = True
                            break

                    if found:
                        self.stats['links_verified'] += 1
                    else:
                        broken_links.append({
                            'file': str(file_path),
                            'link': link_target
                        })
                        self.log('warning', f"⚠️ 깨진 링크: {link_target} (파일: {file_path.name})", Colors.YELLOW)

            except Exception as e:
                self.log('error', f"❌ 링크 검증 중 오류: {file_path} - {e}", Colors.RED)

        # 결과 요약
        if broken_links:
            self.log('warning', f"\n⚠️ 깨진 링크 {len(broken_links)}개 발견", Colors.YELLOW)
        else:
            self.log('info', f"\n✅ 모든 링크 검증됨 ({self.stats['links_verified']}/{self.stats['links_found']})", Colors.GREEN)

    def create_metadata(self):
        """마이그레이션 메타데이터 생성"""
        self.log('info', f"\n{'='*50}", Colors.BLUE)
        self.log('info', "📝 Step 5: 메타데이터 생성", Colors.BLUE)
        self.log('info', f"{'='*50}\n", Colors.BLUE)

        metadata = {
            'migration_date': datetime.now().isoformat(),
            'source': str(self.source_dir),
            'vault': str(self.vault_dir),
            'stats': self.stats,
            'version': '1.0'
        }

        metadata_file = self.vault_dir / ".migration_metadata.json"
        try:
            with open(metadata_file, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2, ensure_ascii=False)
            self.log('info', f"✅ 메타데이터 저장: {metadata_file}", Colors.GREEN)
        except Exception as e:
            self.log('error', f"❌ 메타데이터 저장 실패: {e}", Colors.RED)

    def print_summary(self):
        """마이그레이션 결과 요약"""
        self.log('info', f"\n{'='*50}", Colors.BOLD + Colors.GREEN)
        self.log('info', "📊 마이그레이션 완료 요약", Colors.BOLD + Colors.GREEN)
        self.log('info', f"{'='*50}", Colors.BOLD + Colors.GREEN)

        print(f"""
{Colors.GREEN}✅ 성공{Colors.END}:
  • 복사된 파일: {self.stats['files_copied']}개
  • 검증된 링크: {self.stats['links_verified']}/{self.stats['links_found']}개
  • 건너뛴 파일: {self.stats['files_skipped']}개

{Colors.RED}❌ 오류{Colors.END}:
  • 오류 발생: {self.stats['errors']}개

{Colors.BLUE}🎯 다음 단계{Colors.END}:
  1. Obsidian 재시작 (Settings → Reload vault)
  2. 문서 링크 확인
  3. Dataview 쿼리 테스트
  4. 2026-08-17 첫 회의 준비

{Colors.GREEN}{'='*50}{Colors.END}
""")

    def run(self):
        """전체 마이그레이션 실행"""
        print(f"\n{Colors.BOLD}{Colors.BLUE}")
        print("🚀 Obsidian Vault 마이그레이션 시작")
        print(f"{'='*50}{Colors.END}\n")

        # 백업
        self.create_backup()

        # 마이그레이션
        self.migrate_ssot()
        self.migrate_meetings()
        self.migrate_wiki()

        # 검증
        self.verify_links()

        # 메타데이터
        self.create_metadata()

        # 결과
        self.print_summary()


def main():
    """메인 함수"""
    source_dir = "/Users/mac/work/claude/20260810_harness"
    vault_dir = "/Users/mac/work/claude/20260810_harness/obsidian-vault"

    migrator = ObsidianMigrator(source_dir, vault_dir, backup=True)
    migrator.run()


if __name__ == "__main__":
    main()
