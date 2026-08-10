# 🏗️ 시스템 아키텍처

> Obsidian 기반 회의 관리 시스템의 완전한 구조

---

## 📊 전체 다이어그램

```
┌─────────────────────────────────────────────────────────┐
│          회의 관리 자동화 시스템 (2026-08-10~17)        │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  Obsidian    │  │  Claude API  │  │   Dataview   │  │
│  │   (노트)     │  │  (분석)      │  │  (쿼리)      │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
│        ↓                  ↓                   ↓         │
│  ┌──────────────────────────────────────────────────┐  │
│  │      obsidian-vault/                             │  │
│  │  ├─ SSOT/ (단일 정보 원칙)                      │  │
│  │  ├─ Meetings/ (회의 기록)                       │  │
│  │  ├─ Decisions/ (의사결정)                       │  │
│  │  ├─ Daily/ (일일 노트)                          │  │
│  │  ├─ Templates/ (템플릿)                         │  │
│  │  └─ QUERIES.md (대시보드)                       │  │
│  └──────────────────────────────────────────────────┘  │
│        ↓                  ↓                   ↓         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  원본 데이터 │  │  자동화      │  │  링크 네트  │  │
│  │  보존        │  │  스크립트    │  │  워크       │  │
│  │  llm-ssot/   │  │  scripts/    │  │  [[파일]]   │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## 🔄 데이터 흐름

### 회의 프로세스

```
1️⃣ 회의 준비
   ↓
   Templater (자동 템플릿 생성)
   → meeting-new.md 적용
   → 날짜/시간 자동 입력
   ↓
2️⃣ 회의 진행
   ↓
   Obsidian (실시간 기록)
   → [[담당자]] 링크 추가
   → [[ACTION_ITEMS]] 참조
   ↓
3️⃣ 회의 후 분석
   ↓
   Claude API (meeting-processor.py)
   → 요약 생성 (3-5문장)
   → 액션 추출 (담당자, 마감일)
   → 결정 분석 (근거, 담당자)
   ↓
4️⃣ 대시보드 갱신
   ↓
   Dataview (QUERIES.md)
   → 쿼리 1: 진행 중인 액션
   → 쿼리 2: 회의 타임라인
   → 쿼리 3: 결정사항 현황
   ↓
5️⃣ 링크 네비게이션
   ↓
   [[ACTION_ITEMS]] → 액션 추적
   [[담당자]] → 담당자 프로필
   [[결정]] → 관련 결정사항
