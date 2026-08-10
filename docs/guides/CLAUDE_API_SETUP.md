# 🤖 Claude API 설정 가이드

> meeting-processor.py를 위한 Claude API 환경 설정

---

## 📋 필요한 것

- Claude API 키 (Anthropic 계정)
- Python 3.7+
- scripts/meeting-processor.py 파일

---

## 🔑 Step 1: Claude API 키 획득

### 1-1. Anthropic 콘솔 접속

```
https://console.anthropic.com/account/keys
```

### 1-2. 새 API 키 생성

1. "Create Key" 버튼 클릭
2. 키 이름 입력 (예: "meeting-processor")
3. "Create Key" 클릭
4. 생성된 키 복사 (⚠️ 한 번만 표시됨!)

```
sk-ant-v0-... (이런 형태)
```

---

## ⚙️ Step 2: 환경변수 설정

### 2-1. macOS/Linux - .zshrc 또는 .bash_profile 편집

```bash
# 에디터로 파일 열기
nano ~/.zshrc
# 또는
nano ~/.bash_profile
```

### 2-2. 파일 끝에 추가

```bash
# Claude API Key
export ANTHROPIC_API_KEY="sk-ant-v0-..."
```

**완전한 예시:**
```bash
# === Claude API ===
export ANTHROPIC_API_KEY="sk-ant-v0-abc123def456ghi789..."
```

### 2-3. 저장 & 적용

```bash
# Ctrl + X → Y → Enter (nano 에디터)

# 또는 터미널에 직접 입력
source ~/.zshrc
# 또는
source ~/.bash_profile
```

### 2-4. 확인

```bash
# API 키가 설정되었는지 확인
echo $ANTHROPIC_API_KEY

# 출력 예:
# sk-ant-v0-abc123def456ghi789...
```

✅ **API 키가 출력되면 성공!**

---

## 🧪 Step 3: 실행 테스트

### 3-1. 터미널 열기

```bash
cd /Users/mac/work/claude/20260810_harness
```

### 3-2. 스크립트 실행

```bash
# 기존 회의록으로 테스트
python3 scripts/meeting-processor.py \
  ./obsidian-vault/Meetings/2026-05-14-제품주간회의.enhanced.md
```

### 3-3. 예상 결과

```
🤖 회의 자동화 시스템 (Claude API)
============================================================

✅ 회의 노트 읽음: 2026-05-14-제품주간회의.enhanced.md

🤖 Claude로 분석 중...

✅ Claude 분석 완료

============================================================
📊 회의 분석 결과
============================================================

📝 요약:
  [3-5문장 요약]

📌 액션 아이템 (N개):
  • 🔴 [작업 내용]
    담당: [[담당자]], 마감: 2026-MM-DD

✅ 의사결정 (N개):
  • [결정 내용]
    담당: [[담당자]]

🔗 SSOT 영향:
  • [영향도 분석]

============================================================
✅ 분석 완료! 결과는 JSON 파일로 저장되었습니다.
```

---

## 📂 Step 4: 결과 확인

### 4-1. 생성된 파일

```bash
# 분석 결과 JSON
ls -la obsidian-vault/Meetings/analysis_*.json

# 예상 위치:
# obsidian-vault/Meetings/analysis_20260810_141530.json
```

### 4-2. 결과 내용 확인

```bash
# JSON 파일 보기
cat obsidian-vault/Meetings/analysis_*.json

# 예상 출력:
# {
#   "summary": "...",
#   "actions": [...],
#   "decisions": [...],
#   "ssot_impact": [...]
# }
```

### 4-3. ACTION_ITEMS.md 갱신 확인

```bash
# ACTION_ITEMS.md 마지막 부분 확인
tail -50 obsidian-vault/Meetings/ACTION_ITEMS.md

# 새로운 액션이 추가되어야 함:
# ## 🔄 [타임스탐프] 추가
# 
# ## 📌 액션 아이템
# - [ ] 🔴 [작업 1] - [[담당자]] - (마감: YYYY-MM-DD)
```

---

## 🔧 문제 해결

### ❌ "API 키가 설정되지 않음" 오류

**원인**: ANTHROPIC_API_KEY 환경변수 미설정

**해결**:
```bash
# 1. API 키 설정 재확인
echo $ANTHROPIC_API_KEY

# 2. 비어있으면 다시 설정
export ANTHROPIC_API_KEY="sk-ant-..."

# 3. 확인
echo $ANTHROPIC_API_KEY
```

### ❌ "AuthenticationError: Incorrect API key"

**원인**: API 키 복사 오류 또는 유효하지 않은 키

**해결**:
```bash
# 1. API 콘솔에서 키 재확인
# https://console.anthropic.com/account/keys

# 2. 새 키 생성
# 기존 키는 삭제 후 새로 생성

# 3. 환경변수에 정확히 입력
export ANTHROPIC_API_KEY="sk-ant-..."
```

