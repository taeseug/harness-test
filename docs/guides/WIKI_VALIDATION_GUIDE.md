# 📊 Wiki 검증 시스템 완벽 가이드

> **기계 검증 + LLM 검증을 통한 Wiki 품질 보증**

---

## 🎯 개요

Wiki 적재 후 **2단계 검증**으로 품질을 확보합니다:

```
Wiki 파일 생성
    ↓
[1단계] 기계 검증 (스크립트)
    ├─ Frontmatter 검증
    ├─ 스키마 구조 검증
    └─ 파일명 규칙 검증
    ↓
[2단계] LLM 검증 (스킬)
    ├─ 내용 일치도
    ├─ 허구 생성 여부
    ├─ 누락된 내용
    └─ 액션 상태 추적
    ↓
최종 품질 평가 ✅
```

---

## 📋 1단계: 기계 검증 (Mechanical Validation)

### 목적
- Frontmatter가 올바른가?
- 파일 구조가 스키마를 따르는가?
- 파일명 규칙이 맞는가?

### 실행 방법

**기본 사용:**
```bash
python3 scripts/validate-wiki.py ./obsidian-vault/Meetings
```

**출력 예:**
```
============================================================
🔍 Wiki 기계 검증 시작
============================================================

📊 발견된 파일: 6개

✅ [1/6] 2026-04-16-제품주간회의.enhanced.md
✅ [2/6] 2026-05-14-제품주간회의.enhanced.md
✅ [3/6] 2026-06-11-제품주간회의.enhanced.md
✅ [4/6] 2026-06-25-온보딩개선회의.enhanced.md
✅ [5/6] 2026-07-09-제품주간회의.enhanced.md
❌ [6/6] 2026-07-23-제품주간회의.enhanced.md
   ⚠️ [frontmatter] 필수 필드 'enhanced_date' 누락
   ⚠️ [filename] 파일 확장자가 '.enhanced.md'이 아님

============================================================
📈 검증 결과
============================================================
총 파일: 6
통과: 5 (83.3%)
실패: 1

⚠️ 수정이 필요한 파일들:
  - Meetings/2026-07-23-제품주간회의.enhanced.md
```

### 검증 항목 상세

#### 1️⃣ Frontmatter 검증

**필수 필드:**
```yaml
---
date: YYYY-MM-DD          # 회의 날짜
type: meeting             # 타입 (meeting)
status: ✅/⏳/❌          # 상태
enhanced_date: YYYY-MM-DD # 위키 생성 날짜
participants:             # 참석자 (선택)
  - 이름1
  - 이름2
---
```

**검증 기준:**
- ✅ `date` 형식: YYYY-MM-DD
- ✅ `type` 값: "meeting"
- ✅ `status` 값: ✅ 또는 ⏳ 또는 ❌
- ✅ `enhanced_date` 형식: YYYY-MM-DD
- ⚠️ `participants` 형식: 리스트

**실패 예시:**
```yaml
# ❌ 잘못된 예
date: 2026/06/11           # YYYY-MM-DD 아님
status: 완료                # ✅/⏳/❌ 아님
enhanced_date: 20260610    # 형식 오류

# ✅ 올바른 예
date: 2026-06-11
status: ✅
enhanced_date: 2026-08-10
```

#### 2️⃣ 스키마 검증

**필수 섹션:**
```markdown
## 📝 논의 내용
  (또는 ## 💬 주요 논의 사항)

## ✅ 의사결정
  (또는 ## 🎯 결정사항)

## 🎯 액션 아이템
  (또는 ## 📌 행동항목)
```

**권장 섹션:**
```markdown
## 회의 정보
- 날짜: YYYY-MM-DD
- 시간: HH:MM
- 장소: ...
- 참석자: ...

## 📝 논의 내용
- 주제 1
- 주제 2

## ✅ 의사결정
| 항목 | 결정 | 담당자 | 상태 |
|-----|------|--------|------|

## 🎯 액션 아이템
- [ ] 작업 1 (담당: OOO, 마감: YYYY-MM-DD)
- [ ] 작업 2

## 📌 우려사항
- 위험 1
- 위험 2

## 🔗 관련 문서
- [[링크1]]
- [[링크2]]
```

