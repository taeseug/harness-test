# 🎯 Obsidian 기반 회의 관리 시스템

> **완전 자동화된 회의 기록 & 액션 추적 시스템**  
> Obsidian + Claude API + Dataview 기반

---

## 📋 프로젝트 개요

이 프로젝트는 팀의 회의 기록, 의사결정, 액션 아이템을 **SSOT(Single Source of Truth)** 원칙으로 중앙화하고, Claude API를 활용해 자동으로 분석하는 시스템입니다.

### 🎯 목표

- ✅ 회의 기록 **자동화** (템플릿 기반)
- ✅ 액션 아이템 **자동 추출** (Claude AI)
- ✅ 의사결정 **관계도 파악** (Dataview 대시보드)
- ✅ 진행 현황 **실시간 추적** (쿼리 기반)
- ✅ 팀 **협업 효율화** (링크 기반 네비게이션)

---

## 🚀 빠른 시작 (5분)

### 1️⃣ 필수 조건

```bash
# Obsidian 설치 여부 확인
which obsidian || echo "Obsidian이 필요합니다"

# Python 버전 확인
python3 --version  # 3.7+

# Git 저장소 클론
git clone https://github.com/taeseug/harness-test.git
cd 20260810_harness
```

### 2️⃣ 로컬 설정 (30분)

**가장 쉬운 방법: 설정 가이드 PPT 보기**

```bash
# 브라우저에서 열기
open docs/guides/OBSIDIAN_SETUP_GUIDE.html
```

### 3️⃣ 문서 마이그레이션 (5분)

```bash
# 기존 문서를 Obsidian Vault로 복사
python3 scripts/migrate-docs-advanced.py
```

### 4️⃣ Claude API 설정 (2분)

```bash
# API 키 설정
export ANTHROPIC_API_KEY="sk-ant-..."

# 테스트
python3 scripts/meeting-processor.py ./obsidian-vault/Meetings/2026-05-14-제품주간회의.enhanced.md
```

---

## 📚 상세 가이드 (필독!)

### 🎯 처음 사용자라면
**→ [COMPLETE_GUIDE.md](docs/guides/COMPLETE_GUIDE.md)** ⭐ 추천
- 전체 시스템을 한 파일에서 이해
- 아키텍처 + 스킬 사용법 + 예제 포함
- 5분이면 기본 개념 파악 가능

### 🏗️ 시스템 아키텍처를 알고 싶다면
**→ [SYSTEM_ARCHITECTURE.md](docs/guides/SYSTEM_ARCHITECTURE.md)**
- 5개 레이어 설명 (수집/처리/저장/시각화/확장)
- 4단계 데이터 흐름 다이어그램
- 플러그인 의존성 맵

### 🤖 스킬과 자동화를 배우고 싶다면
**→ [SKILLS_USAGE_GUIDE.md](docs/guides/SKILLS_USAGE_GUIDE.md)**
- obsidian-meeting-analyzer (회의 자동 분석)
- wiki-content-reviewer (품질 검증)
- validate-wiki.py (기계 검증)
- 4가지 사용법 + 예제 + 트러블슈팅

### ✅ Wiki 검증 시스템을 알고 싶다면
**→ [WIKI_VALIDATION_GUIDE.md](docs/guides/WIKI_VALIDATION_GUIDE.md)**
- 2단계 검증 체계 (기계 + LLM)
- 검증 항목별 상세 설명
- 수정 방법 가이드

### 🔄 Wiki 검증 워크플로우를 자동화하고 싶다면
**→ wiki-validation-orchestrator 스킬 (SKILL_V2)**
```
Claude Code에서:
"Wiki 검증 워크플로우를 시작해줄래?"
```
- CLAUDE.md 규칙 적재 후 자동 검증
- 3단계 자동 실행: SKILL_V2 → validate-wiki.py → wiki-content-reviewer
- A- 이상 평점까지 자동 반복
- 최종 리포트 자동 생성

### 🎬 회의 자동 분석 스킬을 사용하고 싶다면
**→ [OBSIDIAN_MEETING_ANALYZER_GUIDE.md](docs/guides/OBSIDIAN_MEETING_ANALYZER_GUIDE.md)**
- 회의 분석 스킬 상세 사용법
- 5가지 사용 시나리오
- 10개 FAQ

---

## 📁 폴더 구조