### ❌ "RateLimitError" 또는 "APIConnectionError"

**원인**: API 사용량 초과 또는 네트워크 오류

**해결**:
```bash
# 1. 인터넷 연결 확인
ping google.com

# 2. 잠시 기다린 후 재시도
# 2-3분 후 다시 실행

# 3. API 사용량 확인
# https://console.anthropic.com/account/billing/overview

# 4. 더 작은 파일로 테스트
```

### ❌ "ModuleNotFoundError: No module named 'anthropic'"

**원인**: anthropic 라이브러리 미설치

**해결**:
```bash
# anthropic 라이브러리 설치
pip3 install anthropic

# 또는
pip install anthropic

# 설치 후 재시도
python3 scripts/meeting-processor.py <파일>
```

---

## 📊 Step 5: 실제 회의록으로 테스트

### 5-1. 새 회의록으로 실행

```bash
# Obsidian에서 새 회의록 생성
# 또는 기존 회의록 사용

python3 scripts/meeting-processor.py \
  ./obsidian-vault/Meetings/[새회의명].enhanced.md
```

### 5-2. 결과 검증

| 항목 | 확인 사항 |
|------|----------|
| **요약** | 3-5문장 생성됨 |
| **액션** | 담당자, 마감일, 우선순위 포함 |
| **결정** | 결정 내용, 근거, 담당자 포함 |
| **JSON** | analysis_*.json 파일 생성됨 |
| **ACTION_ITEMS** | 새 액션이 자동 추가됨 |

---

## ✅ 체크리스트

```
설정 전:
[ ] Anthropic 콘솔 접속 가능
[ ] API 키 생성됨 (sk-ant-...)
[ ] Python 3.7+ 설치됨

설정 중:
[ ] .zshrc/.bash_profile 편집
[ ] ANTHROPIC_API_KEY 환경변수 추가
[ ] source 명령어로 적용

검증:
[ ] echo $ANTHROPIC_API_KEY 확인
[ ] anthropic 라이브러리 설치됨
[ ] meeting-processor.py 문법 OK

테스트:
[ ] 기존 회의록으로 테스트 실행
[ ] JSON 결과 파일 생성됨
[ ] ACTION_ITEMS.md 갱신됨
[ ] 새 회의록으로 재테스트

완료:
[ ] Phase 3D 커밋 & 푸시
[ ] Phase 3E 준비 (최종 검증)
```

---

## 📞 다음 단계

### Day 6 완료 후:

1. ✅ API 키 설정 완료
2. ✅ meeting-processor.py 테스트 완료
3. ✅ JSON 결과 생성 확인
4. ✅ ACTION_ITEMS.md 자동 갱신 확인

### Day 7 진행 (최종 검증):

```bash
# 전체 시스템 점검
# - Obsidian 모든 기능 작동
# - QUERIES.md 쿼리 렌더링
# - Claude API 분석 정상
# - 링크 모두 작동
# - 자동화 스크립트 모두 정상
```

### Day 8 (첫 회의 테스트):

```bash
# 실제 회의에서 자동화 시스템 테스트
# - 회의 템플릿 생성
# - 실시간 기록
# - Claude 자동 분석
# - 대시보드 갱신
# - 모든 기능 검증
```

---

## 🔐 보안 주의

⚠️ **중요:**

```bash
❌ API 키를 코드에 하드코딩하지 마세요
❌ API 키를 GitHub에 푸시하지 마세요
❌ API 키를 다른 사람과 공유하지 마세요

✅ 환경변수로만 관리하세요
✅ .env 파일은 .gitignore에 포함하세요
✅ 노출된 키는 즉시 생성 취소하세요
```

---

## 💡 팁

### 자동 설정 (한 번에)

```bash
# 터미널에서 직접
export ANTHROPIC_API_KEY="sk-ant-..." && \
python3 scripts/meeting-processor.py ./obsidian-vault/Meetings/2026-05-14-제품주간회의.enhanced.md
```

### 반복 테스트

```bash
# 배치 실행
for file in obsidian-vault/Meetings/*.enhanced.md; do
  echo "처리: $file"
  python3 scripts/meeting-processor.py "$file"
done
```

### 결과 분석

```bash
# 모든 분석 결과 보기
ls -la obsidian-vault/Meetings/analysis_*.json

# 최신 결과만 보기
ls -t obsidian-vault/Meetings/analysis_*.json | head -1 | xargs cat
```

---

**마지막 업데이트**: 2026-08-14  
**버전**: 1.0  
**상태**: ✅ 준비 완료

🚀 **이제 Phase 3D를 진행할 준비가 되었습니다!**
