#!/bin/bash

# 📋 Obsidian Vault 문서 마이그레이션 스크립트
# 목표: llm-ssot의 문서들을 obsidian-vault로 복사

echo "🚀 Obsidian Vault 문서 마이그레이션 시작..."
echo ""

# 색상 정의
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# 변수 정의
SOURCE_DIR="./llm-ssot"
VAULT_DIR="./obsidian-vault"

# 디렉토리 확인
if [ ! -d "$SOURCE_DIR" ]; then
    echo -e "${RED}❌ Error: $SOURCE_DIR 디렉토리를 찾을 수 없습니다.${NC}"
    exit 1
fi

if [ ! -d "$VAULT_DIR" ]; then
    echo -e "${RED}❌ Error: $VAULT_DIR 디렉토리를 찾을 수 없습니다.${NC}"
    exit 1
fi

# Step 1: SSOT 문서 복사
echo -e "${BLUE}📁 Step 1: SSOT 문서 마이그레이션${NC}"
echo "소스: $SOURCE_DIR → 대상: $VAULT_DIR/SSOT/"
echo ""

if [ ! -d "$VAULT_DIR/SSOT" ]; then
    mkdir -p "$VAULT_DIR/SSOT"
    echo "✅ SSOT 폴더 생성됨"
fi

# SSOT 메인 파일들 복사
cp "$SOURCE_DIR/SSOT.md" "$VAULT_DIR/SSOT/" 2>/dev/null && echo "✅ SSOT.md 복사됨"
cp "$SOURCE_DIR/model-selection.md" "$VAULT_DIR/SSOT/" 2>/dev/null && echo "✅ model-selection.md 복사됨"
cp "$SOURCE_DIR/prompt-engineering.md" "$VAULT_DIR/SSOT/" 2>/dev/null && echo "✅ prompt-engineering.md 복사됨"
cp "$SOURCE_DIR/GOVERNANCE.md" "$VAULT_DIR/SSOT/" 2>/dev/null && echo "✅ GOVERNANCE.md 복사됨"

echo ""

# Step 2: Meetings 문서 복사
echo -e "${BLUE}📁 Step 2: Meetings 문서 마이그레이션${NC}"
echo "소스: $SOURCE_DIR/Meetings → 대상: $VAULT_DIR/Meetings/"
echo ""

if [ ! -d "$VAULT_DIR/Meetings" ]; then
    mkdir -p "$VAULT_DIR/Meetings"
    echo "✅ Meetings 폴더 생성됨"
fi

# Enhanced 회의록 복사
cp "$SOURCE_DIR/Meetings/"*".enhanced.md" "$VAULT_DIR/Meetings/" 2>/dev/null && echo "✅ Enhanced 회의록 파일들 복사됨"

# 추적 문서 복사
cp "$SOURCE_DIR/Meetings/ACTION_ITEMS.md" "$VAULT_DIR/Meetings/" 2>/dev/null && echo "✅ ACTION_ITEMS.md 복사됨"
cp "$SOURCE_DIR/Meetings/MEETINGS_ANALYSIS.md" "$VAULT_DIR/Meetings/" 2>/dev/null && echo "✅ MEETINGS_ANALYSIS.md 복사됨"

echo ""

# Step 3: Wiki/Decisions 복사
echo -e "${BLUE}📁 Step 3: Wiki/Decisions 문서 마이그레이션${NC}"
echo "소스: $SOURCE_DIR/WIKI → 대상: $VAULT_DIR/Decisions/"
echo ""

if [ ! -d "$VAULT_DIR/Decisions" ]; then
    mkdir -p "$VAULT_DIR/Decisions"
    echo "✅ Decisions 폴더 생성됨"
fi

# Wiki 파일들을 Decisions 폴더로 복사
cp "$SOURCE_DIR/WIKI/DECISIONS.md" "$VAULT_DIR/Decisions/" 2>/dev/null && echo "✅ DECISIONS.md 복사됨"
cp "$SOURCE_DIR/WIKI/WIKI_INDEX.md" "$VAULT_DIR/Decisions/" 2>/dev/null && echo "✅ WIKI_INDEX.md 복사됨"
cp "$SOURCE_DIR/WIKI/TOPICS.md" "$VAULT_DIR/Decisions/" 2>/dev/null && echo "✅ TOPICS.md 복사됨"
cp "$SOURCE_DIR/WIKI/PEOPLE.md" "$VAULT_DIR/Decisions/" 2>/dev/null && echo "✅ PEOPLE.md 복사됨"
cp "$SOURCE_DIR/WIKI/TIMELINE.md" "$VAULT_DIR/Decisions/" 2>/dev/null && echo "✅ TIMELINE.md 복사됨"
cp "$SOURCE_DIR/WIKI/DASHBOARD.md" "$VAULT_DIR/Decisions/" 2>/dev/null && echo "✅ DASHBOARD.md 복사됨"

echo ""

# Step 4: 검증
echo -e "${BLUE}📋 Step 4: 마이그레이션 검증${NC}"
echo ""

echo "SSOT 폴더 내용:"
ls -1 "$VAULT_DIR/SSOT/" 2>/dev/null | wc -l | xargs echo "  파일 수:"

echo ""
echo "Meetings 폴더 내용:"
ls -1 "$VAULT_DIR/Meetings/" 2>/dev/null | wc -l | xargs echo "  파일 수:"

echo ""
echo "Decisions 폴더 내용:"
ls -1 "$VAULT_DIR/Decisions/" 2>/dev/null | wc -l | xargs echo "  파일 수:"

echo ""

# Step 5: 완료 메시지
echo -e "${GREEN}✅ 마이그레이션 완료!${NC}"
echo ""
echo "📊 다음 단계:"
echo "  1. Obsidian에서 Vault 새로고침 (Settings → Reload vault)"
echo "  2. 또는 Obsidian 재시작"
echo "  3. 문서 링크 확인 ([[문서명]])"
echo "  4. Dataview 쿼리 테스트"
echo ""
echo "🎯 준비 완료!"
echo "2026-08-17 첫 회의 준비를 시작할 수 있습니다."
