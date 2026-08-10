# 🔵 Obsidian Vault 설정 가이드

**목표**: Obsidian에서 SSOT + 회의 하네스를 완벽하게 관리  
**소요시간**: 30분 (초기 설정)  
**요구**: Obsidian v1.0+

---

## 🚀 빠른 시작 (5분)

### 1단계: Vault 생성

```bash
# 기존 디렉토리를 Vault로 전환
cd /Users/mac/work/claude/20260810_harness/llm-ssot
```

Obsidian에서:
1. 메뉴 → "다른 vault 열기"
2. 경로 선택: `/Users/mac/work/claude/20260810_harness/llm-ssot`
3. "이 폴더를 vault로 열기"

### 2단계: 필수 플러그인 설치

```
설정 → 커뮤니티 플러그인 → "비활성화 안 함"
```

설치할 플러그인 (아래 목록):
- ✅ Dataview
- ✅ Templater
- ✅ Breadcrumbs
- ✅ Calendar
- ✅ Checklist
- ✅ Periodic Notes

### 3단계: 폴더 구조 확인

```
llm-ssot/
├── .obsidian/           (Obsidian 설정)
├── README.md            ⭐ 시작점
├── SSOT.md              📌 핵심
├── GOVERNANCE.md
├── QUICK_START.md
├── model-selection.md
├── prompt-engineering.md
├── Meetings/
│   ├── HARNESS.md
│   ├── _meeting-template.enhanced.md
│   ├── _agenda-from-previous.md
│   ├── ACTION_ITEMS.md
│   └── [회의록들]
├── Decisions/
│   ├── _decision-template.md
│   └── [ADR들]
└── Obsidian_Setup.md    👈 지금 보는 파일
```

✅ 완료! 이제 Obsidian 최적화로 이동.

---

## 🎯 Obsidian 플러그인 상세 설정

### 1️⃣ Dataview (필수)

**용도**: 회의록, 액션 아이템, ADR을 자동으로 쿼리하고 표로 표시

**설치**:
```
설정 → 커뮤니티 플러그인 → "Dataview" 검색 → 설치
```

**사용 예시**:

#### 📌 Action Items 자동 표시 (SSOT.md에 추가)

```dataview
TABLE
  status as "상태",
  deadline as "마감",
  owner as "담당자",
  link(file.name) as "링크"
FROM "Meetings/ACTION_ITEMS.md"
WHERE status != "✅ 완료"
SORT deadline ASC
```

#### 📅 최근 회의록 자동 표시

```dataview
TABLE
  date as "날짜",
  topic as "주제",
  decisions as "결정 수",
  link(file.path) as "보기"
FROM "Meetings"
WHERE date
SORT date DESC
LIMIT 10
```

#### 📊 ADR 상태 자동 표시

```dataview
TABLE
  status as "상태",
  created_date as "작성일",
  link(file.name) as "ADR"
FROM "Decisions"
WHERE contains(file.name, "ADR")
SORT created_date DESC
```

---

### 2️⃣ Templater (필수)

**용도**: 회의록, ADR을 템플릿으로 자동 생성

**설치**:
```
설정 → 커뮤니티 플러그인 → "Templater" 검색 → 설치
```

**설정**:
```
Templater 설정 → Templates folder location: "."
→ Enable system commands: "No" (보안)
→ Script queries open file on insertion: "Yes"
```

**템플릿 생성** (`.obsidian/templates/` 폴더에 저장):

#### Meeting Template (`meeting-new.md`)

```yaml
---
date: <% tp.date.now("YYYY-MM-DD") %>
time: ""
topic: ""
facilitator: ""
scribe: ""
participants: []
---

# 📅 <% tp.date.now("YYYY-MM-DD") %> [회의 주제]

[[../HARNESS.md#사용-방법-실제-예시|회의록 작성 가이드 보기]]

## 📊 회의 정보

| 항목 | 내용 |
|------|------|
| **날짜** | <% tp.date.now("YYYY-MM-DD") %> |
| **시간** | HH:MM ~ HH:MM |
| **의장** | [이름] |
| **기록자** | [이름] |
| **참석자** | [이름1], [이름2] |

## 🎯 아젠다

## 📝 논의 내용

### 안건 1: [주제]

**배경**:

**의견**:
- **[이름1]**: 

**토론 요점**:

## ✅ 결정사항

## 📌 행동항목

## 🔗 SSOT 영향

## 📎 참고자료
```

