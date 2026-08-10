# LLM SSOT Vault

**LLM 엔지니어링의 Single Source of Truth**

Karpathy의 LLM wiki를 기반으로 한 중앙 집중식 규칙 및 회의록 관리 시스템.

---

## 🎯 목표

1. **SSOT (Single Source of Truth)**: 모든 LLM 규칙이 정확히 한 곳에서 관리됨
2. **회의록 추적**: 팀의 모든 의사결정이 기록되고 참조 가능
3. **책임 명확화**: 각 규칙의 소유자(Owner)와 책임자가 명확함
4. **진화 추적**: 왜, 언제, 누가 규칙을 바꿨는지 이력이 남음

---

## 📚 구조

### 핵심 문서

| 문서 | 목적 | 읽는 시간 |
|------|------|---------|
| [[QUICK_START.md]] | 5분 안에 전체 이해 | 5분 |
| [[SSOT.md]] | 모든 규칙의 중앙 정의 | 15분 |
| [[GOVERNANCE.md]] | 책임소재와 의사결정 프로세스 | 20분 |

### 주제별 상세 문서

| 주제 | 문서 | Owner | 최신화 |
|------|------|-------|--------|
| 모델 선택 | [[model-selection.md]] | [이름] | 2026-08-10 |
| 프롬프트 엔지니어링 | [[prompt-engineering.md]] | [이름] | 2026-08-10 |
| 추론 전략 | [[inference-strategy.md]] | [이름] | - |
| 평가 방법론 | [[evaluation.md]] | [이름] | - |
| 스케일링 법칙 | [[scaling-laws.md]] | [이름] | - |
| 에러 처리 | [[error-handling.md]] | [이름] | - |

### 팀 협업

| 폴더 | 목적 | 사용처 |
|------|------|--------|
| [[Meetings/]] | 회의록 | 팀이 매 회의마다 기록 |
| [[Decisions/]] | 의사결정 기록 | 주요 결정의 근거 저장 |

---

## 🚀 빠른 시작

### 신규자라면
1. [[QUICK_START.md]] 읽기 (5분)
2. [[SSOT.md]] 읽기 (15분)
3. 본인 담당 주제 문서 읽기
4. 팀 멘토와 1:1 (30분)

**소요시간**: 1시간

### 기존 팀원이라면
1. [[QUICK_START.md]] 에서 해당 시나리오 찾기
2. 연결된 문서 읽기
3. Owner와 상담

**소요시간**: 5-20분

