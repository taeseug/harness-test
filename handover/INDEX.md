# Handover 문서 INDEX

**프로젝트**: LLM SSOT + Meeting Harness 1차 설계  
**완료일**: 2026-08-10  
**전체 파일**: 11개

---

## 📚 문서 구성

### 👋 시작하기 (필수)

| # | 파일 | 소요시간 | 목적 |
|---|------|---------|------|
| **00** | PROJECT_OVERVIEW.md | 2분 | 전체 개요 & 산출물 |
| **01** | QUICK_START.md | 5분 | 5분 빠른 시작 |
| **02** | SSOT_STRUCTURE.md | 15분 | SSOT 6가지 규칙 |

### 🏢 운영 가이드 (필수)

| # | 파일 | 소요시간 | 목적 |
|---|------|---------|------|
| **03** | GOVERNANCE.md | 10분 | 책임소재 & 의사결정 |
| **04** | MEETING_HARNESS.md | 30분 | 회의 자동화 상세 |
| **05** | OBSIDIAN_SETUP.md | 30분 | Obsidian 설정 |
| **06** | DASHBOARD.md | 5분 | 대시보드 활용 |

### 🔧 상세 가이드 (필요시)

| # | 파일 | 소요시간 | 목적 |
|---|------|---------|------|
| **07** | ACTION_TRACKING.md | 10분 | 액션 아이템 추적 |
| **08** | WORKFLOWS.md | 20분 | 상세 워크플로우 |
| **09** | CONFIG_REFERENCE.md | 참고용 | 설정값 참고 |
| **10** | TROUBLESHOOTING.md | 필요시 | 문제 해결 |

---

## 🎯 진행 경로별 읽기 순서

### 📖 신규자 온보딩 (50분)

```
1️⃣ 00_PROJECT_OVERVIEW (2분)
   └─ "이 프로젝트가 뭔지 알기"

2️⃣ 01_QUICK_START (5분)
   └─ "5분 안에 이해하기"

3️⃣ 02_SSOT_STRUCTURE (15분)
   └─ "6가지 규칙 배우기"

4️⃣ 03_GOVERNANCE (10분)
   └─ "책임자와 프로세스 이해"

5️⃣ 05_OBSIDIAN_SETUP (30분)
   └─ "Obsidian 한 번 설정하기"

↓

Day 2-3:
6️⃣ 04_MEETING_HARNESS (30분)
   └─ "회의 어떻게 하는지 배우기"

7️⃣ 이전 회의록 2-3개 읽기
   └─ "실제 사용 사례 보기"
```

### ⚡ 기존 팀원 (5-20분)

```
필요한 것만:
• 01_QUICK_START에서 시나리오 찾기
• 해당 문서 링크 따라가기
• 궁금하면 Owner에게 질문
```

### 🛠️ 운영자 (60분)

```
1️⃣ 00_PROJECT_OVERVIEW - 전체 이해
2️⃣ 01_QUICK_START - 신규자가 이해할 수 있는지 확인
3️⃣ 03_GOVERNANCE - 책임 구조 파악
4️⃣ 04_MEETING_HARNESS - 프로세스 이해
5️⃣ 05_OBSIDIAN_SETUP - 기술 설정 확인
6️⃣ 09_CONFIG_REFERENCE - 설정 옵션 검토
```

---

## 📍 주제별 찾기

### "SSOT가 뭔가요?"
→ **01_QUICK_START** (시나리오 1)  
→ **02_SSOT_STRUCTURE** (전체)

### "회의는 어떻게 진행하나요?"
→ **01_QUICK_START** (시나리오 2)  
→ **04_MEETING_HARNESS** (전체)

### "액션 아이템은?"
→ **01_QUICK_START** (시나리오 3)  
→ **07_ACTION_TRACKING** (전체)  
→ **06_DASHBOARD.md** (대시보드)

### "책임자가 누구죠?"
→ **03_GOVERNANCE.md** (Owner 목록)

### "Obsidian을 설정하려면?"
→ **05_OBSIDIAN_SETUP.md** (단계별)

### "문제가 생겼어요"
→ **10_TROUBLESHOOTING.md** (해결책)

### "설정값은?"
→ **09_CONFIG_REFERENCE.md** (참고)

---

## 💾 원본 파일 위치

모든 문서의 원본 & 더 자세한 내용:

```
/Users/mac/work/claude/20260810_harness/llm-ssot/
├─ README.md
├─ QUICK_START.md
├─ SSOT.md
├─ GOVERNANCE.md
├─ DASHBOARD.md
├─ OBSIDIAN_SETUP.md
├─ INTEGRATION_SUMMARY.md
│
├─ Meetings/
│  ├─ HARNESS.md (가장 상세함!)
│  ├─ HARNESS_CONFIG.yaml
│  ├─ _meeting-template.enhanced.md
│  └─ ACTION_ITEMS.md
│
└─ Decisions/
   └─ _decision-template.md
```