#### ADR Template (`adr-new.md`)

```yaml
---
status: "Draft"
created_date: <% tp.date.now("YYYY-MM-DD") %>
decision_type: "Type B"
---

# ADR-NNN: [제목]

**Status**: Draft  
**Date**: <% tp.date.now("YYYY-MM-DD") %>  
**Type**: Type B (일반)

## Context

## Decision

## Rationale

## Consequences

### Positive
- 

### Negative
-

## Alternatives Considered

## References

- [[../Meetings/]]
```

**사용 방법**:

```
Obsidian에서:
1. 명령어 팔레트 (Cmd+P)
2. "Templater: Open Insert Template modal"
3. "meeting-new" 또는 "adr-new" 선택
4. 자동으로 채워짐!
```

---

### 3️⃣ Breadcrumbs (필수)

**용도**: 문서 간 링크 시각화 (SSOT ← 회의록 ← 액션 아이템)

**설치**:
```
설정 → 커뮤니티 플러그인 → "Breadcrumbs" 검색 → 설치
```

**설정**:
```
Breadcrumbs 설정:
→ Primary Field: "up"
→ Fallback Field: "parent"
→ Show breadcrumbs in view: "Yes"
→ Render breadcrumbs in note: "No"
```

**사용 예시**:

회의록 파일의 YAML 헤더에 추가:

```yaml
---
up: [[SSOT]]
parent: [[SSOT]]
---
```

결과: 화면 상단에 "SSOT > 2026-08-17_meeting > ACTION_ITEMS" 처럼 표시됨

---

### 4️⃣ Calendar (권장)

**용도**: 회의 날짜 캘린더로 시각화

**설치**:
```
설정 → 커뮤니티 플러그인 → "Calendar" 검색 → 설치
```

**사용**:
- 좌측 패널에서 캘린더 보기
- 각 날짜에 회의록이 자동으로 표시됨
- 클릭하면 회의록 열림

**설정** (Optional):
```
Calendar 설정:
→ Show dots only for existing notes: "Yes"
→ Confirm on file creation: "No"
```

---

### 5️⃣ Checklist (권장)

**용도**: Action Items의 체크박스 더 잘 관리

**설치**:
```
설정 → 커뮤니티 플러그인 → "Checklist" 검색 → 설치
```

**기능**:
- 체크박스에 클릭하면 자동으로 `[ ]` → `[x]` 변경
- 우클릭 → "완료 시간 기록" (선택사항)

---

### 6️⃣ Periodic Notes (권장)

**용도**: 일일/주간/월간 노트 자동 생성

**설치**:
```
설정 → 커뮤니티 플러그인 → "Periodic Notes" 검색 → 설치
```

**설정**:
```
Periodic Notes 설정:
→ Daily: Enable
  - Format: YYYY-MM-DD.md
  - Folder: Meetings/Daily
  - Template: meeting-new

→ Weekly: Enable
  - Format: YYYY-[W]WW.md
  - Folder: Meetings/Weekly

→ Monthly: Enable
  - Format: YYYY-MM.md
  - Folder: Meetings/Monthly
```

**사용**:
```
명령어 팔레트 (Cmd+P):
- "Periodic Notes: Open today" → 오늘의 일일 노트 열기
- "Periodic Notes: Open this week" → 이주 주간 노트 열기
- "Periodic Notes: Open this month" → 이달 월간 노트 열기
```

---

## 📱 Obsidian 테마 & 모양 설정

### 권장 테마

```
설정 → 모양 → 테마
→ "Minimal" 또는 "Cybertron" 추천
→ "Minimal Theme Settings" → 색상 커스터마이징
```

### 추천 색상 (Minimal 테마)

