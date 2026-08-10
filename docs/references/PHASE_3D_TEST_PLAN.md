# 🧪 Phase 3D 테스트 계획 & 실행 가이드

> **Status**: 준비 완료  
> **날짜**: 2026-08-10  
> **목표**: Claude API 자동화 스크립트 검증  

---

## 📋 테스트 개요

### 생성된 3개 스크립트
```
scripts/
├─ extract-actions-from-meetings.py (Step 1: 액션 추출)
├─ merge-actions.py (Step 2: 액션 병합)
└─ generate-action-items-md.py (Step 3: 마크다운 생성)
```

### 테스트 흐름
```
회의 파일들
    ↓ (Step 1: 추출)
extracted_actions.json
    ↓ (Step 2: 병합)
merged_actions.json
    ↓ (Step 3: 생성)
ACTION_ITEMS.md
    ↓ (Step 4: 검증)
기존 ACTION_ITEMS.md와 비교
```

---

## 🚀 실행 전 필수 확인

### 1. 환경 설정 확인
```bash
# API 키 확인
echo $ANTHROPIC_API_KEY

# Python 버전 확인
python3 --version  # 3.7+ 필요

# 필요한 라이브러리 확인
python3 -c "import anthropic; print('✅ anthropic 라이브러리 설치됨')"
```

### 2. 디렉토리 구조 확인
```bash
# 회의 파일 확인
ls -l obsidian-vault/Meetings/2026-*.enhanced.md

# 출력 디렉토리 준비
mkdir -p scripts/output

# ACTION_ITEMS.md 백업
cp obsidian-vault/Actions/ACTION_ITEMS.md ACTION_ITEMS.md.backup
```

---

## 🧪 테스트 단계별 실행

### Step 1️⃣: 액션 추출 테스트

**목표**: 회의 파일에서 액션을 Claude API로 추출

**명령어**:
```bash
python3 scripts/extract-actions-from-meetings.py
```

**옵션**:
```bash
# 특정 파일만 처리 (테스트용)
python3 scripts/extract-actions-from-meetings.py \
  --file obsidian-vault/Meetings/2026-04-16-제품주간회의.enhanced.md \
  --output scripts/output/test_single.json

# 모든 파일 처리
python3 scripts/extract-actions-from-meetings.py \
  --dir obsidian-vault/Meetings \
  --output scripts/output/extracted_actions.json
```

**확인 항목**:
```
[ ] API 호출 성공 (로그 확인)
[ ] JSON 파일 생성됨 (scripts/output/extracted_actions.json)
[ ] JSON 형식 유효 (python3 -m json.tool 확인)
[ ] 액션 개수 합리적 (각 회의마다 3~5개?)
[ ] 담당자 정보 포함됨
[ ] 날짜 형식 YYYY-MM-DD
```

**문제 해결**:
```bash
# 생성된 JSON 확인
cat scripts/output/extracted_actions.json | python3 -m json.tool | head -50

# 액션 개수 확인
python3 -c "
import json
with open('scripts/output/extracted_actions.json') as f:
    data = json.load(f)
    total = sum(len(m.get('actions', [])) for m in data['meetings'])
    print(f'총 {total}개 액션 추출됨')
"
```

---

### Step 2️⃣: 액션 병합 테스트

**목표**: 추출된 액션을 병합하고 중복 제거

**명령어**:
```bash
python3 scripts/merge-actions.py \
  --input scripts/output/extracted_actions.json \
  --output scripts/output/merged_actions.json
```

**옵션**:
```bash
# 유사도 임계값 변경 (기본값: 0.85)
python3 scripts/merge-actions.py \
  --threshold 0.80
```

**확인 항목**:
```
[ ] merged_actions.json 생성됨
[ ] 총 액션 개수 (원본 ~ 14개)
[ ] 상태별 분류 정상 (완료/진행중/보류)
[ ] 담당자별 통계 포함
[ ] 완료율 계산됨
[ ] 중복 제거 로그 확인
```

**검증**:
```bash
# 병합된 JSON 구조 확인
python3 << 'EOF'
import json

with open('scripts/output/merged_actions.json') as f:
    data = json.load(f)
    print(f"총 액션: {data['total_actions']}개")
    print(f"상태별: {data['stats']['by_status']}")
    print(f"담당자별: {data['stats']['by_owner']}")
    print(f"완료율: {data['stats']['completion_rate']}")
EOF
```

---

### Step 3️⃣: 마크다운 생성 테스트

**목표**: 병합된 JSON을 마크다운으로 변환

**명령어**:
```bash
python3 scripts/generate-action-items-md.py \
  --input scripts/output/merged_actions.json \
  --output scripts/output/ACTION_ITEMS_generated.md
```

**옵션**:
```bash
# 기존 파일 대체
python3 scripts/generate-action-items-md.py \
  --output obsidian-vault/Actions/ACTION_ITEMS.md
```