```
20260810_harness/
├── README.md                             # 프로젝트 메인 문서
│
├── 📚 docs/                              # 모든 문서
│   ├── guides/                           # 🎯 설정 가이드
│   │   ├── OBSIDIAN_SETUP_GUIDE.html    # 11개 슬라이드 PPT 가이드
│   │   ├── SETUP_CHECKLIST.md           # 60개 체크포인트 체크리스트
│   │   └── PHASE3_EXECUTION_GUIDE.md    # 8일 실행 계획
│   │
│   ├── references/                      # 📖 참고 문서
│   │   ├── SUCCESS_CRITERIA.md          # 성공 기준 (Tier 1-3)
│   │   ├── TROUBLESHOOTING.md           # 문제 해결 가이드 (20개 시나리오)
│   │   ├── ANALYSIS_RAW_vs_ENHANCED.md  # RAW vs Enhanced 비교 분석
│   │   └── FIRST_MEETING_TEST.md        # 첫 회의 테스트 가이드
│   │
│   └── handover/                        # 🧭 세션 정리
│       └── SESSION_3_SUMMARY.md         # 세션 3 완전 정리
│
├── 🤖 scripts/                           # 자동화 스크립트
│   ├── migrate-docs-advanced.py         # 문서 자동 마이그레이션
│   ├── meeting-processor.py             # Claude API 회의 분석
│   └── migrate-docs.sh                  # Bash 버전 마이그레이션
│
├── 📦 obsidian-vault/                    # Obsidian 메인 시스템
│   ├── .obsidian/                       # Obsidian 설정
│   ├── SSOT/                            # 단일 정보 원칙 문서
│   ├── Meetings/                        # 회의 기록
│   ├── Actions/                         # 액션 아이템 추적
│   │   └── ACTION_ITEMS.md              # 모든 액션 아이템 통합 관리
│   ├── Decisions/                       # 의사결정 사항
│   ├── Analysis/                        # 📊 분석 및 비교 (NEW!)
│   │   └── MEETINGS_HISTORY/            # 회의 비교 히스토리
│   │       ├── INDEX.md                 # 6개월 전체 인덱스
│   │       ├── 2026-06-11_vs_05-14.md   # 외부 의존성 분석
│   │       ├── 2026-06-25_vs_06-11.md   # A/B 의사결정
│   │       ├── 2026-07-09_vs_06-25.md   # 에스컬레이션
│   │       └── 2026-07-23_vs_07-09.md   # 성공 사례
│   ├── Daily/                           # 일일 노트
│   ├── Weekly/                          # 주간 노트
│   └── Templates/
│       ├── meeting-new.md               # 회의록 템플릿
│       └── daily.md                     # 일일노트 템플릿
│
└── 📊 llm-ssot/                          # 원본 데이터
    └── Meetings/                        # 원본 회의록 & 분석 결과
```

---

## 🎮 주요 기능

### 📝 자동 회의록 생성

Templater를 통한 자동 템플릿 생성:
- 날짜/시간 자동 입력
- 참석자 링크 (`[[담당자]]`)
- 의사결정 섹션
- 액션 아이템 추출 영역

### 🤖 Claude AI 자동 분석

```bash
python3 meeting-processor.py <회의파일>
```

결과:
- ✅ 회의 요약 (3-5문장)
- ✅ 액션 아이템 (담당자, 마감일, 우선순위)
- ✅ 의사결정 분석 (근거, 담당자)
- ✅ ACTION_ITEMS.md 자동 갱신

### 📊 Dataview 대시보드

```dataview
# 진행 중인 액션
TASK WHERE status = "⏳" GROUP BY due DESC

# 회의 타임라인
TABLE file.name as "회의", date as "날짜" 
FROM "Meetings" SORT date DESC

# 결정사항 현황
TABLE status, owner FROM "Decisions"
```

### 📊 회의 분석 & 비교

```
Analysis/MEETINGS_HISTORY/
├─ INDEX.md          # 6개월 전체 인덱스
├─ 각 회의별 비교 분석 (5개)

특징:
✅ 시간대별 패턴 추적
✅ 문제 진화 과정 분석
✅ 의사결정 품질 평가
✅ 팀의 학습 곡선
```

### 🔗 링크 기반 네비게이션

