# 📋 Obsidian 회의 분석 시스템 설정 가이드

## 1️⃣ 사전 요구사항

### 시스템 요구사항
- **Python**: 3.7 이상
- **OS**: macOS, Linux, Windows
- **메모리**: 최소 512MB

### 의존성 설치

```bash
# Anthropic API 클라이언트 설치
pip install anthropic

# 또는 requirements.txt 있으면
pip install -r requirements.txt
```

### Claude API 키 설정

1. [Anthropic Console](https://console.anthropic.com)에서 API 키 생성
2. 환경변수로 설정:

**macOS/Linux:**
```bash
export ANTHROPIC_API_KEY="sk-ant-..."

# 영구 설정 (optional)
echo 'export ANTHROPIC_API_KEY="sk-ant-..."' >> ~/.zshrc
source ~/.zshrc
```

**Windows (PowerShell):**
```powershell
$env:ANTHROPIC_API_KEY="sk-ant-..."

# 영구 설정: 시스템 환경변수 → ANTHROPIC_API_KEY 추가
```

3. 설정 확인:
```bash
echo $ANTHROPIC_API_KEY
# 출력: sk-ant-v0-...
```

---

## 2️⃣ Obsidian Vault 구조 설정

### 필수 폴더 구조

```
your-project/
├── obsidian-vault/
│   ├── Meetings/
│   │   ├── README.md              # 설명
│   │   ├── ACTION_ITEMS.md        # 액션 아이템 (자동 갱신)
│   │   ├── [회의파일].md          # 회의 기록
│   │   └── analysis_*.json        # 분석 결과 (자동 생성)
│   │
│   ├── SSOT/                      # (선택) SSOT 문서
│   ├── Decisions/                 # (선택) 결정사항
│   ├── Daily/                     # (선택) 일일 노트
│   ├── Templates/                 # (선택) 템플릿
│   │   └── meeting-new.md
│   └── .obsidian/                 # Obsidian 설정
│
├── scripts/
│   └── analyze_meeting.py         # 이 스킬의 스크립트
│
└── README.md
```

### Meetings 폴더 초기화

#### 1. 폴더 생성
```bash
mkdir -p obsidian-vault/Meetings
```

#### 2. ACTION_ITEMS.md 생성
```bash
cat > obsidian-vault/Meetings/ACTION_ITEMS.md << 'EOF'
# 📌 액션 아이템

현재 진행 중인 모든 액션을 추적합니다.

## 진행 중 (⏳)
- [ ] 샘플 액션 1
- [ ] 샘플 액션 2

## 완료 (✅)
- [x] 샘플 완료 액션

---

(이 구분선 아래에 새로운 액션이 자동으로 추가됩니다)
EOF
```

---

## 3️⃣ 스크립트 설치

### 방법 1: 직접 복사

```bash
# 프로젝트 루트에서
mkdir -p scripts
cp analyze_meeting.py scripts/

# 실행 권한 설정
chmod +x scripts/analyze_meeting.py
```

### 방법 2: 심볼릭 링크

```bash
ln -s /path/to/analyze_meeting.py scripts/analyze_meeting.py
```

---

## 4️⃣ 첫 실행 테스트

### 테스트용 회의 파일 생성

```bash
cat > obsidian-vault/Meetings/2026-08-17-test-meeting.md << 'EOF'
---
date: 2026-08-17
type: meeting
participants: [담당자1, 담당자2]
---

# 📋 테스트 회의록 - 2026-08-17

## 📌 안건
- 시스템 초기화 테스트
- 기능 검증

## 💬 주요 논의 사항

### 항목 1
팀원들과 새로운 시스템 구축 방안 논의

### 항목 2
액션 아이템 및 의사결정 절차 확인

## ✅ 의사결정

| 항목 | 결정 | 담당자 |
|-----|------|--------|
| 분석 도구 | Claude API 사용 | 담당자1 |

## 🎯 액션 아이템

- [ ] 시스템 배포 (담당: 담당자1, 마감: 2026-08-20)
- [ ] 팀 교육 (담당: 담당자2, 마감: 2026-08-25)
- [ ] 성과 측정 (담당: 담당자1, 마감: 2026-09-01)
EOF
```

### 스크립트 실행

```bash
python scripts/analyze_meeting.py ./obsidian-vault/Meetings/2026-08-17-test-meeting.md
```

### 결과 확인

```bash
# 1. JSON 파일 확인
ls -lh obsidian-vault/Meetings/analysis_*.json

# 2. 최신 파일 내용 확인
cat obsidian-vault/Meetings/analysis_*.json | python -m json.tool

# 3. ACTION_ITEMS.md 갱신 확인
tail -30 obsidian-vault/Meetings/ACTION_ITEMS.md
```

---

## 5️⃣ Obsidian 플러그인 설정 (선택)

### 권장 플러그인

#### 1. Dataview
회의 기록을 동적으로 쿼리하고 대시보드 생성

```javascript
// Obsidian의 QUERIES.md에 다음 쿼리 추가
```dataview
TABLE status, owner, due_date
FROM "Meetings"
WHERE status = "⏳"
SORT due_date ASC
```
```

#### 2. Periodic Notes
Daily/Weekly 노트 자동 생성

설정:
- Daily notes folder: `Daily/`
- Template: `Templates/daily.md`

#### 3. Templater
회의 템플릿 자동화

```markdown
<!-- Templates/meeting-new.md -->
---
date: <% tp.date.now("YYYY-MM-DD") %>
time: <% tp.date.now("HH:mm") %>
type: meeting
---

# 📋 회의록 - <% tp.date.now("YYYY-MM-DD") %>

## 📌 안건

## 💬 주요 논의 사항

## ✅ 의사결정

## 🎯 액션 아이템
```

---

## 6️⃣ 자동화 스크립트 (Optional)

모든 회의를 배치 처리하는 스크립트:

```bash
#!/bin/bash
# batch-analyze.sh

echo "🤖 모든 회의 분석 시작..."

for file in obsidian-vault/Meetings/*.md; do
  # ACTION_ITEMS.md와 분석 결과 파일 제외
  if [[ "$file" == *"ACTION_ITEMS"* ]] || [[ "$file" == *"analysis_"* ]]; then
    continue
  fi

  echo "처리 중: $(basename "$file")"
  python scripts/analyze_meeting.py "$file"
  sleep 2  # API 속도 제한 방지
done

echo "✅ 배치 처리 완료!"
```

사용:
```bash
chmod +x batch-analyze.sh
./batch-analyze.sh
```

---

## 7️⃣ 문제 해결

### "ANTHROPIC_API_KEY 환경변수가 설정되지 않았습니다"

```bash
# 1. API 키 확인
echo $ANTHROPIC_API_KEY

# 2. 키가 없으면 설정
export ANTHROPIC_API_KEY="sk-ant-..."

# 3. 다시 시도
python scripts/analyze_meeting.py ./obsidian-vault/Meetings/test.md
```

### "파일을 찾을 수 없음"

```bash
# 1. 파일 경로 확인
ls -la obsidian-vault/Meetings/

# 2. 절대 경로 사용
python scripts/analyze_meeting.py /Users/yourname/project/obsidian-vault/Meetings/test.md
```

### "JSON 파싱 실패"

Claude의 응답이 유효하지 않을 수 있습니다.

```bash
# 1. 로그 확인
python scripts/analyze_meeting.py ./obsidian-vault/Meetings/test.md 2>&1 | tail -20

# 2. 회의 파일 포맷 확인 (너무 짧지 않은지)

# 3. 다시 시도
```

### "ACTION_ITEMS.md 갱신 실패"

```bash
# 1. 파일 존재 확인
ls -la obsidian-vault/Meetings/ACTION_ITEMS.md

# 2. 파일 권한 확인
chmod 644 obsidian-vault/Meetings/ACTION_ITEMS.md

# 3. 다시 시도
```

---

## ✅ 설정 완료 체크리스트

```
[ ] Python 3.7+ 설치됨
[ ] anthropic 라이브러리 설치됨
[ ] ANTHROPIC_API_KEY 환경변수 설정됨
[ ] Obsidian vault 구조 생성됨
[ ] scripts/analyze_meeting.py 배치됨
[ ] obsidian-vault/Meetings/ 폴더 생성됨
[ ] ACTION_ITEMS.md 생성됨
[ ] 테스트 회의 파일로 실행 완료됨
[ ] 분석 결과 확인됨
[ ] ACTION_ITEMS.md 갱신 확인됨
```

---

## 🚀 다음 단계

1. ✅ 시스템 설정 완료
2. ✅ 테스트 실행 완료
3. ⏳ 실제 회의 기록 작성
4. ⏳ 스크립트 실행
5. ⏳ 팀에 공유