```css
/* .obsidian/theme-customization.css */

/* SSOT 항목 강조 (주황색) */
.tag[href*="SSOT"] {
  background: #ff9500;
  color: white;
}

/* 회의록 (파란색) */
.tag[href*="Meeting"] {
  background: #0066ff;
  color: white;
}

/* ADR 결정 (초록색) */
.tag[href*="Decision"] {
  background: #10b981;
  color: white;
}

/* 액션 아이템 (빨간색) */
.tag[href*="Action"] {
  background: #ef4444;
  color: white;
}
```

---

## 🎯 Obsidian 그래프 뷰 (Graph View)

**용도**: 모든 문서와 링크를 시각적으로 표시

**사용 방법**:
```
오른쪽 패널 → Graph View (🕸️ 아이콘)
```

**최적화**:
```
Graph View 설정:
→ Show attachments: No
→ Show existing only: Yes
→ Filters:
  - Tag: ssot (강조)
  - Tag: meeting (강조)
  - Tag: decision (강조)
```

**보는 방법**:
- 중앙의 SSOT.md가 중심
- 회의록, ADR, Action Items이 주변에 연결됨
- 드래그해서 회전, 줌으로 확대/축소

---

## 🔖 태그 시스템 (Tagging System)

**권장 태그 구조**:

### 문서 유형 태그

```
#ssot - SSOT 핵심 문서
#meeting - 회의록
#decision - ADR 의사결정
#action - 액션 아이템
#template - 템플릿
```

### 우선순위 태그

```
#urgent - 긴급 (3일)
#normal - 일반 (1-2주)
#backlog - 백로그
#completed - 완료
```

### 상태 태그

```
#draft - 초안
#review - 검토 중
#approved - 승인됨
#archived - 보관됨
```

### 주제별 태그

```
#model-selection
#prompt-engineering
#inference-strategy
#evaluation
#scaling-laws
#error-handling
```

**사용 예시** (회의록에):

```yaml
---
tags:
  - meeting
  - normal
  - model-selection
  - 2026-08-17
---
```

**태그로 검색**:
```
Obsidian 검색:
- #meeting #model-selection → 모델 선택 관련 모든 회의
- #action #urgent → 긴급 액션 아이템
- #decision #completed → 완료된 의사결정
```

---

## 🔍 Obsidian 검색 최적화

### 고급 검색 문법

```
검색창에서:

# 모든 긴급 액션 아이템
"action" "urgent" "pending"

# 특정 사람의 액션
"[이름]" path:Meetings "action"

# 특정 기간의 회의록
"2026-08" path:Meetings

# SSOT 변경사항
"변경" path:Decisions "ADR"

# 진행 중인 ADR
"Type B" "draft" path:Decisions
```

### 검색 프리셋 저장

```
Obsidian 검색 패널:
1. 위 검색어 입력
2. "🔖" 아이콘 클릭
3. "저장" 또는 "새 탭 저장"
4. 이름: "긴급 액션 아이템" 등

다음부터 클릭 한 번에 검색됨!
```

---

## 📊 Obsidian Frontmatter 구조

### 회의록 Frontmatter

```yaml
---
date: 2026-08-17
time: "10:00-11:00"
topic: "모델 선택 기준 정의"
facilitator: "[이름1]"
scribe: "[이름2]"
participants:
  - "[이름1]"
  - "[이름2]"
  - "[이름3]"
decisions: 3
action_items: 3
ssot_impact:
  - "model-selection"
  - "prompt-engineering"
adr_created:
  - "ADR-002"
tags:
  - meeting
  - model-selection
  - type-b
links:
  - "[[SSOT]]"
  - "[[model-selection]]"
---
```

### ADR Frontmatter

```yaml
---
status: "Draft"  # Draft / Review / Approved / Implemented
created_date: 2026-08-17
created_by: "[이름]"
decision_type: "Type B"  # Type A / Type B / Type C
priority: "high"  # high / normal / low
impact: "medium"  # high / medium / low
ssot_change: "model-selection.md"
meeting_reference: "[[Meetings/2026-08-17_*]]"
tags:
  - decision
  - type-b
  - model-selection
---
```

---

## 💾 Obsidian 백업 & 동기화

