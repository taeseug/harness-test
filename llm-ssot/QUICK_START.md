# LLM SSOT 빠른 시작 가이드

**목적**: LLM Vault의 구조, 사용법, 책임소재를 한눈에 이해하기  
**소요시간**: 5분  
**대상**: 팀 신규자, 기존 팀원

---

## 🚀 30초 요약

```
LLM SSOT는 LLM 엔지니어링의 중앙 규칙서입니다.

1️⃣ SSOT.md = 핵심 규칙 (여기서 시작)
2️⃣ 각 주제별 상세 문서 (필요할 때만)
3️⃣ Meetings/ = 회의록 (팀에서 관리)
4️⃣ Decisions/ = 의사결정 기록 (왜 이렇게 했는지)
5️⃣ GOVERNANCE.md = 책임소재 (누가 무엇을 관리)
```

---

## 📁 폴더 구조

```
llm-ssot/
│
├── SSOT.md                      ⭐ 여기서 시작!
│   (모든 규칙의 중앙 집중식 정의)
│
├── model-selection.md           📚 상세 문서
├── prompt-engineering.md
├── inference-strategy.md
├── evaluation.md
├── scaling-laws.md
├── error-handling.md
│
├── GOVERNANCE.md                👥 책임소재
│   (누가 뭘 관리하는가?)
│
├── Meetings/
│   ├── _meeting-template.md     📝 회의록 템플릿
│   ├── _agenda-from-previous.md 📋 아젠다 생성 가이드
│   └── 2026-08-10_meeting.md   📅 실제 회의록
│
├── Decisions/
│   ├── _decision-template.md    ✅ 의사결정 템플릿
│   └── ADR-001-...md            📌 실제 의사결정
│
├── QUICK_START.md               👋 이 파일
└── README.md                    📖 전체 개요
```

---

## 🎯 사용 시나리오별 가이드

### 시나리오 1: "모델을 선택해야 하는데 어떤 기준?"

```
1. SSOT.md 열기
   └─ "📌 모델 선택" 섹션 확인

2. model-selection.md 상세 읽기
   └─ 모델 비교표, 의사결정 트리, 비용 최적화 전략

3. 과거 결정 확인
   └─ ADR-001-model-selection 검색 (왜 이 모델을 선택했는가?)

4. 질문이 있으면
   └─ GOVERNANCE.md에서 Owner 찾기 ([이름])
```

### 시나리오 2: "프롬프트 작성 방법이 뭐야?"

```
1. SSOT.md 열기
   └─ "💬 프롬프트 엔지니어링" 섹션

2. prompt-engineering.md 읽기
   └─ 핵심 원칙, 3가지 패턴, 체크리스트

3. 다른 팀원의 사례 확인
   └─ Meetings에서 회의록 검색
   └─ 같은 문제를 어떻게 해결했나?

4. 피드백 원하면
   └─ Owner에게 Slack 메시지
```

### 시나리오 3: "팀 회의록을 작성해야 해"

```
1. Meetings/ 폴더 열기

2. _meeting-template.md 복사
   └─ 파일명: YYYY-MM-DD_meeting-topic.md 로 변경

3. 템플릿 작성
   ├─ 회의 정보 (날짜, 참석자, 주제)
   ├─ 안건별 논의 내용
   ├─ 결정사항
   ├─ 행동항목 (누가, 무엇을, 언제까지)
   └─ SSOT 영향

4. 저장 후
   └─ SSOT.md의 "최근 회의록" 섹션에 링크 추가
   └─ 팀 Slack에 공지

💡 팁: 다음 회의 아젠다는 Meetings/_agenda-from-previous.md 참조!
```

### 시나리오 4: "왜 이 방식으로 결정했지?"

```
1. Decisions/ 폴더 열기

2. 해당 ADR 파일 찾기
   └─ 예: ADR-001-model-selection.md

3. Context 섹션 읽기
   ├─ 왜 이 결정이 필요했나?
   ├─ 어떤 대안이 있었나?
   └─ 비교표 확인

4. Decision 섹션 읽기
   ├─ 최종 선택지
   ├─ 선택 이유
   └─ 우선순위

5. Consequences 섹션 읽기
   ├─ 예상 결과
   └─ 실제 결과 (시간 경과 후)
```

### 시나리오 5: "SSOT를 수정하고 싶은데?"

```
1. GOVERNANCE.md 열기
   └─ 해당 항목의 Owner 확인

2. Type별로 진행
   ├─ Type A (긴급) → 즉시 Owner와 상담
   ├─ Type B (일반) → Owner에게 제안, ADR 작성
   └─ Type C (경미) → Owner가 직접 수정

3. 변경 프로세스
   ├─ ADR 작성 (Type B 이상)
   ├─ 팀 검토 (2-3일)
   ├─ 기술리더 승인
   ├─ 문서 업데이트
   └─ 팀 공지

💡 더 자세히: [[GOVERNANCE.md#변경-관리]]
```

---

## 👥 책임소재 (책임자 이름 입력 필요)

### SSOT 최고 책임자 (CTO/Tech Lead)
**이름**: [입력 필요]  
**권한**: SSOT 전체 방향 결정, 최종 승인  
**연락처**: [Slack/Email]

### 주제별 Owner

