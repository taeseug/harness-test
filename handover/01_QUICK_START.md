# 01_QUICK_START.md - 5분 빠른 시작

**소요시간**: 5분  
**대상**: 모든 팀원  
**목표**: 전체 시스템 이해하기

---

## 🚀 30초 핵심 요약

```
LLM SSOT = LLM 엔지니어링의 중앙 규칙서

1. SSOT.md = 모든 규칙이 한 곳에 정의됨
2. Meetings/ = 회의록 + 자동화
3. Decisions/ = 의사결정 기록 (ADR)
4. Obsidian = 모두 링크로 연결됨
5. Automation = 전후 처리 자동화
```

---

## 📋 3단계로 이해하기

### 1️⃣ SSOT란? (1분)

**Single Source of Truth** = 한 곳에서만 진실

```
❌ 이전: 규칙이 여러 문서에 산재
✅ 이후: SSOT.md에 모두 정의
         다른 곳은 "[[SSOT.md]] 참조"
```

### 2️⃣ 회의 자동화? (2분)

```
회의 전
  ↓ Claude가 자동으로
  • 아젠다 생성
  • 배경 자료 수집
  
회의 중
  ↓ 템플릿에 맞춰 기록
  
회의 후
  ↓ Claude가 자동으로
  • 요약 생성
  • 액션 추출
  • ADR 작성
  • SSOT 업데이트
  • Slack 알림
```

### 3️⃣ Obsidian? (2분)

```
Obsidian = 관계형 노트 앱

특징:
  • 모든 문서가 링크로 연결됨
  • 역링크 (백링크) 자동 표시
  • 플러그인으로 자동화 (6개)
  • 대시보드로 한눈에 추적
```

---

## 🎯 5가지 사용 시나리오

### 시나리오 1: "모델을 선택해야 하는데 기준이 뭐야?"

```
1. SSOT.md 열기
   → "📌 모델 선택" 섹션 확인
   
2. 세부 문서 읽기
   → [[02_SSOT_STRUCTURE.md]] 참조
   
3. 과거 결정 확인
   → Decisions/ 폴더에서 ADR 검색
   
4. 질문 있으면
   → [[03_GOVERNANCE.md]] 에서 Owner 찾기
```

### 시나리오 2: "다음 회의를 어떻게 진행하지?"

```
1. OBSIDIAN 명령어 팔레트 (Cmd+P)
   → "Templater: Insert Template"
   
2. "meeting-new" 선택
   → 아젠다 자동 생성됨!
   
3. 회의 중 기록
   → 템플릿 구조에 맞춰 의견, 결정, 액션 기록
   
4. 회의 후
   → Claude가 자동으로 정리, SSOT 업데이트
```

### 시나리오 3: "액션 아이템 현황이 궁금해"

```
OBSIDIAN DASHBOARD.md 열기
  → "📌 오늘 해야 할 일" 섹션
  → 마감 임박 액션 자동 표시
  → 우선순위별로 정렬됨
```

### 시나리오 4: "왜 이런 결정을 했지?"

```
Decisions/ 폴더에서 ADR 찾기
  → "ADR-001-Model-Selection" 같은 파일
  → Context 섹션: 왜 필요했나?
  → Decision 섹션: 뭘 결정했나?
  → Consequences: 어떤 영향이 있나?
```

### 시나리오 5: "SSOT를 수정하고 싶은데?"

```
1. [[03_GOVERNANCE.md]] 읽기
   → 변경 관리 프로세스 확인
   
2. 담당 Owner에게 제안
   → Type 분류 (긴급/일반/경미)
   
3. ADR 작성 (필요시)
   → [[04_MEETING_HARNESS.md]] 참고
   
4. 팀 검토 및 승인
   → 2-3일 소요
   
5. SSOT 업데이트
   → 변경 이력 기록
```

---

## 📚 핵심 문서 위치

