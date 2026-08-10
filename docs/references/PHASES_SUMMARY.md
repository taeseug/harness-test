# 📊 Phase별 상세 설명

> **프로젝트**: Obsidian 기반 회의 관리 시스템  
> **기간**: 2026-04-16 ~ 2026-08-17 (4개월)  
> **현황**: Phase 3A-D 완료, 3E-F 진행 중

---

## Phase 1: 설계 (Design & Analysis)

### 기간
2026-04-16 ~ 2026-07-23 (약 3개월)

### 목표
팀의 회의 관리 시스템이 어떻게 작동해야 하는지 설계

### 주요 활동
```
1️⃣ 6개월 회의 기록 분석
   └─ 2026-04-16 ~ 2026-07-23 회의 6개
   └─ 각 회의의 액션, 의사결정 분석

2️⃣ 시스템 요구사항 정의
   └─ Single Source of Truth (SSOT) 원칙
   └─ 회의 기록, 액션 추적, 의사결정 관리

3️⃣ 기술 스택 선정
   └─ Obsidian (노트 관리)
   └─ Dataview (동적 쿼리)
   └─ Claude API (AI 분석)
   └─ Python (자동화)

4️⃣ 아키텍처 설계
   └─ 5개 레이어: 수집 → 처리 → 저장 → 시각화 → 확장
   └─ 데이터 흐름 및 의존성 맵
```

### 산출물
```
📋 6개월 회의 데이터 분석
   ├─ 6개 회의 파일 (.enhanced.md)
   ├─ 17개 액션 아이템
   ├─ 2개 주요 의사결정
   └─ 회의별 분석 리포트

📖 시스템 아키텍처 문서
   ├─ SYSTEM_ARCHITECTURE.md (600줄)
   ├─ 데이터 흐름 다이어그램
   └─ 플러그인 의존성 맵
```

### 완료 상태
✅ **100% 완료** (2026-07-23)

---

## Phase 2: 계획 (Planning & Architecture)

### 기간
2026-08-10 (1일)

### 목표
Phase 1의 설계를 어떻게 구현할지 상세 계획

### 주요 활동
```
1️⃣ 구현 계획 수립
   └─ Phase 3: 6개 하위 단계로 분해
   └─ 각 단계의 목표, 산출물, 완료 기준 정의

2️⃣ 기술 검증
   └─ Obsidian 플러그인 호환성
   └─ Dataview 쿼리 문법
   └─ Claude API 호출 방식

3️⃣ 문서화 계획
   └─ 가이드 13개 (완벽 가이드, 아키텍처, 스킬 등)
   └─ 체크리스트 60개
   └─ 트러블슈팅 20개 시나리오

4️⃣ CLAUDE.md 규칙 정의
   └─ Phase별 진행 순서
   └─ Wiki 검증 워크플로우
   └─ 커밋 메시지 형식
```

### 산출물
```
📋 상세 계획 문서
   ├─ PHASE3_EXECUTION_GUIDE.md (8일 상세 계획)
   ├─ SETUP_CHECKLIST.md (60개 체크포인트)
   └─ CLAUDE.md (프로젝트 규칙)

🛠️ 개발 환경
   ├─ GitHub 저장소 설정
   ├─ Python 스크립트 프레임워크
   └─ Git workflow 정의
```

### 완료 상태
✅ **100% 완료** (2026-08-10)

---

## Phase 3: 구현 & 검증 (Implementation & Validation)

### 기간
2026-08-10 ~ 2026-08-17 (1주일)

### 전체 목표
Obsidian 기반 회의 관리 시스템 완성 & 첫 회의 테스트

---

## 📍 Phase 3A: Obsidian 설정

### 기간
2026-08-10 (1일)

### 목표
Obsidian 플러그인 설치 및 템플릿 구성

### 주요 활동
```
1️⃣ 플러그인 설치 (6개)
   ├─ Dataview (동적 쿼리)
   ├─ Templater (자동 템플릿)
   ├─ Breadcrumbs (관계도)
   ├─ Calendar (달력)
   ├─ Checklist (체크리스트)
   └─ Periodic Notes (일일/주간 노트)

2️⃣ 템플릿 생성
   ├─ Templates/meeting-new.md
   │  └─ 날짜 자동 입력, 참석자 링크, 액션 섹션
   └─ Templates/daily.md
      └─ 일일 노트 자동 템플릿

3️⃣ 폴더 구조 설정
   ├─ Meetings/ (회의 기록)
   ├─ Actions/ (액션 아이템)
   ├─ Decisions/ (의사결정)
   ├─ Analysis/ (분석)
   └─ Templates/ (템플릿)

4️⃣ 설정 가이드 작성
   ├─ OBSIDIAN_SETUP_GUIDE.html (11개 슬라이드 PPT)
   └─ 인터랙티브 가이드 (클릭으로 단계 진행)
```

