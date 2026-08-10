# 🔧 Obsidian 플러그인 설정 가이드

**목표**: 6가지 플러그인 설치 및 최적화  
**소요시간**: 약 30분  
**난이도**: 초급

---

## 📋 플러그인 설치 순서

### 1️⃣ Dataview (필수)

**목적**: 자동 쿼리로 액션, 회의, 결정사항 표시

**설치**:
```
Obsidian → Settings → Community Plugins
→ "Dataview" 검색 → Install → Enable
```

**초기 설정**:
1. Settings → Dataview → Enable JavaScript queries ✅
2. Settings → Dataview → Enable Inline Queries ✅

**사용 예시**:
```dataview
TABLE status as "상태", owner as "담당자", due as "마감"
FROM "Meetings/ACTION_ITEMS"
WHERE status = "⏳"
SORT due ASC
```

**테스트**: 
- [ ] Dashboard.md 열기 → 쿼리 실행됨?

---

### 2️⃣ Templater (필수)

**목적**: 회의 생성 시 자동으로 템플릿 생성

**설치**:
```
Settings → Community Plugins → "Templater" 
→ Install → Enable
```

**초기 설정**:
```
Settings → Templater:
├─ Template folder location: "Templates"
├─ Trigger Templater on new file creation: ✅
└─ Enable system commands: ✅
```

**회의 템플릿 생성** (`Templates/meeting-new.md`):
```markdown
# 📅 <% tp.date.now("YYYY-MM-DD") %> 제목

## 📊 회의 정보
| 항목 | 내용 |
|------|------|
| **날짜** | <% tp.date.now("YYYY-MM-DD") %> |
| **의장** | [이름] |
| **참석자** | [이름1], [이름2] |

## 📝 논의 내용

### 안건 1: 
**배경**: 

**의견**: 
- **[이름]**: 

**결정**: 

## 📌 액션
- [ ] **[담당자]** - [작업] (마감: YYYY-MM-DD)

## 🔗 SSOT 영향
- [[]]
```

**테스트**:
- [ ] File → New → meeting-new 실행
- [ ] 템플릿이 자동 생성되나?

---

### 3️⃣ Breadcrumbs (선택)

**목적**: 문서 관계 시각화

**설치**:
```
Settings → Community Plugins → "Breadcrumbs" 
→ Install → Enable
```

**초기 설정**:
```
Settings → Breadcrumbs:
├─ Hierarchy field name: "up"
├─ Show breadcrumbs: ✅
└─ Show matrix view: ✅
```

**사용**:
문서 첫 줄에 `up: [[WIKI/WIKI_INDEX]]` 추가하면 자동으로 계층 구조 표시

---

### 4️⃣ Calendar (선택)

**목적**: 날짜별 회의 보기

**설치**:
```
Settings → Community Plugins → "Calendar" 
→ Install → Enable
```

**초기 설정**:
```
Settings → Calendar:
├─ Show week numbers: ✅
├─ Show weekly notes: ✅
└─ Folder for weekly notes: "Weekly"
```

**사용**:
- 좌측 사이드바에 달력 표시
- 회의 날짜를 클릭하면 해당 회의록 열림

---

### 5️⃣ Checklist (선택)

**목적**: 액션 아이템 체크 및 자동 추적

**설치**:
```
Settings → Community Plugins → "Checklist" 
→ Install → Enable
```

**초기 설정**:
```
Settings → Checklist:
├─ Sort checklist items: ✅
├─ Mark list items complete: ✅
└─ Move completed items: "Bottom"
```

**사용**:
- [ ] 체크박스 항목 클릭하면 자동 체크됨
- 완료된 항목은 자동으로 아래로 이동

---

### 6️⃣ Periodic Notes (필수)

**목적**: 일일/주간 Note 자동 생성

**설치**:
```
Settings → Community Plugins → "Periodic Notes" 
→ Install → Enable
```

**초기 설정**:
```
Settings → Periodic Notes:
Daily Notes:
├─ Folder: "Daily"
└─ Format: "YYYY-MM-DD"

Weekly Notes:
├─ Folder: "Weekly"  
└─ Format: "YYYY-[W]WW"

Monthly Notes:
├─ Folder: "Weekly"
└─ Format: "YYYY-MM"
```

**사용**:
- Cmd+P → "Periodic Notes: Open today note"
- 매일 자동으로 Daily Note 생성
- 매주 자동으로 Weekly Note 생성

**Daily Note 템플릿** (`Templates/daily.md`):
```markdown
# 📅 <% tp.date.now("YYYY-MM-DD") %>

## 📋 오늘 할 일
- [ ] 

## 📊 진행 현황
- 

## 🎯 우선순위
1. 
2. 
3. 

## 📝 메모
-
```

---

## ✅ 설정 검증 체크리스트Rkwl rbclr 


### 플러그인 활성화 확인

- [ ] Dataview: 쿼리 실행됨
- [ ] Templater: 템플릿 자동 생성됨
- [ ] Breadcrumbs: 계층 구조 표시됨
- [ ] Calendar: 달력 표시됨
- [ ] Checklist: 체크박스 작동됨
- [ ] Periodic Notes: Daily/Weekly Note 생성됨

### 템플릿 확인

- [ ] Templates/meeting-new.md 생성됨
- [ ] Templates/daily.md 생성됨
- [ ] Templates/adr.md 생성됨 (아직)

### 쿼리 테스트

- [ ] Dataview 쿼리 정상 동작
- [ ] ACTION_ITEMS 자동 표시
- [ ] 회의 타임라인 자동 표시

---

## 🔧 트러블슈팅

### "Dataview 쿼리가 실행 안 됨"

```
해결:
1. Settings → Community Plugins → Dataview
2. "Render inline queries" 활성화
3. 문서 다시 저장 (Cmd+S)
```

### "Templater로 새 파일 생성 안 됨"

```
해결:
1. Templates 폴더가 "Templates"인지 확인
2. 문서명이 정확한지 확인 (예: "meeting-new.md")
3. Templater 재활성화
```

### "Daily Note가 생성 안 됨"

```
해결:
1. Periodic Notes 활성화 확인
2. Daily 폴더가 "Daily"인지 확인
3. Cmd+P → "Periodic Notes: Open today note" 실행
```

---

## 📚 다음 단계

1. **문서 마이그레이션** (SSOT, Meetings, Decisions 복사)
2. **Dataview 대시보드** 구성
3. **첫 회의** 테스트 (2026-08-17)

---

**설정 완료 예상**: 2026-08-15  
**첫 회의**: 2026-08-17  
**목표**: 100% 자동화 시스템

---

## 💡 팁

### 빠른 명령어

```
Cmd+P 후 입력:
- "Periodic Notes: Open today note"
- "Insert template"
- "Show graph view"
```

### 자주 사용할 폴더

- `/Meetings` - 회의록
- `/Decisions` - 결정사항 (ADR)
- `/Daily` - 일일 노트
- `/Templates` - 템플릿들

### 최적 워크플로우

```
1. Daily Note 열기 (매일 아침)
2. 오늘 할일 확인
3. 회의 있으면 회의 템플릿 생성
4. 회의 후 액션 아이템 기록
5. Weekly Note 확인 (매주 월요일)
```

---

**생성일**: 2026-08-10  
**버전**: 1.0  
**다음 업데이트**: 첫 회의 후 (8/17)