### 규칙을 수정하려면
1. [[GOVERNANCE.md#변경-관리]] 읽기
2. Owner에게 제안
3. ADR 작성 (Type B 이상)
4. 팀 검토 및 승인

**소요시간**: 1-2주

---

## 📋 SSOT 항목 일람

```
🎯 SSOT (Single Source of Truth)
│
├─ 📌 모델 선택
│  ├─ Haiku 4.5 (경량 작업)
│  ├─ Sonnet 5 (균형)
│  └─ Opus 5 (복잡한 추론)
│
├─ 💬 프롬프트 엔지니어링
│  ├─ 명확성 우선
│  ├─ 구조화
│  ├─ 맥락 최소화
│  └─ 예제 포함
│
├─ 🔄 추론 전략
│  ├─ Temperature 설정
│  ├─ Batch processing
│  └─ 캐싱 전략
│
├─ 📊 평가 방법론
│  ├─ Rule-based (L1)
│  ├─ Reference-based (L2)
│  ├─ LLM-as-judge (L3)
│  └─ Human eval (L4)
│
├─ 📈 스케일링 법칙
│  └─ 성능 ∝ (크기^a) × (데이터^b)
│
└─ ⚠️ 에러 처리
   ├─ E1: 입력 검증
   ├─ E2: 모델 한계
   └─ E3: 시스템 에러
```

---

## 👥 조직 구조

```
SSOT 최고 책임자 (CTO/Tech Lead)
│
├─ Owner: 모델 선택 (+ 백업)
├─ Owner: 프롬프트 엔지니어링 (+ 백업)
├─ Owner: 추론 전략 (+ 백업)
├─ Owner: 평가 방법론 (+ 백업)
├─ Owner: 스케일링 법칙 (+ 백업)
└─ Owner: 에러 처리 (+ 백업)
   │
   └─ 팀 멤버: SSOT 준수, 피드백 제공
```

자세한 책임소재: [[GOVERNANCE.md#📌-책임-분담-raci]]

---

## 📅 정기 일정

### 월간 SSOT 리뷰 (1시간)
- **참석**: 전체 Owner + 기술리더
- **아젠다**:
  1. 지난달 변경사항
  2. 현안 issue
  3. 다음달 계획

### 분기별 SSOT 감사 (2시간)
- **참석**: 전체 팀
- **체크사항**: 최신성, 팀 준수도, 추가/제거 항목

### 팀 회의 (정기)
- 매주 or 격주
- [[Meetings/_meeting-template]] 사용
- [[Meetings/_agenda-from-previous]] 로 아젠다 생성

---

## 🔄 워크플로우

### SSOT 변경 프로세스

```
1️⃣ 문제/아이디어 발견
   └─ 팀 멤버 또는 Owner

2️⃣ 변경 제안
   └─ Owner에게 Slack/Email

3️⃣ 우선순위 분류
   ├─ Type A (긴급 24시간)
   ├─ Type B (일반 1-2주)
   └─ Type C (경미 즉시)

4️⃣ ADR 작성 (Type A/B)
   └─ [[Decisions/_decision-template]]

5️⃣ 팀 검토
   └─ 2-3일 피드백 수렴

6️⃣ 기술리더 승인
   └─ 최종 승인

7️⃣ 문서 업데이트
   └─ SSOT + 구체적 문서

8️⃣ 팀 공지
   └─ 회의 또는 Slack

9️⃣ 이력 기록
   └─ SSOT 변경 이력 섹션
```

자세히: [[GOVERNANCE.md#변경-관리]]

### 회의록 작성 프로세스

```
1️⃣ 회의 전
   └─ [[Meetings/_agenda-from-previous]] 로 아젠다 작성
   └─ 이전 회의록 검토

2️⃣ 회의 중
   └─ [[Meetings/_meeting-template]] 사용해서 기록
   └─ 의견, 결정, 행동항목 명확히

3️⃣ 회의 후
   └─ 파일 저장 (Meetings/YYYY-MM-DD_*.md)
   └─ [[SSOT]] "최근 회의록"에 링크 추가
   └─ 팀 Slack에 공지

4️⃣ SSOT 영향
   └─ 회의에서 SSOT 변경 결정시
   └─ ADR 작성 (Type B 이상)
   └─ SSOT 업데이트
```

---

## 📊 통계

| 지표 | 값 | 업데이트 |
|------|-----|---------|
| **SSOT 항목** | 6개 | 2026-08-10 |
| **회의록** | 1개 | 2026-08-10 |
| **ADR** | 0개 | - |
| **Owner** | 6명 | 입력 필요 |
| **팀 규모** | 10명 | 입력 필요 |

---

## ❓ FAQ

**Q: SSOT는 언제 수정하나요?**  
A: 월간 리뷰 + 필요시 즉시. [[GOVERNANCE.md]] 참고.

**Q: 회의록을 꼭 써야 하나요?**  
A: 네. 왜 결정했는지 이력이 남아야 미래에 참조 가능.

**Q: Owner가 아닌데 SSOT를 수정할 수 있나요?**  
A: 제안은 가능. Owner와 상담 후 Type별로 진행.

**Q: 과거 결정사항은 어디서 봐요?**  
A: `Decisions/ADR-*.md` 파일들. 왜 그렇게 결정했는지 모두 기록되어 있음.

**Q: SSOT가 팀 규칙과 충돌하면?**  
A: SSOT가 우선. 충돌이 있으면 GOVERNANCE.md의 의사결정 프로세스로 조율.

**더 많은 Q&A**: [[QUICK_START.md#자주하는-질문-faq]]

---

## 🔗 관련 자료

- **Karpathy의 LLM Engineering**: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- **Claude API**: https://docs.anthropic.com/en/docs/about-claude/models/model-selection
- **Prompt Engineering Guide**: https://platform.openai.com/docs/guides/prompt-engineering

---

## 📝 변경 이력

| 날짜 | 버전 | 변경사항 | 작성자 |
|------|------|---------|--------|
| 2026-08-10 | v1.0.0 | 초기 구조 수립 | Team |

---

## 🔧 회의 자동화 하네스 (NEW!)

**LLM SSOT에 완벽한 회의 관리 시스템이 통합되었습니다!**

### 📋 회의 하네스 구성

| 문서 | 목적 | 읽는 시간 |
|------|------|---------|
| [[Meetings/HARNESS.md]] | 회의 자동화 상세 가이드 | 30분 |
| [[Meetings/HARNESS_CONFIG.yaml]] | 자동화 설정 파일 | 참고용 |
| [[OBSIDIAN_SETUP.md]] | Obsidian 최적화 설정 | 30분 |
| [[DASHBOARD.md]] | Obsidian 대시보드 | 1분 |

### ⚙️ 회의 생명주기 (회의 전 → 중 → 후)

```
회의 생성 (자동화)
    ↓
아젠다 자동 생성 + 배경 자료 수집
    ↓
회의 진행 (템플릿 사용)
    ↓
회의록 자동 처리
    ├─ 요약 생성
    ├─ 액션 아이템 추출
    ├─ SSOT 영향 분석
    ├─ ADR 초안 생성
    ├─ SSOT 자동 업데이트
    └─ 팀 Slack 알림
    ↓
✅ 모든 문서 자동으로 연결됨
```

### 🔵 Obsidian 통합

완벽한 Obsidian 설정:
- ✅ **필수 플러그인**: Dataview, Templater, Breadcrumbs, Calendar, Checklist, Periodic Notes
- ✅ **자동 템플릿**: 회의록 & ADR 템플릿
- ✅ **자동 쿼리**: 액션 아이템, 회의록, ADR 자동 표시
- ✅ **대시보드**: [[DASHBOARD.md]] (Obsidian 대신 탭으로 고정)
- ✅ **그래프 뷰**: 모든 문서의 관계를 시각화

---

## 🚀 다음 단계

### 1단계: 기본 설정 (필수)

- [ ] Owner 이름 입력
  - [[GOVERNANCE.md]] 에서 주제별 Owner 작성
  - [[QUICK_START.md]] 에서 담당자 입력

- [ ] 팀과 공유
  - [[QUICK_START.md]] 링크를 팀 Slack에 공지
  - [[GOVERNANCE.md]] 에서 소유자 확인

### 2단계: Obsidian 설정 (권장)

- [ ] [[OBSIDIAN_SETUP.md|Obsidian 설정 가이드]] 따라하기
  - Vault 생성
  - 플러그인 6개 설치
  - 템플릿 설정
  
- [ ] [[DASHBOARD.md|대시보드]] Obsidian에 고정하기
  - 파일 탭 우클릭 → "탭 고정"

### 3단계: 첫 회의 진행

- [ ] 첫 회의 예약 ([[QUICK_START.md#-정기-일정]])
- [ ] [[Meetings/_meeting-template.enhanced.md|템플릿]] 또는 자동 생성 사용
- [ ] 회의록 작성
- [ ] 자동화 처리 확인 (`/claude meeting:process [파일명]`)

### 4단계: 의사결정 기록

- [ ] 첫 ADR 작성 [[Decisions/_decision-template.md]]
- [ ] ADR 상태 추적 ([[Decisions/ADR_STATUS.md]] 자동 생성됨)

---

## 📚 시작하기

**추천 순서**:

1. **1차**: [[QUICK_START.md]] (5분)
   → 전체 구조 이해

2. **2차**: [[SSOT.md]] (15분)
   → 모든 규칙 확인

3. **3차**: [[Meetings/HARNESS.md]] (30분)
   → 회의 자동화 상세

4. **4차** (옵션): [[OBSIDIAN_SETUP.md]] (30분)
   → Obsidian 최적화

5. **실행**: [[Meetings/_meeting-template.enhanced.md]]
   → 첫 회의 기록

**시작하기**: [[DASHBOARD.md|🎯 대시보드]]를 Obsidian에 고정하고 시작!

