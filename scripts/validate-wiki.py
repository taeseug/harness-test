#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🔍 Wiki 기계 검증 스크립트

목표: Wiki 파일들의 기계적 검증
- Frontmatter 검증 (필수 필드, 포맷)
- 스키마 구조 검증 (섹션, 포맷)
- 파일명 규칙 검증 (명명 규칙)

사용:
python3 scripts/validate-wiki.py ./obsidian-vault/
"""

import os
import json
import re
import sys
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Tuple, Optional
import yaml
import logging

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

# 색상 정의
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    END = '\033[0m'
    BOLD = '\033[1m'

class WikiValidator:
    """Wiki 파일 검증 클래스"""

    def __init__(self, wiki_path: str):
        """
        검증기 초기화

        Args:
            wiki_path: Wiki 루트 경로 (obsidian-vault)
        """
        self.wiki_path = Path(wiki_path)
        self.enhanced_files = []
        self.issues: Dict[str, List[Dict[str, Any]]] = {
            'critical': [],   # 심각한 오류
            'warning': [],    # 경고
            'info': []        # 정보
        }
        self.stats = {
            'total_files': 0,
            'valid_files': 0,
            'files_with_issues': 0
        }

    def log(self, msg: str, color: str = Colors.END) -> None:
        """색상 로깅"""
        print(f"{color}{msg}{Colors.END}")

    # ============================================================================
    # 1. Frontmatter 검증
    # ============================================================================

    def validate_frontmatter(self, file_path: Path) -> Tuple[bool, List[str]]:
        """
        Frontmatter 검증

        필수 필드:
        - date: YYYY-MM-DD 형식
        - type: meeting
        - status: ✅/⏳/❌
        - enhanced_date: YYYY-MM-DD 형식
        """
        issues = []

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Frontmatter 분리
            if not content.startswith('---'):
                issues.append("Frontmatter가 없음 (시작이 '---'이 아님)")
                return False, issues

            parts = content.split('---', 2)
            if len(parts) < 3:
                issues.append("Frontmatter 형식이 잘못됨 (종료 '---' 없음)")
                return False, issues

            try:
                frontmatter = yaml.safe_load(parts[1])
            except yaml.YAMLError as e:
                issues.append(f"YAML 파싱 오류: {str(e)}")
                return False, issues

            if frontmatter is None:
                issues.append("Frontmatter가 비어있음")
                return False, issues

            # 필수 필드 확인
            required_fields = {
                'date': r'^\d{4}-\d{2}-\d{2}$',
                'type': r'^meeting$',
                'status': r'^(✅|⏳|❌)$',
                'enhanced_date': r'^\d{4}-\d{2}-\d{2}$'
            }

            for field, pattern in required_fields.items():
                if field not in frontmatter:
                    issues.append(f"필수 필드 '{field}' 누락")
                else:
                    value = frontmatter[field]
                    if not re.match(pattern, str(value)):
                        issues.append(f"필드 '{field}'의 값이 형식에 맞지 않음: {value}")

            # 참석자 검증 (있으면 좋음)
            if 'participants' in frontmatter:
                if not isinstance(frontmatter['participants'], list):
                    issues.append(f"'participants'는 리스트여야 함: {type(frontmatter['participants'])}")

            return len(issues) == 0, issues

        except Exception as e:
            issues.append(f"예기치 않은 오류: {str(e)}")
            return False, issues

    # ============================================================================
    # 2. 스키마 구조 검증
    # ============================================================================

    def validate_schema(self, file_path: Path) -> Tuple[bool, List[str]]:
        """
        스키마 구조 검증

        필수 섹션:
        - ## 📝 논의 내용
        - ## ✅ 결정사항 또는 ## 🎯 의사결정
        - ## 📌 행동항목 또는 ## 🎯 액션 아이템
        """
        issues = []

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Frontmatter 제거
            if content.startswith('---'):
                parts = content.split('---', 2)
                body = parts[2] if len(parts) > 2 else ''
            else:
                body = content

            # 필수 섹션 확인
            required_sections = {
                '논의 내용': r'## \d*\s*(📝|💬).*논의',
                '의사결정': r'## \d*\s*(✅|🎯).*(결정|의사결정)',
                '액션 아이템': r'## \d*\s*🎯.*(액션|행동)'
            }

            for section_name, pattern in required_sections.items():
                if not re.search(pattern, body, re.IGNORECASE):
                    issues.append(f"필수 섹션 '{section_name}' 없음")

            # 제목 구조 확인 (## 사용 여부)
            if not re.search(r'^##', body, re.MULTILINE):
                issues.append("마크다운 제목(##)이 없음")

            # Frontmatter 정보 섹션 확인 (있으면 좋음)
            if not re.search(r'회의 정보|회의 메타|회의 개요', body, re.IGNORECASE):
                issues.append("'회의 정보' 섹션 없음 (권장)")

            return len(issues) == 0, issues

        except Exception as e:
            issues.append(f"예기치 않은 오류: {str(e)}")
            return False, issues

    # ============================================================================
    # 3. 파일명 규칙 검증
    # ============================================================================

    def validate_filename(self, file_path: Path) -> Tuple[bool, List[str]]:
        """
        파일명 규칙 검증

        규칙: YYYY-MM-DD-<회의명>.enhanced.md
        예: 2026-06-11-제품주간회의.enhanced.md
        """
        issues = []
        filename = file_path.name

        # 기본 확장자 확인
        if not filename.endswith('.enhanced.md'):
            issues.append(f"파일 확장자가 '.enhanced.md'이 아님: {filename}")
            return False, issues

        # 파일명 패턴 확인
        # YYYY-MM-DD-<name>.enhanced.md
        pattern = r'^(\d{4})-(\d{2})-(\d{2})-(.+)\.enhanced\.md$'
        match = re.match(pattern, filename)

        if not match:
            issues.append(f"파일명 형식이 맞지 않음 (YYYY-MM-DD-<name>.enhanced.md): {filename}")
            return False, issues

        # 날짜 검증
        try:
            year, month, day, name = match.groups()
            date_str = f"{year}-{month}-{day}"
            datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            issues.append(f"파일명의 날짜가 유효하지 않음: {date_str}")
            return False, issues

        # 회의명 검증 (한글 또는 영문)
        if not re.match(r'^[\w\s가-힣]+$', name):
            issues.append(f"파일명의 회의명에 유효하지 않은 문자 포함: {name}")
            return False, issues

        return len(issues) == 0, issues

    # ============================================================================
    # 4. 종합 검증
    # ============================================================================

    def validate_file(self, file_path: Path) -> Dict[str, Any]:
        """단일 파일 검증"""
        result = {
            'file': str(file_path.relative_to(self.wiki_path)),
            'frontmatter': {'valid': False, 'issues': []},
            'schema': {'valid': False, 'issues': []},
            'filename': {'valid': False, 'issues': []}
        }

        # 각 항목 검증
        result['frontmatter']['valid'], result['frontmatter']['issues'] = \
            self.validate_frontmatter(file_path)

        result['schema']['valid'], result['schema']['issues'] = \
            self.validate_schema(file_path)

        result['filename']['valid'], result['filename']['issues'] = \
            self.validate_filename(file_path)

        # 전체 유효성
        result['valid'] = (
            result['frontmatter']['valid'] and
            result['schema']['valid'] and
            result['filename']['valid']
        )

        return result

    def run(self) -> Dict[str, Any]:
        """전체 검증 실행"""
        self.log("\n" + "="*60)
        self.log("🔍 Wiki 기계 검증 시작", Colors.BOLD + Colors.BLUE)
        self.log("="*60)

        # Enhanced 파일 찾기
        self.enhanced_files = list(self.wiki_path.glob('**/*.enhanced.md'))
        self.stats['total_files'] = len(self.enhanced_files)

        if not self.enhanced_files:
            self.log(f"❌ Enhanced 파일을 찾을 수 없음: {self.wiki_path}")
            return self._generate_report([])

        self.log(f"\n📊 발견된 파일: {self.stats['total_files']}개\n")

        # 파일별 검증
        results = []
        for i, file_path in enumerate(self.enhanced_files, 1):
            result = self.validate_file(file_path)
            results.append(result)

            # 상태 출력
            status = f"✅" if result['valid'] else f"❌"
            filename = file_path.name
            self.log(f"{status} [{i}/{self.stats['total_files']}] {filename}")

            # 이슈 출력
            if not result['valid']:
                self.stats['files_with_issues'] += 1
                for category in ['frontmatter', 'schema', 'filename']:
                    if not result[category]['valid']:
                        for issue in result[category]['issues']:
                            self.log(f"   ⚠️ [{category}] {issue}", Colors.YELLOW)
            else:
                self.stats['valid_files'] += 1

        return self._generate_report(results)

    def _generate_report(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """검증 리포트 생성"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'stats': self.stats,
            'results': results,
            'summary': {
                'total': self.stats['total_files'],
                'valid': self.stats['valid_files'],
                'invalid': self.stats['files_with_issues'],
                'pass_rate': (
                    f"{self.stats['valid_files'] / self.stats['total_files'] * 100:.1f}%"
                    if self.stats['total_files'] > 0 else "N/A"
                )
            }
        }

        # 최종 결과 출력
        self.log("\n" + "="*60)
        self.log("📈 검증 결과", Colors.BOLD + Colors.BLUE)
        self.log("="*60)
        self.log(f"총 파일: {report['stats']['total_files']}")
        self.log(f"통과: {report['stats']['valid_files']} ({report['summary']['pass_rate']})", Colors.GREEN)
        self.log(f"실패: {report['stats']['files_with_issues']}")

        if report['stats']['files_with_issues'] > 0:
            self.log("\n⚠️ 수정이 필요한 파일들:", Colors.YELLOW)
            for result in results:
                if not result['valid']:
                    self.log(f"  - {result['file']}")

        return report


def main():
    """메인 함수"""
    if len(sys.argv) < 2:
        print(f"{Colors.RED}❌ 사용법: python3 validate-wiki.py <wiki_path>{Colors.END}")
        print(f"\n예시: python3 validate-wiki.py ./obsidian-vault")
        sys.exit(1)

    wiki_path = sys.argv[1]

    if not Path(wiki_path).exists():
        print(f"{Colors.RED}❌ 경로가 없음: {wiki_path}{Colors.END}")
        sys.exit(1)

    # 검증 실행
    validator = WikiValidator(wiki_path)
    report = validator.run()

    # JSON 리포트 저장
    report_path = Path(wiki_path) / 'validation_report.json'
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"\n💾 리포트 저장: {report_path}")

    # 종료 코드
    exit_code = 0 if report['stats']['files_with_issues'] == 0 else 1
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