**확인 항목**:
```
[ ] 마크다운 파일 생성됨
[ ] 헤더 포함 (# 📌 액션 아이템 추적)
[ ] 통계 섹션 있음 (요약 테이블)
[ ] 담당자별 통계 있음
[ ] 상태별 액션 그룹핑 정상
[ ] 각 액션 포맷 정상
  [ ] 체크박스 (완료면 [x], 미완료면 [ ])
  [ ] 담당자 포함 ([담당자])
  [ ] 마감일 포함
  [ ] 목표/기준 포함
  [ ] 회의 링크 포함
```

**마크다운 렌더링 확인**:
```bash
# 마크다운 파일 읽기
head -100 scripts/output/ACTION_ITEMS_generated.md

# 링크 검증
grep -o "\[\[.*\]\]" scripts/output/ACTION_ITEMS_generated.md | head -10
```

---

### Step 4️⃣: 기존 데이터와 비교

**목표**: 자동 생성된 데이터와 기존 ACTION_ITEMS.md 비교

**명령어**:
```bash
# 행 수 비교
wc -l obsidian-vault/Actions/ACTION_ITEMS.md scripts/output/ACTION_ITEMS_generated.md

# 내용 비교 (통계 부분)
diff \
  <(grep "^| " obsidian-vault/Actions/ACTION_ITEMS.md | head -5) \
  <(grep "^| " scripts/output/ACTION_ITEMS_generated.md | head -5)

# 액션 개수 비교
echo "기존:" && grep -c "^- \[" obsidian-vault/Actions/ACTION_ITEMS.md
echo "자동:" && grep -c "^- \[" scripts/output/ACTION_ITEMS_generated.md
```

**정성적 평가**:
```
기존 ACTION_ITEMS.md와 비교:

[ ] 액션 개수 일치 (14개)
[ ] 담당자 정보 일치
[ ] 마감일 일치
[ ] 상태 일치
[ ] 구조 일치
[ ] 링크 정상 작동
[ ] 형식 일치
```

---

## 📊 성공 기준

### Phase 3D 완료 조건

| 항목 | 기준 | 상태 |
|------|------|------|
| **Step 1** | 6개 회의 파일 모두 처리 | ⏳ |
| **Step 2** | 중복 제거 후 10~15개 액션 | ⏳ |
| **Step 3** | 마크다운 파일 생성 | ⏳ |
| **Step 4** | 기존 데이터와 90% 이상 일치 | ⏳ |
| **API 호출** | 오류 없음 | ⏳ |
| **링크 검증** | 모든 회의 링크 유효 | ⏳ |

---

## 🔄 전체 파이프라인 한 번에 실행

```bash
#!/bin/bash
# Phase 3D 전체 자동화 스크립트

set -e  # 에러 발생 시 중단

echo "🚀 Phase 3D 자동화 시작"
echo ""

# Step 1: 액션 추출
echo "Step 1️⃣: 액션 추출 중..."
python3 scripts/extract-actions-from-meetings.py

# Step 2: 액션 병합
echo "Step 2️⃣: 액션 병합 중..."
python3 scripts/merge-actions.py

# Step 3: 마크다운 생성
echo "Step 3️⃣: 마크다운 생성 중..."
python3 scripts/generate-action-items-md.py

# Step 4: 기존 데이터와 비교
echo "Step 4️⃣: 기존 데이터와 비교..."
echo ""
echo "기존 ACTION_ITEMS.md:"
grep -c "^- \[" obsidian-vault/Actions/ACTION_ITEMS.md || echo "0"

# 완료
echo ""
echo "✅ Phase 3D 완료!"
echo ""
echo "생성된 파일:"
ls -lh scripts/output/
ls -lh obsidian-vault/Actions/ACTION_ITEMS.md
```

---

## 📝 테스트 체크리스트

### 준비 단계
- [ ] ANTHROPIC_API_KEY 설정됨
- [ ] Python 3.7+ 설치됨
- [ ] anthropic 라이브러리 설치됨
- [ ] 회의 파일 6개 확인됨
- [ ] scripts/output 디렉토리 생성됨
- [ ] ACTION_ITEMS.md 백업 완료

### 실행 단계
- [ ] Step 1 실행 완료
  - [ ] extracted_actions.json 생성됨
  - [ ] API 호출 성공
  - [ ] JSON 형식 유효
- [ ] Step 2 실행 완료
  - [ ] merged_actions.json 생성됨
  - [ ] 중복 제거 정상
  - [ ] 통계 계산 정상
- [ ] Step 3 실행 완료
  - [ ] ACTION_ITEMS_generated.md 생성됨
  - [ ] 마크다운 형식 정상
  - [ ] 링크 유효

### 검증 단계
- [ ] 액션 개수 일치 (14개)
- [ ] 담당자 정보 정확
- [ ] 마감일 정확
- [ ] 상태 정확
- [ ] 링크 정상 작동

---

## 🎯 다음 단계 (성공 시)

1. **검증 완료** → 마크다운 파일 수동 검토
2. **수동 수정** → 필요시 내용 보정
3. **최종 커밋** → Phase 3D 커밋 & 푸시
4. **Phase 3E** → 최종 검증 단계

---

**작성자**: Claude Haiku 4.5  
**작성일**: 2026-08-10  
**상태**: 📋 테스트 계획 완료
