# 📍 프로젝트 맵 (전체 구조)

**생성일**: 2026-08-10  
**상태**: Phase 1 + Safety Design 완료  
**다음**: Phase 2 시작

---

## 🗺️ 폴더 구조

```
/Users/mac/work/claude/20260810_harness/
│
├── 📋 핵심 문서들
│   ├── SAFETY_DESIGN.md           ⭐ 필독! (안전 설계)
│   ├── DELIVERY_SUMMARY.md        ⭐ 최종 요약
│   ├── PHASE1_COMPLETION.md       ✅ Phase 1 완료
│   └── PROJECT_MAP.md             👈 이 파일
│
├── 📚 handover/ (1차 설계)
│   ├── 00_PROJECT_OVERVIEW.md     (프로젝트 개요)
│   ├── 01_QUICK_START.md          (5분 빠른 시작)
│   ├── 02_SSOT_STRUCTURE.md       (SSOT 구조)
│   ├── 03_GOVERNANCE.md           (거버넌스 & 책임소재)
│   ├── 04_MEETING_HARNESS.md      (회의 하네스)
│   ├── INDEX.md                   (목차)
│   ├── README.md                  (설명서)
│   └── HANDOVER_SUMMARY.md        (요약)
│
├── 🔧 implementation/ (Phase 1 구현)
│   ├── 00_IMPLEMENTATION_PLAN.md  (구현 계획)
│   ├── 01_PHASE1_SUMMARY.md       (Phase 1 상세)
│   ├── 02_SAFETY_IMPLEMENTATION.md (안전 설계 구현)
│   ├── requirements.txt           (의존성)
│   │
│   ├── engines/
│   │   ├── __init__.py
│   │   ├── meeting_engine.py      (회의 자동화)
│   │   ├── ssot_engine.py         (SSOT 관리)
│   │   └── [Phase 2]
│   │       ├── adr_engine.py      (의사결정)
│   │       └── notification_engine.py (알림)
│   │
│   ├── cli/
│   │   ├── harness.py             (메인 CLI)
│   │   ├── commands/              (명령어, Phase 2)
│   │   └── config/                (설정, Phase 2)
│   │
│   ├── operations/                (팀 운영, Phase 3)
│   │   ├── 01_DAILY_GUIDE.md
│   │   ├── 02_MEETING_LIFECYCLE.md
│   │   ├── 03_FAQ_TROUBLESHOOTING.md
│   │   ├── 04_ONBOARDING.md
│   │   └── 05_SCENARIOS.md
│   │
│   ├── docs/                      (문서, Phase 3)
│   │   ├── INSTALLATION.md
│   │   ├── DASHBOARD.md
│   │   ├── API_REFERENCE.md
│   │   └── TROUBLESHOOTING.md
│   │
│   └── tests/                     (테스트, Phase 4)
│       ├── test_meeting_engine.py
│       ├── test_ssot_engine.py
│       └── test_cli.py
│
├── 📁 llm-ssot/ (실제 SSOT Vault)
│   ├── SSOT.md                    (핵심 규칙)
│   ├── model-selection.md
│   ├── prompt-engineering.md
│   ├── (나머지 SSOT 문서들)
│   │
│   ├── Meetings/                  (회의록)
│   │   ├── _meeting-template.md
│   │   ├── _agenda-from-previous.md
│   │   └── [실제 회의록들]
│   │
│   └── Decisions/                 (의사결정)
│       ├── _decision-template.md
│       └── [실제 ADR들]
│
└── 📊 (기타)
    ├── .git/                      (버전 관리)
    └── .backup/                   (자동 백업)
```

---

## 🎯 읽기 순서

### 👤 신규 팀원 (1시간)
```
1️⃣ DELIVERY_SUMMARY.md (5분)
   → 전체 개요 파악

2️⃣ handover/00_PROJECT_OVERVIEW.md (5분)
   → 프로젝트 이해

3️⃣ handover/01_QUICK_START.md (5분)
   → 빠른 시작

4️⃣ SAFETY_DESIGN.md (20분)
   → 핵심 원칙 학습

5️⃣ handover/03_GOVERNANCE.md (10분)
   → 책임소재 확인

6️⃣ 첫 회의 진행!
```

