#!/usr/bin/env python3
"""
추출된 액션 아이템들을 병합, 중복 제거, 정렬하는 스크립트

사용법:
  python3 merge-actions.py
  python3 merge-actions.py --input <JSON파일> --output <출력파일>
"""

import json
import logging
from datetime import datetime
from typing import Dict, List, Set
from pathlib import Path
from difflib import SequenceMatcher


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ActionMerger:
    """추출된 액션들을 병합하고 정렬합니다."""

    def __init__(self, similarity_threshold: float = 0.85):
        """초기화"""
        self.similarity_threshold = similarity_threshold
        logger.info(f"ActionMerger 초기화 (유사도 임계값: {similarity_threshold})")

    def merge(self, input_file: str, output_file: str) -> Dict:
        """JSON 파일 병합"""
        logger.info(f"입력 파일 읽기: {input_file}")

        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # 모든 회의의 액션 수집
        all_actions = []
        for meeting in data.get('meetings', []):
            all_actions.extend(meeting.get('actions', []))

        logger.info(f"총 {len(all_actions)}개 액션 수집")

        # 중복 제거
        unique_actions = self._remove_duplicates(all_actions)
        logger.info(f"중복 제거 후: {len(unique_actions)}개 액션")

        # 상태별 정렬
        actions_by_status = self._sort_by_status(unique_actions)

        # 통계 계산
        stats = self._calculate_stats(unique_actions)

        # 결과 생성
        merged_data = {
            "merged_at": datetime.now().isoformat(),
            "total_actions": len(unique_actions),
            "stats": stats,
            "actions_by_status": actions_by_status,
            "all_actions": unique_actions
        }

        # 파일 저장
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(merged_data, f, ensure_ascii=False, indent=2)

        logger.info(f"✅ 병합 완료: {output_file}")
        logger.info(f"📊 통계: {stats}")

        return merged_data

    def _remove_duplicates(self, actions: List[Dict]) -> List[Dict]:
        """중복 액션 제거"""
        logger.info("중복 액션 제거 중...")

        unique_actions = []
        seen_titles: Set[str] = set()

        for action in actions:
            title = action.get('title', '')

            # 정확한 일치 확인
            if title in seen_titles:
                logger.info(f"  중복 발견 (정확한 일치): {title}")
                continue

            # 유사도 기반 중복 확인
            is_duplicate = False
            for seen_title in seen_titles:
                similarity = self._calculate_similarity(title, seen_title)
                if similarity >= self.similarity_threshold:
                    logger.info(f"  중복 발견 (유사도 {similarity:.2%}): {title}")
                    is_duplicate = True
                    break

            if not is_duplicate:
                unique_actions.append(action)
                seen_titles.add(title)

        return unique_actions

    def _sort_by_status(self, actions: List[Dict]) -> Dict[str, List[Dict]]:
        """상태별로 정렬"""
        logger.info("상태별 정렬 중...")

        status_map = {
            '완료': '✅ 완료',
            '진행중': '⏳ 진행 중',
            '보류': '⏸️ 보류'
        }

        result = {}

        # 상태별로 분류
        for status_key, status_label in status_map.items():
            result[status_label] = []

        # 액션 분류
        for action in actions:
            status = action.get('status', '불명')

            # 상태 정규화
            normalized_status = '✅ 완료' if status == '완료' else \
                               '⏳ 진행 중' if status in ['진행중', '진행 중'] else \
                               '⏸️ 보류' if status == '보류' else \
                               '❓ 불명'

            if normalized_status not in result:
                result[normalized_status] = []

            result[normalized_status].append(action)

        # 각 상태 내에서 마감일 순으로 정렬
        for status in result:
            result[status].sort(
                key=lambda x: x.get('due_date', '9999-12-31')
            )

        return result

    def _calculate_stats(self, actions: List[Dict]) -> Dict:
        """통계 계산"""
        logger.info("통계 계산 중...")

        stats = {
            "total": len(actions),
            "by_status": {},
            "by_owner": {},
            "completion_rate": "0%"
        }

        # 상태별 통계
        status_count = {}
        for action in actions:
            status = action.get('status', '불명')
            status_count[status] = status_count.get(status, 0) + 1

        stats['by_status'] = status_count

        # 담당자별 통계
        owner_count = {}
        for action in actions:
            owner = action.get('owner', '미정')
            owner_count[owner] = owner_count.get(owner, 0) + 1

        stats['by_owner'] = owner_count

        # 완료율
        completed = status_count.get('완료', 0)
        if len(actions) > 0:
            completion_rate = (completed / len(actions)) * 100
            stats['completion_rate'] = f"{completion_rate:.1f}%"

        return stats

    def _calculate_similarity(self, str1: str, str2: str) -> float:
        """두 문자열의 유사도 계산"""
        return SequenceMatcher(None, str1, str2).ratio()


def main():
    """메인 함수"""
    import argparse

    parser = argparse.ArgumentParser(
        description="추출된 액션을 병합하고 정렬합니다"
    )
    parser.add_argument(
        "--input",
        help="입력 JSON 파일",
        default="scripts/output/extracted_actions.json"
    )
    parser.add_argument(
        "--output",
        help="출력 JSON 파일",
        default="scripts/output/merged_actions.json"
    )
    parser.add_argument(
        "--threshold",
        help="중복 판정 유사도 임계값 (0.0 ~ 1.0)",
        type=float,
        default=0.85
    )

    args = parser.parse_args()

    # 입력 파일 확인
    if not Path(args.input).exists():
        logger.error(f"❌ 입력 파일을 찾을 수 없습니다: {args.input}")
        return 1

    try:
        merger = ActionMerger(similarity_threshold=args.threshold)
        result = merger.merge(args.input, args.output)

        logger.info("✅ 병합 완료!")
        logger.info(f"📊 최종 결과:")
        logger.info(f"   - 총 액션: {result['total_actions']}개")
        logger.info(f"   - 상태별: {result['stats']['by_status']}")
        logger.info(f"   - 완료율: {result['stats']['completion_rate']}")

        return 0

    except Exception as e:
        logger.error(f"❌ 오류 발생: {e}")
        return 1


if __name__ == "__main__":
    exit(main())
