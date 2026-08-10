# 🚀 Phase 3C: Dataview 쿼리 설정 가이드

> **Status**: 진행 중 (2026-08-10 시작)  
> **목표**: 실시간 액션, 회의, 결정사항 추적 대시보드 완성  
> **예상 완료**: 2026-08-14  

---

## 📋 Phase 3C 체크리스트

### ✅ 완료된 항목
- [x] QUERIES.md 파일 생성 (5개 쿼리 정의)
- [x] ACTION_ITEMS.md 마이그레이션 (14개 아이템)
- [x] 회의 기록 마이그레이션 (6개 파일)
- [x] Obsidian 플러그인 설치 (Dataview)

### ⏳ 진행 중
- [ ] **Step 1**: Obsidian에서 쿼리 렌더링 테스트
- [ ] **Step 2**: Decisions 폴더 구조 확인/생성
- [ ] **Step 3**: DASHBOARD.md 생성 (메인 대시보드)
- [ ] **Step 4**: 각 쿼리 기능 검증
- [ ] **Step 5**: 링크 검증 및 수정
- [ ] **Step 6**: 최종 커밋

---

## 🔍 현재 구조

```
obsidian-vault/
├─ Meetings/
│  ├─ 2026-04-16-제품주간회의.enhanced.md
│  ├─ 2026-05-14-제품주간회의.enhanced.md
│  ├─ 2026-06-11-제품주간회의.enhanced.md
│  ├─ 2026-06-25-온보딩개선회의.enhanced.md
│  ├─ 2026-07-09-제품주간회의.enhanced.md
│  ├─ 2026-07-23-제품주간회의.enhanced.md
│  ├─ QUERIES.md ✅ (대시보드 쿼리)
│  └─ MEETINGS_ANALYSIS.md
│
├─ Actions/
│  └─ ACTION_ITEMS.md ✅ (14개 액션)
│
└─ Decisions/
   └─ (아직 없음 - 생성 필요)
```

---

## 📝 Step-by-Step 진행

### Step 1️⃣: Obsidian에서 쿼리 렌더링 테스트

**목표**: QUERIES.md의 쿼리들이 올바르게 렌더링되는지 확인

**작업**:
```bash
# Obsidian 열기
open /Users/mac/work/claude/20260810_harness/obsidian-vault

# 또는 MacOS Obsidian.app에서 직접 폴더 열기
```

**확인 사항**:
```
obsidian-vault/Meetings/QUERIES.md 열기
  ↓
5개 쿼리가 테이블로 렌더링되는지 확인:
  1. 진행 중인 액션 (TASK 쿼리)
  2. 회의 타임라인 (TABLE 쿼리)
  3. 결정사항 현황 (TABLE 쿼리)
  4. 액션별 담당자 (선택)
  5. 월별 회의 통계 (선택)
```

**렌더링 안 되면**:
1. Dataview 플러그인 활성화 확인
2. Obsidian 재시작
3. Cmd + Shift + R (새로고침)

---

### Step 2️⃣: Decisions 폴더 구조 확인/생성

**목표**: 결정사항 추적을 위한 폴더 구조 생성

**현재 상태**:
```bash
❌ obsidian-vault/Decisions/ 폴더 없음
```

**생성 단계**:

```bash
# 1. 폴더 생성
mkdir -p obsidian-vault/Decisions

# 2. 템플릿 생성 (DECISIONS_TEMPLATE.md)
cat > obsidian-vault/Decisions/_decision-template.md << 'EOF'
---
date: YYYY-MM-DD
type: decision
status: 확정
owner: 담당자명
category: 기술/비즈니스/운영
impact: 높음/중간/낮음
---

# 결정 제목

## 배경
- 문제점
- 의사결정 필요 이유

## 결정 사항
- 최종 결정
- 선택된 옵션

## 영향도
- 영향을 받는 팀
- 예상 일정

## 연관 회의
[[2026-XX-XX-회의명.enhanced.md]]
EOF
```

**초기 결정사항 추가**:
```bash
# 기존 회의 기록에서 결정사항 추출하여 추가
# 예: 2026-04-16 회의에서의 "A사 PG 선정" 등
```

---

### Step 3️⃣: DASHBOARD.md 생성 (메인 대시보드)

**목표**: 모든 쿼리를 한곳에 모아서 보는 메인 대시보드 생성

**생성할 파일**: `obsidian-vault/DASHBOARD.md`

**구조**:
```markdown
# 📊 회의 관리 시스템 대시보드

## 🎯 실시간 현황

### 📌 진행 중인 액션
[QUERIES.md의 쿼리 1 삽입 또는 링크]

### 📅 최근 회의
[QUERIES.md의 쿼리 2 삽입 또는 링크]

### ✅ 결정사항
[QUERIES.md의 쿼리 3 삽입 또는 링크]

## 📈 통계

- 총 액션: 14개
- 완료율: 79%
- 회의: 6개
```

