# 🚀 Claude API 실행 가이드

> meeting-processor.py를 실행하는 단계별 가이드

---

## 📋 사전 준비

```bash
# ✅ 확인 사항:
- [ ] ANTHROPIC_API_KEY 환경변수 설정됨
- [ ] Python 3.7+ 설치됨
- [ ] anthropic 라이브러리 설치됨
```

**라이브러리 설치:**
```bash
pip3 install anthropic
```

---

## 🎯 실행 방법

### 방법 1️⃣: 기존 회의록으로 테스트

```bash
# 터미널 열기
cd /Users/mac/work/claude/20260810_harness

# 스크립트 실행
python3 scripts/meeting-processor.py \
  ./obsidian-vault/Meetings/2026-05-14-제품주간회의.enhanced.md
```

### 방법 2️⃣: 다른 회의록 선택

```bash
# 이용 가능한 회의록 확인
ls obsidian-vault/Meetings/*.enhanced.md

# 선택한 회의록으로 실행
python3 scripts/meeting-processor.py \
  ./obsidian-vault/Meetings/[파일명].enhanced.md
```

### 방법 3️⃣: 변수로 실행

```bash
# 회의 파일을 변수로 설정
MEETING_FILE="./obsidian-vault/Meetings/2026-05-14-제품주간회의.enhanced.md"

# 스크립트 실행
python3 scripts/meeting-processor.py "$MEETING_FILE"
```

---

## 📊 실행 결과

### 터미널 출력

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
  이 회의에서는 PG사 선정, 온보딩 개선, 
  정산 주기 등 3가지 주요 항목을 논의했습니다.
  A/B 테스트 진행 및 외부 협력사와의 
  협의 결과를 공유했습니다.

📌 액션 아이템 (5개):
  • 🔴 [[담당자명]] - PG사 계약 진행 (마감: 2026-08-20)
  • 🟡 [[담당자명]] - 온보딩 페이지 개선 (마감: 2026-08-25)
  • 🟢 [[담당자명]] - 정산 주기 검토 (마감: 2026-09-01)

✅ 의사결정 (2개):
  • PG사 A사 선정 (근거: 기술 스택, 가격 경쟁력)
  • 온보딩 A/B 테스트 연장 2주 (근거: 데이터 신뢰도)

🔗 SSOT 영향:
  • SSOT 규칙 1: PG사 정책 업데이트 필요
  • SSOT 규칙 3: 결제 연동 일정 확정

============================================================
✅ 분석 완료! 결과는 JSON 파일로 저장되었습니다.
```

### 생성된 파일

```
obsidian-vault/Meetings/
├── analysis_20260810_141530.json    ← 분석 결과
├── ACTION_ITEMS.md                  ← 자동 갱신됨
└── [회의록].enhanced.md
```

---

## ✅ 결과 검증

### 1️⃣ JSON 파일 확인

```bash
# 생성된 파일 확인
ls -lh obsidian-vault/Meetings/analysis_*.json

# 최신 파일 열기
cat obsidian-vault/Meetings/analysis_*.json | jq '.'
```

**예상 내용:**
```json
{
  "summary": "회의 요약 (3-5문장)",
  "actions": [
    {
      "item": "작업 내용",
      "owner": "담당자",
      "due_date": "2026-MM-DD",
      "priority": "높음"
    }
  ],
  "decisions": [
    {
      "decision": "결정 내용",
      "reason": "근거",
      "owner": "담당자"
    }
  ],
  "ssot_impact": ["영향도 항목"]
}
```

### 2️⃣ ACTION_ITEMS.md 확인

```bash
# ACTION_ITEMS.md 마지막 부분 확인
tail -100 obsidian-vault/Meetings/ACTION_ITEMS.md
```

**예상 내용:**
```markdown
---

## 🔄 2026-08-10 14:15 추가

## 📌 액션 아이템

- [ ] 🔴 [[담당자]] - 작업 1 (마감: 2026-MM-DD)
- [ ] 🟡 [[담당자]] - 작업 2 (마감: 2026-MM-DD)
- [ ] 🟢 [[담당자]] - 작업 3 (마감: 2026-MM-DD)
```

### 3️⃣ QUERIES.md에서 확인

```bash
# Obsidian에서 QUERIES.md 열기
# → 쿼리 1 (진행 중인 액션) 확인
# → 새로 추가된 액션이 나타나는지 확인
```

---

## 🔄 배치 처리 (모든 회의록)

### 한 번에 여러 회의록 처리

```bash
#!/bin/bash