```

---

## 📦 컴포넌트 구조

### Layer 1: 입력층 (Data Input)

```
┌────────────────────────────────────┐
│       회의 기록 입력               │
├────────────────────────────────────┤
│                                    │
│  Obsidian Templater               │
│  ├─ meeting-new.md                │
│  ├─ daily.md                      │
│  └─ 자동 날짜/시간 입력           │
│                                    │
│  Periodic Notes                    │
│  └─ Daily Note 자동 생성          │
│                                    │
└────────────────────────────────────┘
```

### Layer 2: 저장층 (Data Storage)

```
┌────────────────────────────────────┐
│      Obsidian Vault 저장소         │
├────────────────────────────────────┤
│                                    │
│  obsidian-vault/                  │
│  ├─ SSOT/                         │
│  │  └─ 단일 정보 원칙 문서        │
│  │                                │
│  ├─ Meetings/                     │
│  │  ├─ 회의록 파일 (6개)          │
│  │  ├─ ACTION_ITEMS.md            │
│  │  ├─ MEETINGS_ANALYSIS.md       │
│  │  └─ analysis_*.json            │
│  │                                │
│  ├─ Decisions/                    │
│  │  ├─ DECISIONS.md               │
│  │  ├─ TIMELINE.md                │
│  │  ├─ PEOPLE.md                  │
│  │  ├─ TOPICS.md                  │
│  │  ├─ DASHBOARD.md               │
│  │  └─ WIKI_INDEX.md              │
│  │                                │
│  ├─ Daily/                        │
│  │  └─ YYYY-MM-DD.md (자동생성)   │
│  │                                │
│  ├─ Templates/                    │
│  │  ├─ meeting-new.md             │
│  │  └─ daily.md                   │
│  │                                │
│  └─ QUERIES.md (대시보드)         │
│                                    │
└────────────────────────────────────┘
```

### Layer 3: 처리층 (Processing)

```
┌────────────────────────────────────┐
│      자동화 처리 (Automation)      │
├────────────────────────────────────┤
│                                    │
│  A. 문서 마이그레이션             │
│     migrate-docs-advanced.py       │
│     ├─ 원본 데이터 읽기           │
│     ├─ 자동 백업 생성             │
│     ├─ 링크 검증                  │
│     └─ obsidian-vault 복사        │
│                                    │
│  B. Claude API 분석               │
│     meeting-processor.py           │
│     ├─ 회의 노트 읽기             │
│     ├─ Claude로 분석              │
│     ├─ JSON 결과 저장             │
│     └─ ACTION_ITEMS 자동 갱신     │
│                                    │
│  C. Dataview 렌더링               │
│     Dataview 플러그인             │
│     ├─ 쿼리 실행                  │
│     ├─ 데이터 필터링              │
│     └─ 테이블 렌더링              │
│                                    │
└────────────────────────────────────┘
```

### Layer 4: 출력층 (Output)

```
┌────────────────────────────────────┐
│      대시보드 & 분석 결과          │
├────────────────────────────────────┤
│                                    │
│  QUERIES.md (대시보드)             │
│  ├─ 쿼리 1: 진행 중인 액션        │
│  │  └─ TABLE 렌더링               │
│  │                                │
│  ├─ 쿼리 2: 회의 타임라인         │
│  │  └─ TABLE 렌더링               │
│  │                                │
│  └─ 쿼리 3: 결정사항 현황         │
│     └─ TABLE 렌더링               │
│                                    │
│  analysis_*.json (분석 결과)       │
│  ├─ 요약                          │
│  ├─ 액션                          │
│  ├─ 결정                          │
│  └─ SSOT 영향                     │
│                                    │
└────────────────────────────────────┘
```

---

## 🔌 플러그인 역할

### 필수 플러그인 (Tier 1)

| 플러그인 | 역할 | 목적 |
|---------|------|------|
| **Dataview** | 동적 쿼리 실행 | 대시보드 렌더링 |
| **Templater** | 자동 템플릿 생성 | 회의 기록 자동화 |
| **Periodic Notes** | 주기적 노트 생성 | Daily Note 자동화 |

### 보조 플러그인 (Tier 2)

| 플러그인 | 역할 | 목적 |
|---------|------|------|
| **Breadcrumbs** | 문서 관계도 | 네비게이션 시각화 |
| **Calendar** | 달력 인터페이스 | 날짜 기반 접근 |
| **Checklist** | 체크리스트 UI | 액션 추적 |

---

## 🔗 링크 체계

### 링크 유형

```
1. 문서 링크
   [[파일명]]
   └─ Obsidian 파일로 연결