---

### Step 4️⃣: 각 쿼리 기능 검증

**목표**: 모든 쿼리가 정상 작동하는지 확인

**쿼리별 검증**:

| 쿼리 | 데이터 소스 | 확인 항목 | 상태 |
|------|----------|---------|------|
| 진행 중인 액션 | ACTION_ITEMS.md | TASK 렌더링, 상태 표시 | ⏳ |
| 회의 타임라인 | Meetings/ 폴더 | 최근순 정렬, 링크 작동 | ⏳ |
| 결정사항 현황 | Decisions/ 폴더 | 상태별 정렬, 담당자 표시 | ⏳ |
| 담당자별 액션 | Meetings/ | 그룹핑, 개수 표시 | ⏳ |
| 월별 통계 | Meetings/ | 월별 집계, 개수 표시 | ⏳ |

**테스트 방법**:
```
각 쿼리 클릭 후:
1. 테이블 헤더에서 정렬 변경 가능한가?
2. 링크를 클릭하면 해당 문서로 이동하는가?
3. 필터링이 가능한가?
4. 데이터가 최신으로 갱신되는가?
```

---

### Step 5️⃣: 링크 검증 및 수정

**목표**: 모든 내부 링크가 올바르게 작동하는지 확인

**검증 스크립트** (선택사항):
```bash
python3 scripts/migrate-docs-advanced.py \
  --validate-links \
  --source obsidian-vault/Meetings/
```

**수동 확인**:
1. 각 ACTION_ITEMS 항목의 회의 링크 확인
2. 각 회의 파일의 액션 항목 링크 확인
3. 결정사항에서 회의 링크 확인

**링크 포맷**:
```markdown
✅ 올바른 형식:
[[2026-04-16-제품주간회의.enhanced.md]]
[[2026-04-16-제품주간회의.enhanced.md#섹션]]

❌ 잘못된 형식:
[링크](obsidian-vault/Meetings/...)
[[./relative/path]]
```

---

### Step 6️⃣: 최종 커밋

**목표**: Phase 3C 완료 커밋

**작업**:
```bash
# 변경사항 확인
git status

# 파일 추가
git add obsidian-vault/Decisions/
git add obsidian-vault/DASHBOARD.md
git add docs/references/PHASE_3C_GUIDE.md

# 커밋
git commit -m "feat: Phase 3C 완료 - Dataview 쿼리 설정 & 대시보드

✅ QUERIES.md: 5개 쿼리 정의 및 테스트
✅ DASHBOARD.md: 메인 대시보드 생성
✅ Decisions/: 결정사항 폴더 구조 완성
✅ 링크 검증: 모든 내부 링크 확인

지원 기능:
- 실시간 액션 추적 (ACTION_ITEMS.md 기반)
- 회의 타임라인 조회 (Meetings 폴더)
- 결정사항 현황 (Decisions 폴더)
- 담당자별 액션 그룹핑
- 월별 회의 통계

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"

# 푸시
git push origin release/v1.0.0
```

---

## 🎯 Expected Output

Phase 3C 완료 후:

```
obsidian-vault/
├─ Meetings/
│  ├─ [6개 회의 파일]
│  ├─ QUERIES.md ✅
│  └─ MEETINGS_ANALYSIS.md
│
├─ Actions/
│  └─ ACTION_ITEMS.md ✅
│
├─ Decisions/
│  ├─ _decision-template.md ✅
│  ├─ 2026-04-16-PG사-선정.md ✅
│  └─ [기타 결정사항]
│
└─ DASHBOARD.md ✅ (메인 대시보드)
```

---

## 📊 진행도

```
Phase 3C: Dataview 쿼리
  └─ Step 1: 쿼리 렌더링 테스트 ⏳
  └─ Step 2: Decisions 폴더 생성 ⏳
  └─ Step 3: DASHBOARD.md 생성 ⏳
  └─ Step 4: 쿼리 기능 검증 ⏳
  └─ Step 5: 링크 검증 ⏳
  └─ Step 6: 최종 커밋 ⏳
```

---

## 📞 문제 해결

### 쿼리가 렌더링 안 됨
```
1. Dataview 플러그인 활성화 확인
2. Obsidian 재시작
3. Cmd + Shift + R (캐시 새로고침)
4. 쿼리 문법 확인 (QUERIES.md)
```

### 링크가 작동 안 함
```
1. 파일명 정확히 확인
2. [[파일명.md]] 포맷 확인
3. 상대 경로 사용 금지
4. 공백/특수문자 확인
```

### 데이터가 표시 안 됨
```
1. ACTION_ITEMS.md 파일 존재 확인
2. Decisions/ 폴더 및 파일 확인
3. Frontmatter 메타데이터 확인
4. 필터링 조건 (WHERE) 재확인
```

---

**마지막 업데이트**: 2026-08-10  
**Dataview 버전**: 5.3+  
**예상 완료 기한**: 2026-08-14