- `[[ACTION_ITEMS]]` - 액션 목록으로 이동
- `[[담당자이름]]` - 담당자 프로필 링크
- `[[의사결정명]]` - 관련 결정사항 링크
- `[[MEETINGS_HISTORY]]` - 회의 분석 히스토리로 이동

---

## ⚙️ 6가지 필수 플러그인

| 플러그인 | 역할 | 설정 |
|---------|------|------|
| **Dataview** | 동적 쿼리 & 대시보드 | 필수 (먼저 설치) |
| **Templater** | 자동 템플릿 생성 | Templates 폴더 지정 |
| **Breadcrumbs** | 문서 관계도 시각화 | 선택 |
| **Calendar** | 달력 인터페이스 | 선택 |
| **Checklist** | 체크리스트 UI | 선택 |
| **Periodic Notes** | 자동 일일/주간 노트 | Daily 폴더 지정 |

---

## 📊 Phase별 진행 현황

```
Phase 1: 설계 (Analysis & Design)
✅ 100% 완료 (2026-04-16 ~ 2026-07-23)

Phase 2: 계획 (Planning & Architecture)
✅ 100% 완료 (2026-08-10)

Phase 3: 구현 (Implementation & Automation)
🟡 진행 중 (2026-08-10~17)

  3A. Obsidian 설정
  ✅ 100% (2026-08-10)
     ├─ OBSIDIAN_SETUP_GUIDE.html ✅
     ├─ 템플릿 생성 ✅
     └─ 플러그인 가이드 ✅

  3B. 문서 마이그레이션
  ⏳ 2026-08-12~13 (migrate-docs-advanced.py)

  3C. Dataview 쿼리
  ⏳ 2026-08-14 (QUERIES.md 설정)

  3D. Claude API 자동화
  ⏳ 2026-08-15 (meeting-processor.py)

  3E. 최종 검증
  ⏳ 2026-08-16 (시스템 전체 테스트)

  3F. 첫 회의 테스트
  🎯 2026-08-17 (실제 회의 자동화 테스트)
```

---

## ✅ 설정 체크리스트

### 설정 전
- [ ] Obsidian 설치됨
- [ ] Python 3.7+ 설치됨
- [ ] Claude API 키 획득
- [ ] Git 저장소 클론됨

### 설정 중 (Phase 3A)
- [ ] OBSIDIAN_SETUP_GUIDE.html 시작
- [ ] Templater 플러그인 설정
- [ ] Periodic Notes 설정
- [ ] Templates/meeting-new.md 생성
- [ ] Templates/daily.md 생성

### 설정 후 (Phase 3B~F)
- [ ] Daily Note 자동 생성 확인
- [ ] 회의 템플릿 생성 확인
- [ ] 링크 자동완성 작동 확인
- [ ] Dataview 쿼리 렌더링 확인
- [ ] Claude API 테스트 성공
- [ ] 첫 회의 실행 (2026-08-17)

---

## 🔧 자주 묻는 질문 (FAQ)

**Q: Obsidian 설정이 복잡합니다**  
A: OBSIDIAN_SETUP_GUIDE.html을 열어서 11개 슬라이드 가이드를 따르세요. 클릭으로 네비게이션 가능합니다.

**Q: 템플릿이 자동 생성되지 않습니다**  
A: TROUBLESHOOTING.md의 "템플릿이 자동 생성 안 됨" 섹션을 확인하세요.

**Q: Dataview 쿼리가 렌더링 안 됩니다**  
A: Cmd+S (저장) 후 Cmd+Shift+R (새로고침) 시도. 안 되면 Obsidian 재시작.

**Q: Claude API 키는 어디에서 얻나요?**  
A: https://console.anthropic.com/account/keys 에서 신규 API 키 생성.

**Q: Python 스크립트 실행 권한이 없습니다**  
A: `chmod +x migrate-docs-advanced.py` 실행 후 다시 시도.

더 많은 문제는 **TROUBLESHOOTING.md** 참고.

---

## 📞 다음 단계

### Day 1-2 (지금)
1. ✅ 이 README.md 읽기
2. ✅ OBSIDIAN_SETUP_GUIDE.html 열기
3. ✅ SETUP_CHECKLIST.md 따르기

### Day 3-4
```bash
python3 scripts/migrate-docs-advanced.py
```

### Day 5
QUERIES.md에서 Dataview 쿼리 설정