### 산출물
```
✅ 플러그인 설치 완료 (6개)
✅ Templates/meeting-new.md
✅ Templates/daily.md
✅ OBSIDIAN_SETUP_GUIDE.html (11개 슬라이드)
✅ 폴더 구조 생성
```

### 완료 상태
✅ **100% 완료** (2026-08-10)

---

## 📍 Phase 3B: Wiki 검증 워크플로우

### 기간
2026-08-10 (1일)

### 목표
AI 기반 자동 검증 시스템 구축

### 주요 활동
```
1️⃣ Wiki 검증 오케스트레이터 개발 (SKILL_V2)
   ├─ Step 1: CLAUDE.md 규칙 확인
   ├─ Step 2: 기계 검증 (validate-wiki.py)
   └─ Step 3: LLM 검증 (Claude AI)

2️⃣ 검증 기준 정의
   ├─ Frontmatter (YAML 메타데이터)
   ├─ 파일 명명 규칙 (YYYY-MM-DD-*.enhanced.md)
   ├─ 필수 섹션 (3개)
   └─ 액션 아이템 표준

3️⃣ 자동 검증 로직
   ├─ 정규식 기반 구조 검증
   ├─ 유사도 기반 중복 검사
   ├─ 허구 (Hallucination) 탐지
   └─ 점수 산정 (A+~F)

4️⃣ CLAUDE.md 규칙 추가
   ├─ 3단계 검증 필수 조건
   ├─ A- 이상 평점 기준
   └─ 반복 검증 규칙 (최대 3회)
```

### 산출물
```
✅ SKILL_V2 (wiki-validation-orchestrator)
✅ validate-wiki.py (기계 검증 스크립트)
✅ CLAUDE.md 검증 규칙
✅ WIKI_VALIDATION_GUIDE.md (800줄)
✅ 3단계 자동 검증 시스템
```

### 검증 결과
```
📊 기계 검증 (Step 2)
   └─ 통과율: 85.7% (회의 파일 100%)

📊 LLM 검증 (Step 3)
   ├─ 평균 점수: 93.8/100 (A)
   ├─ 일치도: 90% 이상
   ├─ 허구: 0개
   └─ 완성도: 90% 이상
```

### 완료 상태
✅ **100% 완료** (2026-08-10)

---

## 📍 Phase 3C: Dataview 쿼리 & 대시보드

### 기간
2026-08-10 (1일)

### 목표
Obsidian Dataview를 이용한 실시간 대시보드 구축

### 주요 활동
```
1️⃣ Dataview 쿼리 작성 (6개)
   ├─ TASK: 진행 중인 액션 아이템
   ├─ TABLE: 회의 목록
   ├─ TABLE: 의사결정 현황
   ├─ STATS: 액션 통계
   ├─ TIMELINE: 회의 타임라인
   └─ GROUP: 담당자별 액션

2️⃣ 메인 대시보드 구성
   ├─ obsidian-vault/DASHBOARD.md
   ├─ 5개 섹션 (요약, 진행 중, 완료, 의사결정, 통계)
   └─ 모든 쿼리 통합

3️⃣ 의사결정 폴더 구축
   ├─ obsidian-vault/Decisions/
   ├─ _decision-template.md (템플릿)
   ├─ 2026-04-16-PG사-선정.md (결정: 결제 게이트웨이)
   └─ 2026-05-14-온보딩-개선-전략.md (결정: 온보딩)

4️⃣ 문서화
   ├─ obsidian-vault/Meetings/QUERIES.md (상세 쿼리 설명)
   └─ PHASE_3C_GUIDE.md (6단계 구축 가이드)
```

### 산출물
```
✅ DASHBOARD.md (메인 대시보드)
✅ QUERIES.md (6개 쿼리 + 상세 설명)
✅ Decisions/ 폴더 (템플릿 + 2개 사례)
✅ PHASE_3C_GUIDE.md (구축 가이드)
✅ PHASE_3C_TEST_PLAN.md (테스트 절차)
```

### 대시보드 기능
```
📊 실시간 통계
   ├─ 총 액션: 14개
   ├─ 완료: 11개 (79%)
   ├─ 진행 중: 2개 (14%)
   └─ 보류: 1개 (7%)

🎯 담당자별 현황
   ├─ 박준서: 5개 (완료 3개)
   ├─ 개발팀: 4개 (진행 중 2개)
   └─ 최민아: 3개 (완료 3개)

📅 마감일 기반 정렬
   └─ 우선순위 자동 계산
```

### 완료 상태
✅ **100% 완료** (2026-08-11)

---

## 📍 Phase 3D: Claude API 자동화

### 기간
2026-08-11 (준비 완료)

### 목표
Claude API를 이용한 회의 기록 자동 분석 & 액션 추출