| 주제 | Owner | 백업 | Slack |
|------|-------|------|-------|
| 모델 선택 | [이름] | [이름] | @owner1 |
| 프롬프트 엔지니어링 | [이름] | [이름] | @owner2 |
| 추론 전략 | [이름] | [이름] | @owner3 |
| 평가 방법론 | [이름] | [이름] | @owner4 |
| 스케일링 법칙 | [이름] | [이름] | @owner5 |
| 에러 처리 | [이름] | [이름] | @owner6 |

더 자세히: [[GOVERNANCE.md#📌-책임-분담-raci]]

---

## 📋 정기 일정

### 월간 SSOT 리뷰
- **일정**: [요일], [시간]
- **참석**: 전체 Owner + 기술리더
- **목적**: 지난달 변경사항, 현안 논의, 다음달 계획
- **Slack 채널**: #ssot-monthly

### 분기별 SSOT 감사
- **일정**: [분기], [일정]
- **참석**: 전체 팀
- **목적**: SSOT 최신성 확인, 필요한 항목 추가/제거
- **Slack 채널**: #ssot-quarterly

### 신규자 온보딩
- **일정**: 신입 입사 후 1주일 이내
- **소요시간**: 2시간
- **프로세스**:
  1. [[SSOT.md]] 읽기 (30분)
  2. 관련 주제별 문서 읽기 (1시간)
  3. 멘토와 1:1 (30분)

---

## ✅ 신규자 체크리스트

입사 후 하루 안에:

- [ ] QUICK_START.md 읽기 (5분)
- [ ] SSOT.md 읽기 (30분)
- [ ] 본인 담당 주제 문서 읽기 (1시간)
- [ ] Slack #ssot 채널 구독
- [ ] 멘토(Owner)와 1:1 예약

---

## 🔗 자주 찾는 링크

| 찾는 것 | 링크 |
|--------|------|
| 모든 규칙 | [[SSOT]] |
| 모델 선택 기준 | [[model-selection]] |
| 프롬프트 작성법 | [[prompt-engineering]] |
| 추론 최적화 | [[inference-strategy]] |
| 평가 방법 | [[evaluation]] |
| 과거 결정사항 | `Decisions/` 폴더 |
| 회의록 | `Meetings/` 폴더 |
| 책임자 | [[GOVERNANCE]] |

---

## 💬 자주하는 질문 (FAQ)

### Q1: SSOT가 뭔가요?
A: Single Source of Truth. 모든 LLM 규칙이 한 곳에만 정의되어 있고, 다른 곳에서는 그것을 참조합니다.

### Q2: 회의록은 어디에 저장하나요?
A: `Meetings/` 폴더. [[Meetings/_meeting-template]] 복사해서 사용.

### Q3: SSOT를 수정하려면 어떻게 하나요?
A: [[GOVERNANCE.md#변경-관리]] 참조. Owner에게 제안하면 됨.

### Q4: 과거 의사결정을 알고 싶으면?
A: `Decisions/` 폴더의 ADR 파일 확인. "왜" 그런 결정을 했는지 모두 기록되어 있음.

### Q5: Owner에게 질문하려면?
A: [[GOVERNANCE.md#책임-분담]]에서 해당 Owner 찾기 → Slack 메시지.

---

## 🎓 학습 경로

**Day 1 (신입 첫날)**
1. 이 문서 읽기 (5분)
2. [[SSOT.md]] 읽기 (30분)

**Day 2-3**
1. 본인 담당 주제 문서 읽기 (1시간)
2. 관련 Meetings 와 ADR 읽기 (1시간)
3. Owner와 1:1 (30분)

**Week 1-2**
1. 팀 회의 참석 (회의록 이해하기)
2. 간단한 SSOT 업데이트 제안해보기 (Type C)

**Month 1**
1. Owner 역할 이해하기
2. 월간 리뷰 미팅 참석
3. 첫 ADR 작성해보기

---

## 🚨 긴급 상황

### "모델이 갑자기 작동 안 해요"
→ [[error-handling]] 섹션 확인  
→ Owner에게 즉시 Slack 메시지

### "프롬프트가 자꾸 실패해요"
→ [[prompt-engineering]] 체크리스트 확인  
→ [[Meetings]] 에서 유사 사례 찾기

### "SSOT가 현실과 안 맞아요"
→ [[GOVERNANCE.md#변경-관리]] 참조  
→ Owner에게 제안 (Type B)

---

## 📞 연락처

| 상황 | 연락처 | 채널 |
|------|--------|------|
| 일반 질문 | 해당 Owner | Slack |
| 긴급 | 기술리더 | Slack + 전화 |
| SSOT 개선 제안 | SSOT 최고 책임자 | #ssot 채널 |

---

## 🎯 핵심 3가지

1. **SSOT.md = 시작점**  
   모든 규칙의 요약. 5분 안에 모든 원칙 파악 가능

2. **상세 문서 = 구현 가이드**  
   SSOT에서 링크된 각 주제별 문서. 실제로 "어떻게" 하는지 설명

3. **Meetings + Decisions = 이력 관리**  
   왜 이 규칙이 있는지, 언제 바뀌었는지, 누가 책임지는지 모두 기록

---

**다음 단계**: [[SSOT.md]] 를 열어서 5분간 읽기!