# 모든 회의록 처리
for file in ./obsidian-vault/Meetings/*.enhanced.md; do
  echo "=========================================="
  echo "처리 중: $(basename "$file")"
  echo "=========================================="
  python3 scripts/meeting-processor.py "$file"
  echo ""
  sleep 2  # 2초 대기 (API 제한 방지)
done

echo "✅ 모든 회의록 처리 완료!"
```

**저장 방법:**
```bash
# 파일 생성
cat > run_all_meetings.sh << 'EOF'
[위의 배치 스크립트 내용]
EOF

# 실행 권한 설정
chmod +x run_all_meetings.sh

# 실행
./run_all_meetings.sh
```

---

## 🧪 테스트 단계별

### Stage 1: API 키 확인

```bash
# API 키 설정 확인
echo $ANTHROPIC_API_KEY

# 출력:
# sk-ant-v0-abc123...
```

### Stage 2: 스크립트 실행

```bash
# 가장 작은 회의록으로 테스트
python3 scripts/meeting-processor.py \
  ./obsidian-vault/Meetings/2026-05-14-제품주간회의.enhanced.md
```

### Stage 3: 결과 파일 확인

```bash
# JSON 파일 생성 확인
ls -la obsidian-vault/Meetings/analysis_*.json

# 파일 크기 확인 (0 바이트 아님)
du -h obsidian-vault/Meetings/analysis_*.json
```

### Stage 4: ACTION_ITEMS.md 갱신 확인

```bash
# 파일 수정 시간 확인
stat obsidian-vault/Meetings/ACTION_ITEMS.md | grep Modify

# 파일 내용 확인
wc -l obsidian-vault/Meetings/ACTION_ITEMS.md
```

### Stage 5: Obsidian 대시보드 확인

```
Obsidian에서:
1. Meetings/ACTION_ITEMS.md 열기
2. 새 액션이 추가되었는지 확인
3. QUERIES.md의 쿼리 1 확인
4. 새 액션이 테이블에 표시되는지 확인
```

---

## 🎯 성공 기준

| 항목 | 기준 | 확인 |
|------|------|------|
| **JSON 파일** | analysis_*.json 생성됨 | ls 명령 |
| **액션 추출** | 3개 이상 추출 | cat analysis_*.json \| jq '.actions' |
| **액션 추가** | ACTION_ITEMS.md 자동 갱신 | tail 명령 |
| **요약 생성** | 3-5문장 생성 | cat analysis_*.json \| jq '.summary' |
| **결정 분석** | 1개 이상 분석 | cat analysis_*.json \| jq '.decisions' |
| **대시보드** | QUERIES.md에 반영 | Obsidian 확인 |

---

## ⚠️ 문제 해결

### ❌ "No module named 'anthropic'"

```bash
# 라이브러리 설치
pip3 install anthropic

# 또는
pip install anthropic

# 재시도
python3 scripts/meeting-processor.py <파일>
```

### ❌ "ANTHROPIC_API_KEY 환경변수가 설정되지 않음"

```bash
# 환경변수 설정
export ANTHROPIC_API_KEY="sk-ant-..."

# 확인
echo $ANTHROPIC_API_KEY

# 재시도
python3 scripts/meeting-processor.py <파일>
```

### ❌ "AuthenticationError: Incorrect API key"

```bash
# 1. API 콘솔에서 키 확인
# https://console.anthropic.com/account/keys

# 2. 정확히 복사해서 설정
export ANTHROPIC_API_KEY="sk-ant-정확한-키"

# 3. 확인
echo $ANTHROPIC_API_KEY

# 4. 재시도
python3 scripts/meeting-processor.py <파일>
```

### ❌ "RateLimitError"

```bash
# 1. 인터넷 연결 확인
ping google.com

# 2. 2-3분 대기

# 3. 재시도
python3 scripts/meeting-processor.py <파일>
```

---

## 📋 체크리스트

```
실행 전:
[ ] ANTHROPIC_API_KEY 설정됨
[ ] anthropic 라이브러리 설치됨
[ ] 회의 파일 확인됨

실행:
[ ] python3 scripts/meeting-processor.py <파일> 실행
[ ] 터미널에 "✅ 분석 완료" 메시지 보임

결과 확인:
[ ] analysis_*.json 파일 생성됨
[ ] JSON 내용이 유효함
[ ] ACTION_ITEMS.md 자동 갱신됨
[ ] QUERIES.md에 새 액션 표시됨

완료:
[ ] 모든 단계 완료
[ ] Phase 3D 커밋 준비
```

---

## 🚀 다음 단계

### Phase 3D 완료 후 (Day 6):

1. ✅ API 설정 및 테스트 완료
2. ✅ meeting-processor.py 성공 실행
3. ✅ JSON 결과 생성 확인
4. ✅ ACTION_ITEMS.md 자동 갱신 확인

### Phase 3E (Day 7):

```
최종 검증:
[ ] Obsidian 모든 기능 작동
[ ] QUERIES.md 쿼리 렌더링
[ ] Claude API 분석 정상
[ ] 링크 모두 작동
[ ] 자동화 스크립트 모두 정상
```

### Phase 3F (Day 8):

```
첫 회의 테스트:
[ ] 회의 템플릿 생성
[ ] 실시간 기록
[ ] Claude 자동 분석
[ ] 대시보드 갱신
[ ] 모든 기능 검증 ✅
```

---

**마지막 업데이트**: 2026-08-14  
**버전**: 1.0  
**상태**: ✅ 준비 완료

🎯 **이제 실행할 준비가 되었습니다!**
