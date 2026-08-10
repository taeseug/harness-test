#!/bin/bash

# 🤖 회의 배치 분석 스크립트
# 모든 회의를 자동으로 분석하고 ACTION_ITEMS.md에 누적

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MEETINGS_DIR="$PROJECT_ROOT/obsidian-vault/Meetings"
SCRIPT_PATH="$PROJECT_ROOT/.claude/skills/obsidian-meeting-analyzer/scripts/analyze_meeting.py"

# 색상 정의
RED='\033[91m'
GREEN='\033[92m'
YELLOW='\033[93m'
BLUE='\033[94m'
CYAN='\033[96m'
BOLD='\033[1m'
END='\033[0m'

echo -e "${BOLD}${BLUE}========================================${END}"
echo -e "${BOLD}${BLUE}🤖 회의 배치 분석 시작${END}"
echo -e "${BOLD}${BLUE}========================================${END}\n"

# API 키 확인
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo -e "${RED}❌ ANTHROPIC_API_KEY 환경변수가 설정되지 않았습니다${END}"
    echo -e "${YELLOW}💡 다음 명령어로 설정하세요:${END}"
    echo -e "${CYAN}export ANTHROPIC_API_KEY=\"sk-ant-...\"${END}"
    exit 1
fi

echo -e "${GREEN}✅ API 키 확인 완료${END}"
echo ""

# 분석할 회의 파일 찾기 (템플릿 제외)
MEETING_FILES=$(find "$MEETINGS_DIR" -name "*.enhanced.md" ! -name "_*" | sort)

if [ -z "$MEETING_FILES" ]; then
    echo -e "${RED}❌ 회의 파일을 찾을 수 없습니다${END}"
    exit 1
fi

# 파일 개수 세기
FILE_COUNT=$(echo "$MEETING_FILES" | wc -l)
echo -e "${CYAN}📋 분석할 회의: $FILE_COUNT 개${END}\n"

# 분석 통계
SUCCESS_COUNT=0
FAIL_COUNT=0

# 각 회의 파일 분석
for file in $MEETING_FILES; do
    filename=$(basename "$file")
    echo -e "${BOLD}${CYAN}─────────────────────────────────────${END}"
    echo -e "${CYAN}📄 처리 중: $filename${END}"
    echo -e "${BOLD}${CYAN}─────────────────────────────────────${END}"

    if python "$SCRIPT_PATH" "$file" "$PROJECT_ROOT/obsidian-vault"; then
        echo -e "${GREEN}✅ 완료: $filename${END}\n"
        ((SUCCESS_COUNT++))
    else
        echo -e "${RED}❌ 실패: $filename${END}\n"
        ((FAIL_COUNT++))
    fi

    # API 속도 제한 방지
    sleep 2
done

# 최종 결과
echo -e "${BOLD}${BLUE}========================================${END}"
echo -e "${BOLD}${BLUE}📊 배치 분석 완료${END}"
echo -e "${BOLD}${BLUE}========================================${END}\n"

echo -e "${GREEN}✅ 성공: $SUCCESS_COUNT 개${END}"
if [ $FAIL_COUNT -gt 0 ]; then
    echo -e "${RED}❌ 실패: $FAIL_COUNT 개${END}"
fi

# 분석 결과 파일 확인
ANALYSIS_COUNT=$(find "$MEETINGS_DIR" -name "analysis_*.json" | wc -l)
echo -e "${CYAN}📁 생성된 분석 파일: $ANALYSIS_COUNT 개${END}\n"

# ACTION_ITEMS.md 확인
if [ -f "$MEETINGS_DIR/ACTION_ITEMS.md" ]; then
    echo -e "${CYAN}📌 ACTION_ITEMS.md 크기:${END}"
    ls -lh "$MEETINGS_DIR/ACTION_ITEMS.md" | awk '{print "   " $5}'
    echo ""
fi

# 분석 결과 미리보기
echo -e "${BOLD}${CYAN}최신 분석 결과:${END}"
LATEST_ANALYSIS=$(ls -t "$MEETINGS_DIR"/analysis_*.json 2>/dev/null | head -1)
if [ -n "$LATEST_ANALYSIS" ]; then
    echo -e "${CYAN}파일: $(basename "$LATEST_ANALYSIS")${END}"
    python -m json.tool "$LATEST_ANALYSIS" 2>/dev/null | head -20
    echo "..."
else
    echo -e "${YELLOW}분석 결과 파일을 찾을 수 없습니다${END}"
fi

echo ""
echo -e "${GREEN}🎉 배치 분석 완료!${END}"
echo -e "${CYAN}다음 단계:${END}"
echo -e "  1. git add obsidian-vault/Meetings/"
echo -e "  2. git commit -m 'feat: 회의 자동 분석 결과 추가'"
echo -e "  3. git push origin main"