### 로컬 백업 (자동)

```
설정 → Obsidian Sync (선택사항)
또는
수동: git + GitHub
```

**Git 설정** (권장):

```bash
cd /Users/mac/work/claude/20260810_harness/llm-ssot

# Git 초기화 (처음만)
git init
git add .
git commit -m "Initial SSOT + Meeting Harness"

# 이후 자동 커밋 (매일)
# (Git hook 또는 cron 작업으로 구성)
```

### GitHub 동기화

```bash
# 원격 저장소 추가
git remote add origin https://github.com/[user]/llm-ssot.git

# 처음 푸시
git push -u origin main

# 이후 자동 푸시
# (GitHub Actions 또는 로컬 스크립트)
```

---

## 🎓 Obsidian 팁 & 트릭

### 1️⃣ 링크 빠르게 만들기

```
[[ 입력하면 자동 완성됨
[[model]] → [[model-selection.md]]
```

### 2️⃣ 문서 미리보기

```
Ctrl+클릭 (또는 Cmd+클릭)
→ 옆 패널에 문서 미리보기
```

### 3️⃣ 백링크 (역링크) 보기

```
우측 패널 → "역링크" (🔗 아이콘)
→ "이 문서를 링크하는 모든 문서" 자동 표시

예: model-selection.md를 열면:
- Meetings/2026-08-17_*
- Decisions/ADR-002
- SSOT.md
... 모두 자동으로 표시됨
```

### 4️⃣ 빠른 스위처 (Quick Switcher)

```
Cmd+O (또는 Ctrl+O)
→ "2026-08" 입력
→ 2026-08로 시작하는 모든 파일 표시
→ 엔터로 열기
```

### 5️⃣ 명령어 팔레트

```
Cmd+P (또는 Ctrl+P)
→ "templater" 입력
→ 명령어 자동 완성
→ "Templater: Insert template" 선택
```

---

## ✅ Obsidian 초기 설정 체크리스트

- [ ] Vault 생성됨
- [ ] 필수 플러그인 설치됨:
  - [ ] Dataview
  - [ ] Templater
  - [ ] Breadcrumbs
  - [ ] Calendar
  - [ ] Checklist
  - [ ] Periodic Notes
- [ ] 템플릿 폴더 생성됨: `.obsidian/templates/`
- [ ] 템플릿 파일 저장됨:
  - [ ] `meeting-new.md`
  - [ ] `adr-new.md`
- [ ] 테마 설정됨 (선택사항)
- [ ] 태그 시스템 설정됨
- [ ] Git 초기화됨 (선택사항)
- [ ] 첫 회의록 생성 테스트 완료

---

## 🚀 첫 회의 준비하기

### 1단계: 회의 생성

```
Obsidian에서:
1. 명령어 팔레트 (Cmd+P)
2. "Templater: Open Insert Template modal"
3. "meeting-new" 선택
4. 파일명 변경: 2026-08-XX_주제.md
5. 자동으로 템플릿 채워짐!
```

### 2단계: 회의록 작성

```
회의 정보, 의견, 결정, 액션 아이템 기입
```

### 3단계: SSOT 링크

```
회의록에서 관련 SSOT 문서 링크:
[[model-selection]]
[[GOVERNANCE]]
```

### 4단계: Dataview 확인

```
SSOT.md를 열면:
- 최근 회의록 자동 표시
- 진행 중 액션 아이템 자동 표시
- 모두 링크로 연결됨!
```

---

## 📞 Obsidian 도움말

- **공식 도움말**: https://help.obsidian.md/
- **플러그인 가이드**: https://obsidian.md/plugins
- **커뮤니티**: https://forum.obsidian.md/
- **Reddit**: r/ObsidianMD

---

## 🎯 다음 단계

1. ✅ Vault 생성
2. ✅ 플러그인 설치
3. ✅ 템플릿 설정
4. ✅ 첫 회의록 작성
5. ✅ SSOT와 연결
6. ✅ Slack 통합 (선택사항)

---

**시작하기**: Obsidian에서 명령어 팔레트 (Cmd+P) → "Templater" 검색 → 템플릿 선택!