**검증 기준:**
- ✅ 필수 3개 섹션 존재
- ✅ 마크다운 제목(##) 사용
- ⚠️ 회의 정보 섹션 권장

#### 3️⃣ 파일명 규칙

**규칙:**
```
YYYY-MM-DD-<회의명>.enhanced.md
```

**예시:**
```
✅ 2026-06-11-제품주간회의.enhanced.md
✅ 2026-06-25-온보딩개선회의.enhanced.md
❌ 2026/06/11-제품주간회의.enhanced.md        (날짜 형식)
❌ 2026-06-11-제품주간회의.md                 (확장자)
❌ 제품주간회의-2026-06-11.enhanced.md         (순서)
```

**검증 기준:**
- ✅ YYYY-MM-DD 형식의 날짜
- ✅ 유효한 날짜 (2026-13-01 불가)
- ✅ .enhanced.md 확장자
- ✅ 회의명에 한글/영문만 사용
- ❌ 특수문자 (!@#$%, 등)

### 결과 해석

**리포트 파일:**
```
obsidian-vault/validation_report.json
```

**JSON 구조:**
```json
{
  "timestamp": "2026-08-10T15:30:00",
  "stats": {
    "total_files": 6,
    "valid_files": 5,
    "files_with_issues": 1
  },
  "results": [
    {
      "file": "Meetings/2026-06-11-제품주간회의.enhanced.md",
      "valid": true,
      "frontmatter": {"valid": true, "issues": []},
      "schema": {"valid": true, "issues": []},
      "filename": {"valid": true, "issues": []}
    }
  ],
  "summary": {
    "total": 6,
    "valid": 5,
    "invalid": 1,
    "pass_rate": "83.3%"
  }
}
```

### 수정 방법

**문제 1: Frontmatter 누락**
```
❌ 상황: Frontmatter가 없음
✅ 해결:
---
date: 2026-06-11
type: meeting
status: ✅
enhanced_date: 2026-08-10
---

# 회의록 제목
...
```

**문제 2: 파일명 오류**
```
❌ 현재: 제품주간회의-2026-06-11.enhanced.md
✅ 수정: 2026-06-11-제품주간회의.enhanced.md

# 터미널에서:
mv "제품주간회의-2026-06-11.enhanced.md" "2026-06-11-제품주간회의.enhanced.md"
```

**문제 3: 필수 섹션 누락**
```
❌ 상황: "의사결정" 섹션이 없음
✅ 해결: 파일에 다음 추가

## ✅ 의사결정
| 항목 | 결정 | 담당자 | 상태 |
|-----|------|--------|------|
| 안건1 | 결정1 | OOO | ✅ |
```

---

## 📖 2단계: LLM 검증 (Content Validation)

### 목적

기계 검증으로는 알 수 없는 **콘텐츠 품질**을 LLM이 검증합니다:

- ✅ 원본 회의록과 wiki가 일치하는가?
- ✅ 잘못된 정보(hallucination)가 있는가?
- ✅ 중요한 내용을 빠뜨렸는가?
- ✅ 액션 아이템들이 정확히 추적되는가?

### 실행 방법

**가장 간단한 방법:**
```
Claude Code에서 다음 입력:
"2026-06-11 회의 wiki를 검증해줄래?"
```

**구체적인 요청:**
```
"2026-06-11 제품주간회의:
- 원본: llm-ssot/Meetings/2026-06-11-제품주간회의.enhanced.md
- Wiki: obsidian-vault/Meetings/2026-06-11-제품주간회의.enhanced.md

이 둘을 비교해서:
1. 내용이 일치하는가?
2. 허구로 생성된 내용은 없나?
3. 누락된 액션이 있나?
4. 액션의 담당자와 마감일이 정확한가?

를 검증해줄래?"
```

**여러 회의 한번에 검증:**
```
"지난 회의 6개 (4월~7월)의 wiki를 모두 검증해줄래?
각 wiki에 대해:
- 일치도 점수
- 허구 여부
- 누락된 내용
을 보고해줄래?"
```

### 검증 결과 해석

#### 1️⃣ 일치도 (Alignment Score)

**95점 이상**: 탁월함 ⭐⭐⭐⭐⭐
```
✅ 요약이 정확
✅ 주요 논점 모두 포함
✅ 표현이 원본과 유사
→ 배포 가능
```

**85-94점**: 매우 좋음 ⭐⭐⭐⭐
```
✅ 대부분 일치
⚠️ 사소한 표현 차이
→ 경미한 수정 후 배포
```

**75-84점**: 좋음 ⭐⭐⭐
```
⚠️ 일부 내용 다름
⚠️ 명확하지 않은 부분
→ 검토 권장
```

**65-74점**: 미흡 ⭐⭐
```
⚠️ 여러 부분 다름
⚠️ 주요 내용 누락
→ 수정 필요
```

**65점 미만**: 부족 ⭐
```
❌ 주요 내용 누락
❌ 신뢰도 낮음
→ 다시 작성 권장
```

#### 2️⃣ 허구 탐지 (Hallucination Detection)

**허구 없음**: 최고 등급 ✅
```json
{
  "detected": false,
  "verdict": "모든 내용이 원본과 일치"
}
```

**경미한 허구**: 경고 ⚠️
```json
{
  "detected": true,
  "items": [
    {
      "type": "액션",
      "content": "API 문서 작성 (원본에 없음)",
      "severity": "low"
    }
  ],
  "verdict": "영향 작음, 수정 권장"
}
```

**심각한 허구**: 재작성 필요 ❌
```json
{
  "detected": true,
  "items": [
    {
      "type": "의사결정",
      "content": "Q3 로드맵 변경 (원본에 없음)",
      "severity": "high"
    },
    {
      "type": "액션",
      "content": "3개의 虚構 액션",
      "severity": "high"
    }
  ],
  "verdict": "신뢰도 낮음, 다시 작성 필요"
}
```

#### 3️⃣ 완성도 (Completeness)

**100%**: 모든 내용 포함
```
✅ 모든 액션 기록됨
✅ 모든 결정 기록됨
✅ 우려사항/위험 포함
```

**90-99%**: 거의 모든 내용
```
✅ 주요 내용 포함
⚠️ 부가 정보 일부 누락
→ 주석 추가 권장
```

**80-89%**: 중요 내용 포함
```
⚠️ 일부 액션 누락
⚠️ 부가 정보 누락
→ 재검토 권장
```

**80% 미만**: 주요 누락
```
❌ 중요 액션 누락
❌ 결정사항 누락
→ 수정 필요
```

#### 4️⃣ 액션 상태 추적 (Action Status Tracking)

**상태 종류:**
- `⏳ 열림`: 아직 진행 중 또는 시작 안 됨
- `✅ 완료`: 완료됨
- `⏸️ 홀드`: 의도적으로 보류 중
- `❌ 취소`: 취소됨
- `❓ 조용히 사라짐`: 상태 불명확

**검증 항목:**
```json
{
  "actions": [
    {
      "item": "A사 테스트 계정 발급",
      "owner": "박준서",
      "due_date": "2026-06-18",
      "status": "⏳",
      "status_accuracy": "정확",
      "notes": "담당자와 마감일 명확"
    },
    {
      "item": "정산 주기 재검토",
      "owner": "이지혜, 박준서",
      "due_date": null,
      "status": "⏸️",
      "status_accuracy": "경고",
      "notes": "⚠️ 마감일 미정 - 재검토 필요"
    }
  ]
}
```

### 최종 평점

```
종합 평점 = (일치도 + 허구_역수 + 완성도 + 액션_정확도) / 4

A+ (95점~):   탁월 - 배포 가능
A  (90점~):   우수 - 경미한 수정 후 배포
B+ (85점~):   양호 - 주석 추가 권장
B  (80점~):   보통 - 재검토 권장
C  (70점~):   미흡 - 수정 필요
D  (60점~):   부족 - 상당한 수정 필요
F  (~60점):   불가 - 다시 작성 권장
```

---

## 🔄 검증 워크플로우 (전체 흐름)

### Day 1: Wiki 생성
```bash
# 원본 회의록을 Wiki로 변환
python3 scripts/migrate-docs-advanced.py
# 또는 Claude Code에서 직접 생성
```

### Day 2: 기계 검증
```bash
# 1단계 검증 실행
python3 scripts/validate-wiki.py ./obsidian-vault/Meetings

# 결과 확인
cat obsidian-vault/validation_report.json

# 오류 수정 (필요시)
# - Frontmatter 수정
# - 파일명 변경
# - 섹션 추가
```

### Day 3: LLM 검증
```
Claude Code에서:
"지난 wiki들을 모두 검증해줄래?"

또는 개별적으로:
"2026-06-11 회의 wiki를 검증해줄래?"
```

### Day 4: 피드백 반영
```
검증 결과 검토
  ↓
개선 사항 식별
  ↓
Wiki 파일 수정
  ↓
필요시 재검증
  ↓
최종 배포 ✅
```

---

## 💾 검증 결과 저장

### 기계 검증 리포트
```
위치: obsidian-vault/validation_report.json
형식: JSON
내용: 모든 파일의 검증 결과
```

### LLM 검증 리포트 (수동 저장)
```
위치: docs/references/wiki-validation-results.json (추천)
또는: obsidian-vault/_validation_results/
형식: JSON
내용: 각 wiki의 일치도, 허구, 누락 정보
```

---

## 🎯 품질 기준 요약

| 항목 | 기준 | 확인 |
|------|------|------|
| **Frontmatter** | date, type, status, enhanced_date 필수 | 기계 검증 |
| **구조** | 3개 필수 섹션 (논의, 결정, 액션) | 기계 검증 |
| **파일명** | YYYY-MM-DD-<name>.enhanced.md | 기계 검증 |
| **일치도** | 90점 이상 | LLM 검증 |
| **허구** | 0개 (경미한 것도 권장하지 않음) | LLM 검증 |
| **완성도** | 90% 이상 | LLM 검증 |
| **액션 정확도** | 90% 이상 | LLM 검증 |

---

## 🚀 빠른 시작 (5분)

### 1️⃣ 기계 검증 실행
```bash
python3 scripts/validate-wiki.py ./obsidian-vault/Meetings
```

### 2️⃣ 결과 확인
```bash
cat obsidian-vault/validation_report.json | jq .summary
```

### 3️⃣ LLM 검증 요청 (Claude Code)
```
2026-06-11 회의 wiki를 검증해줄래?
```

### 4️⃣ 결과 검토 및 개선

완료! ✅

---

## 📚 참고 문서

- **기계 검증 스크립트**: `scripts/validate-wiki.py`
- **LLM 검증 스킬**: `.claude/skills/wiki-content-reviewer/`
- **회의 자동 분석 스킬**: `.claude/skills/obsidian-meeting-analyzer/`

---

**마지막 업데이트**: 2026-08-10  
**버전**: 1.0  
**상태**: ✅ 준비 완료