### 주요 활동
```
1️⃣ 액션 추출 스크립트 (Step 1)
   ├─ scripts/extract-actions-from-meetings.py
   ├─ 기능: 회의 파일 읽기 → Claude API → JSON 추출
   ├─ 모델: claude-opus-5
   ├─ 최대 토큰: 4096
   └─ 입력: obsidian-vault/Meetings/*.md

2️⃣ 액션 병합 스크립트 (Step 2)
   ├─ scripts/merge-actions.py
   ├─ 기능: 중복 제거 + 정렬 + 통계
   ├─ 유사도 기반 중복 제거 (임계값: 0.85)
   ├─ 상태별 정렬 (완료, 진행중, 보류)
   └─ 마감일 기반 정렬

3️⃣ 마크다운 생성 스크립트 (Step 3)
   ├─ scripts/generate-action-items-md.py
   ├─ 기능: JSON → Markdown 변환
   ├─ 포맷: 상태별 섹션, 체크박스, 통계 테이블
   └─ 출력: obsidian-vault/Actions/ACTION_ITEMS.md

4️⃣ 문서화
   ├─ PHASE_3D_GUIDE.md (400줄, 상세 가이드)
   ├─ PHASE_3D_TEST_PLAN.md (330줄, 테스트 절차)
   └─ 4단계 테스트 흐름
```

### 파이프라인
```
회의 파일 (6개)
    ↓ (Step 1: Claude API)
extracted_actions.json
    ↓ (Step 2: 병합 & 중복 제거)
merged_actions.json
    ↓ (Step 3: 마크다운 생성)
ACTION_ITEMS.md (자동 생성)
    ↓ (Step 4: 검증)
기존 ACTION_ITEMS.md와 비교
```

### 산출물
```
✅ extract-actions-from-meetings.py (250줄)
✅ merge-actions.py (230줄)
✅ generate-action-items-md.py (200줄)
✅ PHASE_3D_GUIDE.md (400줄)
✅ PHASE_3D_TEST_PLAN.md (330줄)
✅ Commit: 0f1c4de
```

### 기대 효과
```
⏱️  시간 단축: 30분 → 2분 (16배 빠름)
✅ 정확도: 90% → 95%+ (AI 분석)
🔄 반복성: 낮음 → 높음 (자동화)
📊 추적성: 수동 → 자동 (JSON 기반)
```

### 완료 상태
✅ **100% 준비 완료** (2026-08-11)  
⏳ **테스트**: API 키 필요 (스킵 - 옵션 3)

---

## 📍 Phase 3E: 최종 검증

### 기간
2026-08-15 (예정)

### 목표
전체 자동화 시스템이 의도대로 작동하는지 검증

### 주요 활동
```
1️⃣ 환경 & 디렉토리 검증
   ├─ Obsidian 플러그인 설치 확인
   ├─ 회의 파일 6개 확인
   ├─ 템플릿 및 폴더 구조 확인
   └─ 모든 링크 유효성 검사

2️⃣ 스크립트 동작 검증
   ├─ Python 문법 검증 (py_compile)
   ├─ 임포트 의존성 확인
   ├─ 로깅 및 에러 핸들링 검증
   └─ (테스트 실행은 선택사항)

3️⃣ 문서 & 가이드 검증
   ├─ 모든 가이드 문서 검증
   ├─ 링크 정상 작동 확인
   ├─ 코드 예제 실행 가능 확인
   └─ README.md 최신화

4️⃣ 시스템 통합 검증
   ├─ Phase 3A-D 모두 완료 확인
   ├─ 데이터 흐름 일관성 검사
   ├─ Obsidian → Claude API → Markdown 파이프라인 검증
   └─ 최종 검증 리포트 작성
```

### 검증 체크리스트
```
✅ Phase 3A (Obsidian 설정) 완료
✅ Phase 3B (Wiki 검증) 완료
✅ Phase 3C (Dataview 쿼리) 완료
✅ Phase 3D (Claude API) 완료
⏳ Phase 3E (최종 검증) - 이번 단계
```

### 산출물
```
📋 최종 검증 리포트
   ├─ 시스템 상태 확인
   ├─ 발견된 문제 및 해결책
   ├─ 최종 점수 (Go/No-Go 판정)
   └─ Phase 3F 준비 상태
```

### 완료 기준
```
✅ 모든 플러그인 설치됨
✅ 모든 템플릿 생성됨
✅ 모든 스크립트 준비됨
✅ 모든 문서 완성됨
✅ 모든 링크 유효함
✅ README.md 최신화됨
→ Go for Phase 3F
```

### 완료 상태
🟡 **진행 중** (2026-08-15 예정)

---

## 📍 Phase 3F: 첫 회의 테스트

### 기간
2026-08-17 (목표)

### 목표
실제 회의에서 전체 자동화 프로세스 테스트

