# 2차 구현 계획서

**버전**: v2.0.0  
**시작일**: 2026-08-10  
**목표**: 회의 자동화 엔진 + 팀 운영 매뉴얼 + CLI 도구 완성

---

## 🎯 2차 구현의 목표

### Before (1차 설계)
```
✅ SSOT 구조 수립
✅ 회의록 템플릿 정의
✅ 책임소재 명확화
❌ 자동화 미구현
❌ 팀 운영 가이드 미작성
❌ CLI 도구 없음
```

### After (2차 구현)
```
✅ SSOT 구조 수립
✅ 회의록 템플릿 정의
✅ 책임소재 명확화
✅ 회의 자동화 엔진 완성
✅ 팀 운영 매뉴얼 작성
✅ CLI 도구 배포
✅ 즉시 운영 가능
```

---

## 📦 2차 구현 4개 영역

### 영역 1️⃣: 회의 자동화 엔진

**목표**: "회의 끝 → 자동으로 모든 처리"

| 기능 | 담당 | 소요시간 |
|------|------|---------|
| 회의 자동 생성 | Engine | 30분 |
| 회의록 자동 처리 | Engine | 1시간 |
| SSOT 자동 업데이트 | Engine | 1시간 |
| ADR 자동 생성 | Engine | 45분 |
| 팀 자동 알림 | Engine | 30분 |

**구현**: Python 또는 Node.js 스크립트

---

### 영역 2️⃣: 팀 운영 매뉴얼

**목표**: "팀이 이 문서만 보고 운영 가능"

| 섹션 | 상세 | 대상 |
|------|------|------|
| 일일 운영 가이드 | 매일 해야 할 일 | 모든 팀원 |
| 회의 생명주기 | 회의 전/중/후 | 의장/기록자 |
| 문제 해결 (FAQ) | 자주하는 실수 | 모든 팀원 |
| 온보딩 체크리스트 | 신입 교육 | 신입/멘토 |
| 시나리오별 가이드 | "~하려면 이렇게" | 상황별 |

---

### 영역 3️⃣: CLI 도구 & 스크립트

**목표**: "터미널에서 한 줄 커맨드로 완성"

```bash
# 회의 생성
harness meeting:create --date 2026-08-17 --topic "모델 선택 논의"

# 회의록 처리 (자동으로 아젠다 생성, 요약, ADR 초안, Slack 알림)
harness meeting:process /path/to/meeting.md

# SSOT 업데이트
harness ssot:update model-selection --version v1.0.1

# 상태 확인
harness status --dashboard

# 리포트 생성
harness report --period monthly
```

---

### 영역 4️⃣: 통합 문서

**목표**: "전체 시스템이 한눈에 보임"

| 문서 | 내용 |
|------|------|
| 설치 가이드 | 1. 폴더 생성, 2. 스크립트 배포, 3. 설정, 4. 테스트 |
| 운영 대시보드 | 실시간 상태, 액션 아이템, 회의 일정 |
| 트러블슈팅 | "~이 안 돼요" 문제별 해결법 |
| 마이그레이션 가이드 | 기존 팀에서 이 시스템으로 전환 |

---

## 📅 구현 일정 (예상 5-7일)

```
Day 1: 회의 자동화 엔진 설계 & 첫 번째 모듈 구현
Day 2: 자동화 엔진 완성
Day 3: 팀 운영 매뉴얼 작성
Day 4: CLI 도구 개발
Day 5: 통합 테스트 & 문서 완성
Day 6-7: 팀 리뷰 & 개선
```

---

## 🔧 기술 스택 결정

### 옵션 1: Python (추천)
**장점**:
- Claude API SDK 최적화
- 스크립트 작성 용이
- 자동화 라이브러리 풍부 (schedule, slack-sdk, etc.)

**단점**:
- Python 환경 필요

### 옵션 2: Node.js
**장점**:
- CLI 도구 개발 쉬움 (commander, chalk)
- 크로스 플랫폼

**단점**:
- 번들 크기가 큼

### 결정: **Python** (1차로 Python, 나중에 Node.js 옵션 추가)

---

## 📊 성공 지표

