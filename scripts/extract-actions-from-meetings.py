#!/usr/bin/env python3
"""
회의 기록 파일에서 액션 아이템을 자동 추출하는 스크립트 (Claude API 사용)

사용법:
  python3 extract-actions-from-meetings.py
  python3 extract-actions-from-meetings.py --file <파일경로>
  python3 extract-actions-from-meetings.py --dir <폴더경로>
"""

import os
import json
import glob
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

import anthropic


# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ActionExtractor:
    """Claude API를 사용하여 회의 기록에서 액션을 추출합니다."""

    def __init__(self, api_key: Optional[str] = None, model: str = "claude-opus-5"):
        """초기화"""
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = model
        logger.info(f"ActionExtractor 초기화 (모델: {self.model})")

    def extract_from_file(self, file_path: str) -> Dict:
        """단일 파일에서 액션 추출"""
        logger.info(f"파일 읽기: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 파일명에서 회의 날짜 추출 (YYYY-MM-DD 형식)
        filename = Path(file_path).stem
        meeting_date = filename.split('-')[0:3]
        meeting_date_str = '-'.join(meeting_date) if len(meeting_date) >= 3 else "불명"
        meeting_title = filename

        logger.info(f"분석 중: {meeting_date_str} - {meeting_title}")

        # Claude API 호출
        prompt = self._create_prompt(content, meeting_title, meeting_date_str)
        response = self.client.messages.create(
            model=self.model,
            max_tokens=4096,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        # 응답 파싱
        response_text = response.content[0].text
        logger.info(f"API 응답 수신 (길이: {len(response_text)}자)")

        # JSON 추출 (응답에서 JSON 부분만 추출)
        try:
            json_start = response_text.find('{')
            json_end = response_text.rfind('}') + 1
            if json_start >= 0 and json_end > json_start:
                json_str = response_text[json_start:json_end]
                result = json.loads(json_str)
                logger.info(f"추출 완료: {len(result.get('actions', []))}개 액션")
                return result
            else:
                logger.warning("JSON 응답을 찾을 수 없음")
                return self._create_empty_result(meeting_date_str, meeting_title)
        except json.JSONDecodeError as e:
            logger.error(f"JSON 파싱 실패: {e}")
            return self._create_empty_result(meeting_date_str, meeting_title)

    def extract_from_directory(self, directory: str) -> List[Dict]:
        """디렉토리의 모든 회의 파일에서 액션 추출"""
        logger.info(f"디렉토리 분석: {directory}")

        # 모든 .enhanced.md 파일 찾기
        files = sorted(glob.glob(os.path.join(directory, "*-*.enhanced.md")))
        logger.info(f"발견된 파일: {len(files)}개")

        results = []
        for file_path in files:
            try:
                result = self.extract_from_file(file_path)
                results.append(result)
            except Exception as e:
                logger.error(f"파일 처리 실패 ({file_path}): {e}")
                continue

        logger.info(f"디렉토리 분석 완료: {len(results)}개 파일 처리")
        return results

    def _create_prompt(self, content: str, title: str, date: str) -> str:
        """API 호출용 프롬프트 생성"""
        return f"""당신은 회의 기록 분석 전문가입니다.

다음 회의 기록에서 액션 아이템을 추출해주세요:

회의명: {title}
회의일: {date}

내용:
---
{content[:3000]}  # 처음 3000자만 (토큰 절약)
---

다음 JSON 형식으로 반환해주세요:
{{
  "meeting_date": "YYYY-MM-DD",
  "meeting_title": "회의명",
  "actions": [
    {{
      "title": "액션 제목",
      "owner": "담당자명",
      "status": "완료|진행중|보류",
      "due_date": "YYYY-MM-DD",
      "goal": "목표 설명",
      "criteria": "성공 기준",
      "related_meeting": "관련 회의 파일명"
    }}
  ]
}}

주의사항:
- 각 액션은 구체적이고 측정 가능해야 함
- 담당자는 사람 이름 또는 팀명
- 상태는 반드시 "완료|진행중|보류" 중 하나
- 날짜는 YYYY-MM-DD 형식 (불명확하면 "불명")
- 불명확한 정보는 "불명" 표시
- 중복되는 액션은 1개만 추출
"""

    def _create_empty_result(self, date: str, title: str) -> Dict:
        """빈 결과 생성"""
        return {
            "meeting_date": date,
            "meeting_title": title,
            "actions": [],
            "error": "처리 실패"
        }


def main():
    """메인 함수"""
    import argparse

    parser = argparse.ArgumentParser(
        description="회의 기록에서 액션 아이템을 자동 추출합니다"
    )
    parser.add_argument(
        "--file",
        help="단일 파일 경로",
        default=None
    )
    parser.add_argument(
        "--dir",
        help="디렉토리 경로",
        default="obsidian-vault/Meetings"
    )
    parser.add_argument(
        "--output",
        help="출력 파일 경로",
        default="scripts/output/extracted_actions.json"
    )
    parser.add_argument(
        "--model",
        help="Claude 모델",
        default="claude-opus-5"
    )

    args = parser.parse_args()

    # 출력 디렉토리 생성
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        logger.info(f"출력 디렉토리 생성: {output_dir}")

    # API 키 확인
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        logger.error("❌ ANTHROPIC_API_KEY 환경변수가 설정되지 않았습니다")
        return 1

    try:
        extractor = ActionExtractor(api_key=api_key, model=args.model)

        # 파일 또는 디렉토리 처리
        if args.file:
            logger.info(f"단일 파일 모드: {args.file}")
            results = [extractor.extract_from_file(args.file)]
        else:
            logger.info(f"디렉토리 모드: {args.dir}")
            results = extractor.extract_from_directory(args.dir)

        # 결과 저장
        output_data = {
            "extracted_at": datetime.now().isoformat(),
            "total_meetings": len(results),
            "total_actions": sum(len(r.get("actions", [])) for r in results),
            "meetings": results
        }

        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)

        logger.info(f"✅ 결과 저장: {args.output}")
        logger.info(f"📊 요약: {output_data['total_meetings']}개 회의, {output_data['total_actions']}개 액션")

        return 0

    except Exception as e:
        logger.error(f"❌ 오류 발생: {e}")
        return 1


if __name__ == "__main__":
    exit(main())