### 👨‍💻 개발자 (2시간)
```
1️⃣ DELIVERY_SUMMARY.md (10분)

2️⃣ implementation/00_IMPLEMENTATION_PLAN.md (20분)

3️⃣ SAFETY_DESIGN.md (20분)

4️⃣ implementation/02_SAFETY_IMPLEMENTATION.md (30분)

5️⃣ 엔진 코드 검토 (30분)
   - meeting_engine.py
   - ssot_engine.py

6️⃣ CLI 테스트 (10분)
```

### 📊 운영자 (1.5시간)
```
1️⃣ handover/04_MEETING_HARNESS.md (20분)

2️⃣ SAFETY_DESIGN.md (20분)

3️⃣ implementation/02_SAFETY_IMPLEMENTATION.md (20분)

4️⃣ CLI 명령어 학습 (10분)

5️⃣ 월간 리뷰 준비 (10분)
```

---

## 📝 주요 문서 요약

### SAFETY_DESIGN.md ⭐ 필독
**핵심**: Raw = SSOT, 최소 프론트매터, 상태는 후속 회의에서만

| 항목 | 내용 |
|------|------|
| Raw | 회의록 파일 (진실의 원천) |
| Wiki | 자동 생성 (파생물, 읽기 전용) |
| 포맷 | 프론트매터만 강제 |
| 상태 | 후속 회의에서만 변경 |
| Owner | 6명 (주제별) |

### DELIVERY_SUMMARY.md
**내용**: 최종 납품 내용, 아키텍처, 사용 시나리오

### PHASE1_COMPLETION.md
**내용**: Phase 1 구현 완료, 테스트 방법, 성능 지표

### implementation/02_SAFETY_IMPLEMENTATION.md
**내용**: 안전 설계를 구현하는 구체적인 코드 가이드

---

## 🔧 사용 명령어

### 첫 회의 생성
```bash
cd implementation
python3 cli/harness.py meeting:create \
    --date 2026-08-20 \
    --title "팀 회의" \
    --participants Alice Bob
```

### 회의록 처리
```bash
python3 cli/harness.py meeting:process \
    /path/to/meeting.md
```

### 상태 확인
```bash
python3 cli/harness.py status
python3 cli/harness.py action-items
```

---

## 📊 단계별 완성도

| 단계 | 목표 | 달성도 | 상태 |
|------|------|--------|------|
| **1차 설계** | SSOT 구조 | 100% | ✅ 완료 |
| **Phase 1** | 기초 엔진 & CLI | 90% | ✅ 완료 |
| **Safety Design** | 안전 원칙 | 100% | ✅ 완료 |
| **Phase 2** | 자동화 완성 | 0% | 🔜 예정 |
| **Phase 3** | 팀 매뉴얼 | 0% | 🔜 예정 |
| **Phase 4** | 테스트 & 배포 | 0% | 🔜 예정 |

---

## 🎯 다음 단계

### 이번 주 (Week 1)
- [ ] 팀과 SAFETY_DESIGN.md 공유
- [ ] 첫 회의 준비
- [ ] 회의록 포맷 확정

### 다음 주 (Week 2-3)
- [ ] Phase 2 구현 시작
- [ ] 엔진 안전화
- [ ] 자동화 완성

### 2주 후 (Week 4+)
- [ ] 팀 운영 매뉴얼 작성
- [ ] 첫 팀 리뷰
- [ ] 개선 반영

---

## 📞 문의처

### 문제 발생
1. SAFETY_DESIGN.md 확인
2. implementation/02_SAFETY_IMPLEMENTATION.md 참고
3. 팀과 논의 (회의)

### 개선 제안
1. 월간 리뷰 미팅
2. Slack 논의
3. 다음 Phase에 반영

---

## ✅ 최종 체크리스트

설계 단계:
- [x] SSOT 원칙 확정
- [x] 안전 설계 완성
- [x] 책임소재 명확화

구현 단계:
- [x] Phase 1 완료
- [ ] Phase 2 (안전화)
- [ ] Phase 3 (매뉴얼)
- [ ] Phase 4 (테스트)

운영 단계:
- [ ] 팀과 공유
- [ ] 첫 회의 진행
- [ ] 월간 리뷰
- [ ] 지속적 개선

---

**모두 준비됐습니다!**

지금 시작하세요:
1. `SAFETY_DESIGN.md` 읽기
2. `handover/01_QUICK_START.md` 따라하기
3. 첫 회의 진행!