| 지표 | 목표 | 측정 |
|------|------|------|
| **자동화율** | 회의록 작성 시간 80% 단축 | 수동 vs 자동화 시간 비교 |
| **팀 채택율** | 80% 팀원이 사용 | 사용량 통계 |
| **에러율** | 자동화 실패 < 5% | 실패 로그 분석 |
| **만족도** | NPS > 7 | 팀 설문조사 |

---

## 🎯 핵심 성과물

### 완성 후 결과물

```
/implementation/
├── engines/
│   ├── meeting_engine.py      # 회의 생성/처리
│   ├── ssot_engine.py         # SSOT 자동 업데이트
│   ├── adr_engine.py          # ADR 자동 생성
│   └── notification_engine.py # Slack/Email 알림
│
├── cli/
│   ├── harness.py             # 메인 CLI (entry point)
│   ├── commands/
│   │   ├── meeting.py
│   │   ├── ssot.py
│   │   ├── adr.py
│   │   └── report.py
│   └── config/
│       ├── default.yaml
│       └── hooks.yaml
│
├── operations/
│   ├── 01_DAILY_GUIDE.md      # 일일 운영 가이드
│   ├── 02_MEETING_LIFECYCLE.md # 회의 생명주기
│   ├── 03_FAQ_TROUBLESHOOTING.md
│   ├── 04_ONBOARDING.md       # 신입 온보딩
│   └── 05_SCENARIOS.md        # 상황별 가이드
│
├── docs/
│   ├── INSTALLATION.md         # 설치 가이드
│   ├── DASHBOARD.md           # 운영 대시보드
│   ├── API_REFERENCE.md       # CLI 명령어 레퍼런스
│   └── TROUBLESHOOTING.md     # 트러블슈팅
│
└── tests/
    ├── test_meeting_engine.py
    ├── test_ssot_engine.py
    └── test_cli.py
```

---

## 🔄 구현 순서

### Phase 1: 기초 (Day 1-2)
1. 프로젝트 구조 생성
2. 회의 자동화 엔진 (meeting_engine.py)
   - 회의 메타데이터 파싱
   - 아젠다 자동 생성
   - 회의록 템플릿 자동 생성
3. 기본 CLI (harness.py)

### Phase 2: 확장 (Day 3)
1. SSOT 자동화 엔진 (ssot_engine.py)
2. ADR 자동화 엔진 (adr_engine.py)
3. 알림 엔진 (notification_engine.py)

### Phase 3: 운영 (Day 4-5)
1. 팀 운영 매뉴얼 작성
2. CLI 명령어 완성
3. 설치 가이드 & 대시보드

### Phase 4: 검증 (Day 6-7)
1. 통합 테스트
2. 팀 리뷰
3. 개선 & 배포

---

## 📋 체크리스트

### 영역별 산출물 체크리스트

#### 회의 자동화 엔진 ✅
- [ ] meeting_engine.py 완성
- [ ] ssot_engine.py 완성
- [ ] adr_engine.py 완성
- [ ] notification_engine.py 완성
- [ ] 단위 테스트 (>80% 커버리지)

#### 팀 운영 매뉴얼 ✅
- [ ] 01_DAILY_GUIDE.md
- [ ] 02_MEETING_LIFECYCLE.md
- [ ] 03_FAQ_TROUBLESHOOTING.md
- [ ] 04_ONBOARDING.md
- [ ] 05_SCENARIOS.md

#### CLI 도구 & 스크립트 ✅
- [ ] harness.py (메인)
- [ ] commands/meeting.py
- [ ] commands/ssot.py
- [ ] commands/adr.py
- [ ] commands/report.py
- [ ] CLI 헬프 텍스트 작성

#### 통합 문서 ✅
- [ ] INSTALLATION.md
- [ ] DASHBOARD.md
- [ ] API_REFERENCE.md
- [ ] TROUBLESHOOTING.md
- [ ] README.md

---

## 🚀 다음 스텝

👉 **지금 바로 Phase 1 시작:**

1. 폴더 구조 생성
2. 회의 자동화 엔진 첫 번째 모듈 구현
3. 기본 CLI 프로토타입

준비되셨으면 시작하겠습니다!