| 이름 | 파일 | 소요시간 | 시기 |
|------|------|---------|------|
| 빠른 시작 | 01_QUICK_START.md | 5분 | 입사 첫날 |
| SSOT 규칙 | 02_SSOT_STRUCTURE.md | 15분 | 입사 이틀째 |
| 책임소재 | 03_GOVERNANCE.md | 10분 | 필요시 |
| 회의 방법 | 04_MEETING_HARNESS.md | 30분 | 회의 전 |
| Obsidian | 05_OBSIDIAN_SETUP.md | 30분 | 처음 한 번 |
| 대시보드 | 06_DASHBOARD.md | 1분 | 매일 |

---

## 👥 책임자 (입력 필요)

| 역할 | 이름 | Slack |
|------|------|-------|
| **SSOT 최고책임자** | [입력] | @owner |
| **모델 선택 Owner** | [입력] | @owner1 |
| **프롬프트 Owner** | [입력] | @owner2 |
| **평가 방법 Owner** | [입력] | @owner3 |
| **기술리더** | [입력] | @techLead |

---

## 📅 정기 일정

```
🎯 주간 팀 회의
  └─ [[04_MEETING_HARNESS.md]] 템플릿 사용

📊 월간 SSOT 리뷰
  └─ 지난달 변경사항 + 현안 논의 + 다음달 계획

📈 분기 감사
  └─ SSOT 최신성 + 팀 준수도 점검
```

---

## ✅ 신규자 체크리스트

**입사 당일:**
- [ ] 이 파일 (01_QUICK_START.md) 읽기 (5분)
- [ ] 02_SSOT_STRUCTURE.md 읽기 (15분)
- [ ] 담당 주제 문서 읽기 (30분)
- [ ] Slack #ssot 채널 구독

**입사 이틀째:**
- [ ] 이전 회의록 3개 읽기 (30분)
- [ ] Owner와 1:1 미팅 (30분)
- [ ] Obsidian vault 설정 (05 참고)

**1주일 후:**
- [ ] 팀 회의 참석 + 기록
- [ ] SSOT 문서 한 개 업데이트 해보기

---

## 💡 팁

### Obsidian 단축키
```
Cmd+P    = 명령어 팔레트 (템플릿 생성)
Cmd+O    = 빠른 스위처 (파일 검색)
Cmd+K    = 검색 (단어 찾기)
[[ 입력  = 자동 완성 (링크 생성)
```

### 마크다운 링크
```
[[SSOT]] = SSOT.md 링크
[[model-selection|모델 선택]] = 텍스트 다르게 표시
```

### 형식 규칙
```
담당자:    [이름]          (괄호 필수)
마감일:    YYYY-MM-DD      (날짜 형식)
결정:      ✅ [내용]        (체크마크)
액션:      [ ] **[이름]**   (체크박스 + 이름)
```

---

## ❓ 자주 하는 질문

**Q: SSOT가 뭔가요?**  
A: Single Source of Truth. 모든 규칙이 한 곳에만 정의되어 있습니다. [[02_SSOT_STRUCTURE.md]]

**Q: 회의록은 어디에?**  
A: Meetings/ 폴더. [[04_MEETING_HARNESS.md]] 참고.

**Q: 마감이 지난 액션이 있어요**  
A: [[06_DASHBOARD.md]]에서 확인하고, Owner에게 연락하세요.

**Q: SSOT를 수정하려면?**  
A: [[03_GOVERNANCE.md#변경-관리]]를 따르세요.

**Q: 과거 결정을 찾으려면?**  
A: Decisions/ 폴더 또는 Obsidian 검색 (Cmd+K).

---

## 🚀 다음 단계

1. **02_SSOT_STRUCTURE.md** 읽기 (15분)
2. **03_GOVERNANCE.md** 읽기 (10분)
3. **04_MEETING_HARNESS.md** 읽기 (30분) - 회의 진행하기 전에
4. **05_OBSIDIAN_SETUP.md** 따라하기 (30분) - 한 번만

---

**의문점이 있으신가요?** 
- Slack #ssot 채널에 질문하기
- 담당 Owner에게 직접 메시지
- [[03_GOVERNANCE.md]]에서 연락처 확인

**더 알아보기**: [[00_PROJECT_OVERVIEW.md|프로젝트 전체 개요]]