### 주요 활동
```
1️⃣ 회의 진행
   ├─ 실제 팀 회의 진행
   ├─ Obsidian 템플릿으로 회의록 작성
   └─ 액션 아이템 및 의사결정 기록

2️⃣ 실시간 대시보드 확인
   ├─ DASHBOARD.md 열기
   ├─ 새 액션 아이템 즉시 반영 확인
   ├─ 담당자별 통계 업데이트 확인
   └─ Dataview 쿼리 렌더링 확인

3️⃣ (선택) Claude API 테스트
   ├─ ANTHROPIC_API_KEY 설정
   ├─ extract-actions-from-meetings.py 실행
   ├─ 자동 추출 결과 확인
   └─ 기존 ACTION_ITEMS.md와 비교

4️⃣ 최종 평가
   ├─ 시스템 안정성 평가
   ├─ 사용자 경험 평가
   ├─ 성능 평가 (속도, 정확도)
   └─ 개선 사항 도출
```

### 성공 기준
```
✅ 회의록이 자동 템플릿으로 생성됨
✅ 액션 아이템이 즉시 대시보드에 반영됨
✅ 모든 링크가 정상 작동함
✅ Dataview 쿼리가 실시간 업데이트됨
✅ 통계 데이터가 정확함
✅ (선택) Claude API가 액션을 정확히 추출함
→ 프로젝트 성공!
```

### 산출물
```
📋 첫 회의 테스트 리포트
   ├─ 테스트 날짜 & 참석자
   ├─ 실행 결과 (성공/실패)
   ├─ 발견된 문제
   ├─ 개선 사항
   └─ 최종 평가 (별점)
```

### 완료 상태
🎯 **예정** (2026-08-17)

---

## 📊 전체 진행도

```
Phase 1: 설계
✅ ████████████████████ 100%

Phase 2: 계획
✅ ████████████████████ 100%

Phase 3: 구현 & 검증
  3A. Obsidian 설정
  ✅ ████████████████████ 100% (2026-08-10)
  
  3B. Wiki 검증
  ✅ ████████████████████ 100% (2026-08-10)
  
  3C. Dataview 쿼리
  ✅ ████████████████████ 100% (2026-08-11)
  
  3D. Claude API
  ✅ ████████████████████ 100% (2026-08-11)
  
  3E. 최종 검증
  🟡 ████████░░░░░░░░░░░░  40% (예정: 2026-08-15)
  
  3F. 첫 회의 테스트
  🎯 ░░░░░░░░░░░░░░░░░░░░   0% (예정: 2026-08-17)
```

---

## 🎯 주요 마일스톤

| 날짜 | Phase | 내용 | 상태 |
|------|-------|------|------|
| 2026-04-16 | 1 | 설계 시작 | ✅ 완료 |
| 2026-07-23 | 1 | 설계 완료 | ✅ 완료 |
| 2026-08-10 | 2 | 계획 완료 | ✅ 완료 |
| 2026-08-10 | 3A | Obsidian 설정 | ✅ 완료 |
| 2026-08-10 | 3B | Wiki 검증 | ✅ 완료 |
| 2026-08-11 | 3C | Dataview 쿼리 | ✅ 완료 |
| 2026-08-11 | 3D | Claude API | ✅ 완료 |
| 2026-08-15 | 3E | 최종 검증 | 🟡 진행 중 |
| 2026-08-17 | 3F | 첫 회의 테스트 | 🎯 예정 |

---

## 📚 주요 문서 맵

```
Phase 1-2
└─ docs/guides/
   ├─ COMPLETE_GUIDE.md (전체 요약)
   └─ SYSTEM_ARCHITECTURE.md (아키텍처)

Phase 3A
└─ docs/guides/
   ├─ OBSIDIAN_SETUP_GUIDE.html (설정 PPT)
   └─ SETUP_CHECKLIST.md (60개 체크리스트)

Phase 3B
└─ docs/guides/
   ├─ WIKI_VALIDATION_GUIDE.md (검증 가이드)
   └─ SKILLS_USAGE_GUIDE.md (스킬 사용법)

Phase 3C
└─ docs/references/
   ├─ PHASE_3C_GUIDE.md (구축 가이드)
   └─ PHASE_3C_TEST_PLAN.md (테스트 절차)

Phase 3D
└─ docs/references/
   ├─ PHASE_3D_GUIDE.md (상세 가이드)
   └─ PHASE_3D_TEST_PLAN.md (테스트 절차)

Phase 3E-F
└─ docs/references/
   ├─ FIRST_MEETING_TEST.md (테스트 가이드)
   └─ SUCCESS_CRITERIA.md (성공 기준)
```

---

**문서 작성**: 2026-08-11  
**최신 업데이트**: 2026-08-11  
**다음 리뷰**: 2026-08-15 (Phase 3E)