2. 섹션 링크
   [[파일명#섹션명]]
   └─ 특정 섹션으로 연결

3. 사람 링크
   [[담당자명]]
   └─ 담당자 프로필로 연결

4. 액션 링크
   [[ACTION_ITEMS#작업내용]]
   └─ 특정 액션으로 연결
```

### 링크 네트워크

```
ACTION_ITEMS.md
├─ [[담당자1]] (담당자 프로필)
├─ [[담당자2]]
└─ [[2026-05-14-회의]] (회의 기록)

2026-05-14-회의.enhanced.md
├─ [[담당자1]]
├─ [[담당자2]]
├─ [[ACTION_ITEMS]]
└─ [[결정사항]]

Decisions/DECISIONS.md
├─ [[담당자1]]
├─ [[담당자2]]
└─ [[ACTION_ITEMS#관련액션]]
```

---

## 📊 데이터 저장소

### obsidian-vault/ (메인)

```
obsidian-vault/
├─ .obsidian/           (Obsidian 설정)
├─ SSOT/                (단일 정보 원칙)
│  ├─ SSOT.md
│  ├─ GOVERNANCE.md
│  ├─ model-selection.md
│  └─ prompt-engineering.md
│
├─ Meetings/            (회의 기록)
│  ├─ 2026-04-16-제품주간회의.enhanced.md
│  ├─ 2026-05-14-제품주간회의.enhanced.md
│  ├─ ... (4개 더)
│  ├─ ACTION_ITEMS.md
│  ├─ MEETINGS_ANALYSIS.md
│  ├─ _meeting-template.enhanced.md
│  └─ analysis_*.json
│
├─ Decisions/           (의사결정)
│  ├─ DECISIONS.md
│  ├─ TIMELINE.md
│  ├─ PEOPLE.md
│  ├─ TOPICS.md
│  ├─ DASHBOARD.md
│  └─ WIKI_INDEX.md
│
├─ Daily/               (일일 노트)
│  └─ YYYY-MM-DD.md (자동생성)
│
├─ Weekly/              (주간 노트)
│
├─ Templates/           (템플릿)
│  ├─ meeting-new.md
│  └─ daily.md
│
└─ QUERIES.md           (대시보드)
```

### llm-ssot/ (원본)

```
llm-ssot/
├─ SSOT/                (원본 SSOT)
├─ Meetings/            (원본 회의록)
│  ├─ Raw/             (RAW 형식)
│  └─ Enhanced 형식들
├─ WIKI/                (분석 결과)
└─ ...
```

---

## ⚙️ 스크립트 구조

### migrate-docs-advanced.py

```
입력: llm-ssot/ (원본)
  ↓
처리:
  1. 백업 생성 (vault_backup_*)
  2. 파일 복사
  3. 링크 검증
  4. 메타데이터 생성
  ↓
출력: obsidian-vault/ (대상)
     .migration_metadata.json
```

### meeting-processor.py

```
입력: 회의 파일 (Meetings/*.enhanced.md)
  ↓
처리:
  1. 파일 읽기
  2. Claude API로 분석
  3. JSON 생성
  4. ACTION_ITEMS.md 갱신
  ↓
출력: analysis_*.json
     ACTION_ITEMS.md (갱신)
```

---

## 🎯 정보 흐름 (Phase별)

### Phase 1: 설계 (분석)

```
회의록 분석 → 패턴 파악 → 문제점 도출 → 규칙 정의
```

### Phase 2: 계획 (설계)

```
SSOT 규칙 → Obsidian 구조 → 자동화 설계 → 단계별 계획
```

### Phase 3: 구현 (자동화)

```
Phase 3A: 설정
  Obsidian → 플러그인 → 템플릿

Phase 3B: 마이그레이션
  llm-ssot → migrate-docs → obsidian-vault

Phase 3C: 쿼리
  QUERIES.md → Dataview → 대시보드

Phase 3D: API
  회의 파일 → meeting-processor → 분석 결과

Phase 3E: 검증
  전체 시스템 → 동작 확인 → 준비 완료

Phase 3F: 테스트
  첫 회의 → 자동화 검증 → 본운영 준비
```

---

## 📈 확장성 (미래)

### 추가 가능한 기능

```
1. Slack 연동
   → 회의 알림 자동 송신
   → 액션 진행도 알림

2. Google Calendar 연동
   → 회의 일정 자동 연동
   → 마감일 자동 전송

3. 메일 연동
   → 회의록 자동 발송
   → 액션 리마인더

4. 깃허브 이슈 연동
   → 액션 ↔ 이슈 동기화
   → 자동 할당

5. 비즈니스 인텔리전스
   → 회의 빈도 분석
   → 액션 완료율 추적
   → 의사결정 속도 분석
```

---

## 🔐 보안 & 무결성

### 데이터 보호

```
1. 백업
   → vault_backup_* (자동 생성)
   → llm-ssot/ (원본 보존)

2. 검증
   → 링크 검증 (migration_metadata)
   → 파일 체크섬
   → 데이터 일관성 확인

3. 접근 제어
   → Obsidian 로컬 저장
   → Git으로 버전 관리
   → API 키 환경변수 관리
```

---

## 📊 성능 특성

### 처리 시간

| 작업 | 예상 시간 |
|------|----------|
| 회의 템플릿 생성 | < 1초 |
| 회의 기록 저장 | < 1초 |
| Claude 분석 | 10-30초 |
| Dataview 렌더링 | 1-2초 |
| 링크 이동 | < 0.5초 |

### 메모리 사용

```
Obsidian: 200-400MB
Python 스크립트: 100-200MB
Dataview 쿼리: 10-50MB
```

---

## 🎯 핵심 특징

```
✅ 자동화: 템플릿 → 분석 → 대시보드까지 자동
✅ 링크: [[파일]] 네트워크로 관계 추적
✅ SSOT: 단일 정보 원칙으로 데이터 무결성
✅ 통합: Obsidian + Claude API + Dataview
✅ 확장: 플러그인/스크립트로 기능 추가 가능
✅ 안전: 백업 + 버전관리 + 검증
```

---

**마지막 업데이트**: 2026-08-14  
**버전**: 1.0  
**상태**: ✅ 완성

🏗️ **완전한 시스템 아키텍처 설계 완료!**
