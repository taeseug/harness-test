# 🎯 LLM SSOT + Meeting Harness 대시보드

> **팁**: 이 페이지를 Obsidian 대신 탭으로 고정하면 항상 시작점에서 시작할 수 있습니다.  
> (파일 탭 우클릭 → "탭 고정")

---

## 🚀 오늘 해야 할 일

### 📌 마감 임박 액션 아이템 (3일 이내)

```dataview
TABLE
  owner as "담당자",
  link(file.name) as "작업",
  deadline as "마감",
  status as "상태"
FROM "Meetings"
WHERE contains(file.name, "ACTION_ITEMS") AND deadline <= date(today) + dur(3 days)
SORT deadline ASC
```

**직접 추적**:
- [ ] [담당자] - [작업] - [마감]
- [ ] [담당자] - [작업] - [마감]
- [ ] [담당자] - [작업] - [마감]

---

### 📊 오늘의 회의

```dataview
TABLE
  time as "시간",
  topic as "주제",
  facilitator as "의장",
  link(file.name) as "보기"
FROM "Meetings"
WHERE date = date(today)
SORT time ASC
```

**예정된 회의가 없으면**: 예정된 회의 확인하기 [[SSOT.md#-정기-일정]]

---

## 📈 주간 현황

### ✅ 완료된 액션 (이번주)

```dataview
TABLE
  link(file.name) as "작업",
  date as "완료일",
  owner as "담당자"
FROM "Meetings"
WHERE contains(file.name, "ACTION_ITEMS") AND status = "✅ 완료" AND date >= date(today) - dur(7 days)
SORT date DESC
```

**통계**: [개수] 항목 완료

---

### ⏳ 진행 중인 액션

```dataview
TABLE
  owner as "담당자",
  link(file.name) as "작업",
  deadline as "마감",
  priority as "우선순위"
FROM "Meetings"
WHERE contains(file.name, "ACTION_ITEMS") AND status = "🔄 진행 중"
SORT deadline ASC
```

**통계**: [개수] 항목 진행 중

---

### 🚫 미완료 항목 (마감 지남)

```dataview
TABLE
  owner as "담당자",
  link(file.name) as "작업",
  deadline as "마감",
  "오버듀" as "상태"
FROM "Meetings"
WHERE contains(file.name, "ACTION_ITEMS") AND deadline < date(today) AND status != "✅ 완료"
SORT deadline ASC
```

**경고**: 마감이 지난 항목이 있습니다! [[Meetings/ACTION_ITEMS.md|상세 보기]]

---

## 📅 최근 회의록

```dataview
TABLE WITHOUT ID
  link(file.name, file.name) as "📅",
  topic as "주제",
  decisions as "결정",
  action_items as "액션",
  date as "날짜"
FROM "Meetings"
WHERE date AND !contains(file.name, "HARNESS") AND !contains(file.name, "ACTION_ITEMS") AND !contains(file.name, "_template")
SORT date DESC
LIMIT 5
```

**전체 회의록**: [[Meetings/]]

---

## 📌 최근 의사결정

### 검토 대기 중인 ADR

```dataview
TABLE WITHOUT ID
  link(file.name) as "📌",
  decision_type as "Type",
  created_date as "작성일",
  "⏳ 검토 중" as "상태"
FROM "Decisions"
WHERE status = "Draft" AND contains(file.name, "ADR")
SORT created_date DESC
```

**더 보기**: [[Decisions/]] → 상태별 필터링

### 최근 승인된 ADR

```dataview
TABLE WITHOUT ID
  link(file.name) as "📌",
  decision_type as "Type",
  created_date as "작성일",
  "✅ 승인됨" as "상태"
FROM "Decisions"
WHERE status = "Approved" AND contains(file.name, "ADR")
SORT created_date DESC
LIMIT 3
```

---

## 🎯 SSOT 상태

### 📊 SSOT 항목 요약

| 항목 | 상태 | 마지막 업데이트 | 소유자 |
|------|------|----------------|--------|
| [[model-selection\|📌 모델 선택]] | ✅ 최신 | 2026-08-17 | [이름] |
| [[prompt-engineering\|💬 프롬프트]] | ✅ 최신 | 2026-08-10 | [이름] |
| [[inference-strategy\|🔄 추론 전략]] | ⚠️ 검토 필요 | 2026-07-20 | [이름] |
| [[evaluation\|📊 평가 방법]] | ⚠️ 검토 필요 | 2026-07-15 | [이름] |
| [[scaling-laws\|📈 스케일링]] | ⚠️ 검토 필요 | 2026-06-30 | [이름] |
| [[error-handling\|⚠️ 에러 처리]] | ⚠️ 검토 필요 | 2026-06-15 | [이름] |

**전체 SSOT**: [[SSOT.md]]

### 📋 SSOT 변경 이력 (최근)

```dataview
TABLE
  date as "날짜",
  change_type as "유형",
  description as "변경사항",
  link(file.name) as "ADR"
FROM "Decisions"
WHERE contains(file.name, "ADR")
SORT date DESC
LIMIT 5
```

---

## 🔗 관련 정보

### 📚 핵심 문서

| 문서 | 설명 | 소요시간 |
|------|------|---------|
| [[QUICK_START.md\|🚀 빠른 시작]] | 5분 안에 전체 이해 | 5분 |
| [[SSOT.md\|📌 SSOT]] | 모든 규칙의 중앙 정의 | 15분 |
| [[GOVERNANCE.md\|👥 거버넌스]] | 책임소재와 의사결정 | 20분 |
| [[Meetings/HARNESS.md\|⚙️ 회의 하네스]] | 자동화 상세 가이드 | 30분 |
| [[OBSIDIAN_SETUP.md\|🔵 Obsidian 설정]] | Obsidian 최적화 | 30분 |

### 🎓 배우기

- [[QUICK_START.md#-학습-경로|신규자 학습 경로]]
- [[Meetings/HARNESS.md#-예시-모델-선택-기준-회의-개최|회의 완성 예시]]
- [[GOVERNANCE.md#-변경-관리|SSOT 변경 프로세스]]

### 👥 팀 정보

**SSOT 최고 책임자**: [이름]  
**기술리더**: [이름]  
**팀 규모**: [명]

**Owner 목록**: [[GOVERNANCE.md#책임-분담-raci]]

---

## 🛠️ 빠른 작업

### 새로운 회의 시작

```
1. 명령어 팔레트 (Cmd+P)
2. "Templater: Insert Template"
3. "meeting-new" 선택
4. 완료!

또는: [[Meetings/_meeting-template.enhanced.md|템플릿 복사]]
```

**필수 입력**:
- 날짜, 주제, 의장, 기록자, 참석자
- 아젠다, 논의 내용, 결정, 액션 아이템

### 새로운 ADR 시작

```
1. 명령어 팔레트 (Cmd+P)
2. "Templater: Insert Template"
3. "adr-new" 선택
4. 완료!

또는: [[Decisions/_decision-template.md|템플릿 복사]]
```

### SSOT 검색

```
검색창 (Cmd+K / Ctrl+K):
- "model" → [[model-selection.md|모델 선택]]
- "prompt" → [[prompt-engineering.md|프롬프트]]
- "evaluation" → 평가 방법
```

---

## 🔔 중요 이벤트

### 📅 정기 일정

| 행사 | 주기 | 다음 예정 | 비고 |
|------|------|---------|------|
| 📊 회의 | 주간 | [요일] | [[QUICK_START.md#-정기-일정]] |
| 🎯 월간 SSOT 리뷰 | 월간 | [날짜] | [[GOVERNANCE.md]] |
| 📈 분기 감사 | 분기 | [날짜] | [[GOVERNANCE.md]] |

---

## 📊 통계 & 지표

### 이번 달 활동

```dataview
TABLE WITHOUT ID
  "📋 회의" as "항목",
  rows.file.name as "통계"
FROM "Meetings"
WHERE date >= date(today) - dur(30 days) AND !contains(file.name, "HARNESS") AND !contains(file.name, "_template")
LIMIT 1
```

```
📊 지표:
- 회의 횟수: [개]
- 결정 수: [개]
- 액션 아이템: [개]
- 완료율: [%]

ADR:
- 작성됨: [개]
- 승인됨: [개]
- 진행 중: [개]
```

---

## ⚡ 빠른 링크

```
바로 가기:
- 🚀 [[QUICK_START.md|빠른 시작 가이드]]
- 📌 [[SSOT.md|SSOT 전체 보기]]
- 📅 [[Meetings/|회의록 폴더]]
- 📝 [[Decisions/|의사결정 기록]]
- ⚙️ [[Meetings/ACTION_ITEMS.md|액션 아이템 추적]]
- 👥 [[GOVERNANCE.md|책임소재 확인]]
```

---

## 💬 도움말 & FAQ

### 자주 하는 질문

**Q: 회의록은 어디에 저장하나요?**  
A: `Meetings/YYYY-MM-DD_주제.md` [[Meetings/|폴더 보기]]

**Q: 액션 아이템은 어떻게 추적하나요?**  
A: [[Meetings/ACTION_ITEMS.md|자동 추적됨]] (Dataview 사용)

**Q: SSOT를 수정하려면?**  
A: [[GOVERNANCE.md#변경-관리|변경 프로세스]] 확인

**Q: 마감이 지난 액션이 있어요**  
A: [[Meetings/ACTION_ITEMS.md|상세 보기]] → Owner에게 연락

**Q: 과거 회의록을 찾으려면?**  
A: 검색 (Cmd+K) 또는 [[Meetings/|Meetings 폴더]]

---

## 🎨 Obsidian 팁

**즐겨찾기에 추가**:
```
이 파일(DASHBOARD.md) 탭 우클릭
→ "즐겨찾기 추가"
→ 왼쪽 패널에서 항상 접근 가능
```

**빠른 탐색**:
- Cmd+P (명령어 팔레트)
- Cmd+O (빠른 스위처)
- Cmd+K (검색)

**우측 패널**:
- "역링크" 탭: 이 문서를 링크하는 모든 문서
- "아웃라인" 탭: 이 문서의 목차
- "태그" 탭: 태그별 정렬

---

## 📞 지원 & 피드백

**문제 또는 개선 제안**:
- Slack: [#ssot 채널]
- 이메일: [담당자]
- 회의: [[QUICK_START.md#-정기-일정|정기 SSOT 리뷰]]

**자세한 정보**:
- [[QUICK_START.md|빠른 시작 가이드]]
- [[Meetings/HARNESS.md|회의 하네스 상세]]
- [[OBSIDIAN_SETUP.md|Obsidian 설정]]

---

## ✨ 마지막 업데이트

**마지막 업데이트**: 2026-08-10  
**업데이트 내용**:
- ✅ SSOT + Meeting Harness 통합
- ✅ Obsidian 최적화 가이드 추가
- ✅ 자동 대시보드 설정

**다음 계획**:
- [ ] 첫 회의 진행 (2026-08-17)
- [ ] 회의 하네스 실제 테스트
- [ ] 피드백 수집 & 개선
- [ ] 팀 전체 공유

---

**🚀 준비 완료!** [[QUICK_START.md|빠른 시작 가이드]]에서 시작하세요.