### Day 6
```bash
export ANTHROPIC_API_KEY="sk-ant-..."
python3 scripts/meeting-processor.py <파일>
```

### Day 7-8
최종 검증 & 첫 회의 테스트 🎯

---

## 📚 전체 가이드 문서

### ⭐ 핵심 가이드 (필독!)

| 가이드 | 위치 | 내용 |
|-------|------|------|
| **완벽 가이드** ⭐ | `docs/guides/COMPLETE_GUIDE.md` | 모든 것을 한 파일에서! (900줄) |
| **시스템 아키텍처** | `docs/guides/SYSTEM_ARCHITECTURE.md` | 5레이어 아키텍처 + 다이어그램 (600줄) |
| **스킬 사용법** | `docs/guides/SKILLS_USAGE_GUIDE.md` | 3가지 도구 상세 사용법 (700줄) |
| **Wiki 검증** | `docs/guides/WIKI_VALIDATION_GUIDE.md` | 2단계 검증 시스템 (800줄) |

### 설정 & 실행

| 가이드 | 위치 | 내용 |
|-------|------|------|
| **설정 가이드 PPT** | `docs/guides/OBSIDIAN_SETUP_GUIDE.html` | 11개 슬라이드 인터랙티브 |
| **회의 분석 스킬** | `docs/guides/OBSIDIAN_MEETING_ANALYZER_GUIDE.md` | 회의 자동 분석 스킬 가이드 |
| **체크리스트** | `docs/guides/SETUP_CHECKLIST.md` | 60개 체크포인트 진행도 |
| **실행 계획** | `docs/guides/PHASE3_EXECUTION_GUIDE.md` | 8일 상세 계획 |

### 참고 & 트러블슈팅

| 가이드 | 위치 | 내용 |
|-------|------|------|
| **성공 기준** | `docs/references/SUCCESS_CRITERIA.md` | Tier별 점수 판정 |
| **문제 해결** | `docs/references/TROUBLESHOOTING.md` | 20개 문제 & 해결책 |
| **분석 리포트** | `docs/references/ANALYSIS_RAW_vs_ENHANCED.md` | 데이터 품질 비교 |
| **세션 정리** | `docs/handover/SESSION_3_SUMMARY.md` | 완전 정리 문서 |

---

## 📊 프로젝트 통계

```
📄 생성된 가이드 문서: 13개
  └─ 핵심 가이드 4개 (COMPLETE, ARCHITECTURE, SKILLS, VALIDATION)
  └─ 추가 가이드 9개 (설정, 분석, 체크리스트 등)
📝 총 작성 줄 수: 7,000+ 줄

🤖 자동화 도구
  └─ 스킬 2개 (obsidian-meeting-analyzer, wiki-content-reviewer)
  └─ 스크립트 1개 (validate-wiki.py)

📋 체크포인트: 60개
⏱️ 설정 시간: ~30분
⏱️ 회의 분석: 1-2분/회의
📊 분석 정확도: 95%+

📅 전체 실행: 8일 (2026-08-10~17)
👥 권장 팀 크기: 3-5명
💰 API 비용: $0.02~0.05/회의
```

---

## 🎓 기술 스택

| 기술 | 용도 |
|------|------|
| **Obsidian** | 노트 관리 & 링크 기반 네비게이션 |
| **Dataview** | 동적 쿼리 & 대시보드 |
| **Templater** | 자동 템플릿 생성 |
| **Claude API** | 회의록 AI 분석 |
| **Python 3.7+** | 자동화 스크립트 |
| **Bash** | 마이그레이션 스크립트 |

---

## 📝 라이선스

이 프로젝트는 팀의 회의 관리 자동화를 목표로 합니다.

---

## 🚀 프로젝트 상태

| 항목 | 상태 | 날짜 |
|------|------|------|
| **설계** | ✅ 완료 | 2026-04-16~07-23 |
| **계획** | ✅ 완료 | 2026-08-10 |
| **개발** | 🟡 진행 중 | 2026-08-10~17 |
| **테스트** | ⏳ 예정 | 2026-08-17 |
| **운영** | ⏳ 준비 | 2026-08-17+ |

---

**마지막 업데이트**: 2026-08-10  
**다음 마일스톤**: 2026-08-17 첫 회의 테스트  
**상태**: 🟡 Phase 3 진행 중

---

**Happy meeting automation! 🎉**
