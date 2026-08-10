# 🚀 GitHub Actions 자동화 설정

> **최종 업데이트**: 2026-08-10  
> **상태**: ✅ 완료 (모든 워크플로우 활성)

---

## 📋 설정된 워크플로우

### 1. **Wiki Validation** (`wiki-validation.yml`)
**목적**: Wiki 파일 품질 보장  
**트리거**:
- Push to `main` (Wiki 파일 변경 시)
- Pull Request (Wiki 파일 변경 시)
- 매주 월요일 09:00 UTC

**검증 항목**:
- ✅ Frontmatter 검증 (date, type, status, enhanced_date)
- ✅ 액션 아이템 포맷 확인
- ✅ 파일 이름 규칙 (YYYY-MM-DD-*.enhanced.md)
- ✅ 링크 검증

**성공 조건**: 모든 메트릭이 PASS

---

### 2. **Python Lint & Type Check** (`python-lint.yml`)
**목적**: Python 코드 품질 관리  
**트리거**:
- Push to `main` (scripts/ 변경 시)
- Pull Request (scripts/ 변경 시)

**검증 항목**:
- ✅ Black 포매팅
- ✅ isort import 정렬
- ✅ Flake8 linting
- ✅ MyPy 타입 체크
- ✅ Syntax 검증

**도구**:
```
black, flake8, isort, pylint, mypy
```

---

### 3. **Automated PR Creation** (`auto-pr.yml`) ⭐ NEW
**목적**: 검증 통과 후 자동으로 PR 생성  
**트리거**:
- Push to `release/v1.0.0` (변경 감지 시)
- 수동 실행 가능 (`workflow_dispatch`)

**자동화 기능**:
- ✅ 변경사항 자동 감지
- ✅ Wiki & Python 검증 실행
- ✅ 검증 통과 시 자동 PR 생성
- ✅ PR에 상세 설명 자동 포함
- ✅ 최종 리포트 GitHub Summary 생성

**PR 자동 생성 조건**:
```
release/v1.0.0 → PR to main (자동)
```

**PR 포함 정보**:
- 커밋 메시지 (제목)
- 변경사항 상세
- 검증 상태 (Wiki, Python)
- 프로젝트 규칙 링크

---

### 4. **Test & Deploy Check** (`test-and-deploy.yml`) ⭐ NEW
**목적**: PR 병합 전 종합 검증  
**트리거**:
- Pull Request (opened, synchronize, reopened)
- Push to `main` (scripts/, Markdown 변경 시)

**검증 범위**:
- ✅ 모든 Python 스크립트 syntax 확인
- ✅ Wiki validator 기능 테스트
- ✅ Create-PR 스크립트 기능 테스트
- ✅ Wiki 파일 구조 검증
- ✅ CLAUDE.md 규칙 확인
- ✅ README.md 진행도 확인
- ✅ Git 상태 확인

**자동 댓글**:
- PR에 검증 결과를 자동으로 댓글 추가
- 상태: ✅ PASSED / ❌ FAILED

**배포 준비도 체크리스트**:
- Python syntax
- Wiki validator
- Create-PR script
- CLAUDE.md rules
- README.md updates
- Git state

---

## 🔄 워크플로우 흐름도

```
Local Development
        ↓
Push to release/v1.0.0
        ↓
┌─────────────────────┐
│ auto-pr.yml (자동)  │
│ - 변경 감지         │
│ - Wiki 검증         │
│ - Python 검증       │
│ - PR 자동 생성      │
└─────────────────────┘
        ↓
PR to main (자동 생성됨)
        ↓
┌─────────────────────┐
│ test-and-deploy.yml │
│ - 종합 검증         │
│ - PR 댓글 추가      │
│ - 배포 준비도 체크  │
└─────────────────────┘
        ↓
Code Review & Merge
        ↓
┌─────────────────────┐
│ wiki-validation.yml │
│ python-lint.yml     │
│ (Main에 자동 실행)  │
└─────────────────────┘
        ↓
✅ Production Ready
```

---

## 📊 워크플로우 상태 확인

### GitHub에서 확인하기
```
Repository → Actions → 워크플로우 선택 → 실행 기록 확인
```

### 각 워크플로우 보기
| 워크플로우 | 상태 | 최근 실행 |
|-----------|------|---------|
| Wiki Validation | ✅ 활성 | 정기 실행 |
| Python Lint | ✅ 활성 | 코드 변경 시 |
| Auto PR | ✅ 활성 | release/v1.0.0 변경 시 |
| Test & Deploy | ✅ 활성 | PR 생성 시 |

---

## 🔧 필수 GitHub 설정

### 1. Token 권한 확보
워크플로우가 PR 생성 & 댓글을 달 수 있어야 함:

```
Settings → Actions → General
  ├─ Permissions: Read and write permissions ✅
  └─ Allow GitHub Actions to create and approve pull requests ✅
```

### 2. Branch Protection (권장)
Main 브랜치 보호:

```
Settings → Branches → main
  ├─ Require pull request reviews ✅
  ├─ Require status checks to pass ✅
  └─ Require branches to be up to date ✅
```

### 3. PR 자동화 설정 (선택)
```
Settings → Autolink references (선택사항)
Settings → Pull Requests → auto-merge (선택사항)
```

---

## 🚀 사용 방법

### 자동 실행 (기본)
```bash
# release/v1.0.0 브랜치에 commit & push
git add .
git commit -m "feat: Phase 3C 완료 - Dataview 쿼리"
git push origin release/v1.0.0

# 자동으로:
# 1. auto-pr.yml 실행 (검증)
# 2. PR 자동 생성
# 3. test-and-deploy.yml 실행
# 4. 결과 댓글 추가
```

### 수동 실행
```bash
# GitHub 웹에서
Actions → Automated PR Creation → Run workflow

# 또는 커스텀 PR 제목/본문 지정
Actions → Automated PR Creation → Run workflow
  ├─ pr_title: "Custom title"
  └─ pr_body: "Custom description"
```

---

## 📝 워크플로우 로그 보기

### 실시간 로그
```
GitHub → Actions → 워크플로우 → 실행 번호 클릭
```

### 단계별 상세 보기
```
실행 → Jobs → 단계 클릭 → 로그 확인
```

### 핵심 로그 항목
- ✅ Checkout repository
- ✅ Set up Python
- ✅ Install dependencies
- ✅ Run validations
- ✅ Create PR / Generate report

---

## ✅ 검증 체크리스트

각 워크플로우가 처리하는 항목:

### Wiki Validation
- [ ] Frontmatter 존재
- [ ] 필수 필드 (date, type, status)
- [ ] 액션 아이템 포맷
- [ ] 파일명 규칙

### Python Lint
- [ ] Syntax error 없음
- [ ] Code format (Black)
- [ ] Import order (isort)
- [ ] Linting issues (Flake8)
- [ ] Type hints (MyPy)

### Auto PR
- [ ] 변경 감지
- [ ] Wiki 검증 PASS
- [ ] Python 검증 PASS
- [ ] PR 생성

### Test & Deploy
- [ ] Python syntax PASS
- [ ] Wiki validator test PASS
- [ ] Create-PR script test PASS
- [ ] Wiki structure check PASS
- [ ] CLAUDE.md verified
- [ ] README.md updated

---

## 🔐 보안 주의사항

### API 키 관리
```
❌ .github/workflows 파일에 API 키 절대 금지
✅ GitHub Secrets 사용:
   Settings → Secrets and variables → Actions
```

### PR 자동 댓글
```
✅ 공개 정보만 포함
❌ 민감 정보 절대 금지
```

---

## 🎯 다음 Phase에서의 활용

### Phase 3C (Dataview 쿼리)
```
1. Dataview 쿼리 파일 생성
2. git push release/v1.0.0
3. auto-pr.yml 자동 실행
4. PR 자동 생성
5. test-and-deploy.yml 검증
6. Code review & merge
```

### Phase 3D (Claude API)
```
1. API 스크립트 작성
2. scripts/ 폴더에 저장
3. python-lint.yml 자동 실행
4. auto-pr.yml PR 생성
5. test-and-deploy.yml 테스트
6. 병합 & 배포
```

---

## 📞 문제 해결

### PR이 생성되지 않음
```
1. auto-pr.yml 로그 확인
2. git 변경사항 확인 (release/v1.0.0)
3. 검증 에러 확인
4. GitHub Actions 권한 확인
```

### 워크플로우가 실행 안 됨
```
1. 브랜치/경로 확인 (트리거 조건)
2. .github/workflows/ 문법 검증
3. GitHub Actions 활성화 확인
```

### 댓글이 달리지 않음
```
1. PR이 자동으로 생성되었는지 확인
2. github.event.issue.number 존재 확인
3. Token 권한 확인
```

---

## 📚 참고 문서

- [GitHub Actions 공식 문서](https://docs.github.com/en/actions)
- [create-pull-request 액션](https://github.com/peter-evans/create-pull-request)
- [CLAUDE.md - 프로젝트 규칙](../CLAUDE.md)
- [Phase 진행도 - README.md](../README.md)

---

**작성자**: Claude Haiku 4.5  
**작성일**: 2026-08-10  
**상태**: ✅ 완료 (모든 워크플로우 설정 완료)