**Handover vs Original**:
- **Handover**: 간결, 요점, 신속하게 필요한 것만
- **Original**: 상세, 예시, 트러블슈팅 모두 포함

---

## ✅ 체크리스트

### 준비 단계
- [ ] 00_PROJECT_OVERVIEW 읽기 (진행 상황 파악)
- [ ] 파일 구조 확인 (이 INDEX로)
- [ ] 필요한 파일 선택

### 학습 단계
- [ ] 01_QUICK_START (핵심 5분)
- [ ] 02_SSOT_STRUCTURE (규칙 15분)
- [ ] 03_GOVERNANCE (책임 10분)

### 실행 단계
- [ ] 04_MEETING_HARNESS (프로세스 30분)
- [ ] 05_OBSIDIAN_SETUP (환경 구성 30분)
- [ ] 첫 회의 진행 (테스트)

### 추가 학습 (필요시)
- [ ] 07_ACTION_TRACKING (액션 추적)
- [ ] 08_WORKFLOWS (상세 워크플로우)
- [ ] 10_TROUBLESHOOTING (문제 해결)

---

## 📊 파일별 정보

```
00_PROJECT_OVERVIEW.md
  • 이 프로젝트가 뭔지
  • 산출물 요약
  • 아키텍처 개요
  • 다음 단계

01_QUICK_START.md
  • 30초 요약
  • 5가지 시나리오
  • 핵심 문서 링크
  • 신규자 체크리스트

02_SSOT_STRUCTURE.md
  • 6가지 핵심 규칙
  • 의사결정 트리
  • 실제 예시
  • 패턴 3가지

03_GOVERNANCE.md
  • Owner 목록
  • 책임 분담
  • RACI 매트릭스
  • 의사결정 프로세스
  • 변경 관리

04_MEETING_HARNESS.md
  • 회의 생명주기 (전→중→후)
  • 자동화 파이프라인
  • 템플릿 상세
  • 실제 예시

05_OBSIDIAN_SETUP.md
  • 플러그인 6개 설치
  • 자동 템플릿 설정
  • 자동 쿼리 (Dataview)
  • 색상 테마
  • 백업 & 동기화

06_DASHBOARD.md
  • 오늘 할일
  • 주간 현황
  • 빠른 링크
  • 통계 & 지표

07_ACTION_TRACKING.md
  • 액션 추출 규칙
  • 우선순위 분류
  • 상태 추적
  • Slack 리마인더

08_WORKFLOWS.md
  • 신규 프로젝트 플로우
  • 문제 해결 플로우
  • SSOT 업데이트 플로우

09_CONFIG_REFERENCE.md
  • HARNESS_CONFIG.yaml 상세
  • 플러그인별 설정
  • 단계별 설정값

10_TROUBLESHOOTING.md
  • 자주 하는 질문 (FAQ)
  • 문제별 해결책
  • 디버깅 팁
```

---

## 🎯 추천 학습 시간

```
신규자 온보딩
├─ 1시간 30분: 00 → 01 → 02 → 03 → 05
└─ 이후 필요시: 04, 06, 07

기존 팀원
├─ 5분: 필요한 시나리오만 01에서 찾기
└─ 10분: 해당 문서 읽기

운영자
├─ 2시간: 전체 이해 (00~09)
└─ 필요시: 10 참고
```

---

## 💡 효과적인 사용법

### 1. 스캔 (Scan)
```
먼저 필요한 파일의 목차(##)를 보고 
원하는 섹션을 찾아 읽기
```

### 2. 북마크 (Bookmark)
```
자주 보는 파일:
• 06_DASHBOARD.md - 매일
• 01_QUICK_START.md - 참고용
• 03_GOVERNANCE.md - 필요시
```

### 3. 링크 (Link)
```
이 파일(INDEX.md)에서
필요한 파일로 바로 이동 가능
```

### 4. 원본 참고 (Reference)
```
이해가 안 되면:
이 파일의 원본 위치 확인
(훨씬 더 자세함)
```

---

## 📞 지원

**질문 있을 때:**

1. **이 INDEX에서 찾기**
   - 주제별 찾기 사용

2. **해당 파일 읽기**
   - 대부분 10-30분 안에 해결

3. **원본 파일 참고**
   - 더 상세한 설명 필요시

4. **Owner에게 질문**
   - 03_GOVERNANCE.md에서 연락처 확인

5. **Slack #ssot**
   - 팀과 함께 논의

---

## 🚀 시작하기

**지금 바로:**

```
이 파일을 읽고 있다면
다음은 00_PROJECT_OVERVIEW.md를 읽으세요!

또는 필요한 주제를 직접 선택:
• 신규자? → 00 → 01 → 02
• 회의 있어? → 04
• 설정해야 해? → 05
• 문제있어? → 10
```

---

**업데이트**: 2026-08-10  
**버전**: 1.0.0

다음: [[00_PROJECT_OVERVIEW.md]]
