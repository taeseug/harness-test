# 🤖 GitHub Actions 자동화 설정 가이드

> **완전 자동화된 CI/CD 파이프라인**  
> Wiki 검증, Python 린트, 마크다운 검증 자동 실행

---

## 📋 개요

GitHub Actions를 통해 다음을 자동으로 실행합니다:

1. **Wiki Validation** - 회의 파일 자동 검증
2. **Python Lint** - Python 스크립트 품질 검사
3. **Markdown Validation** - 마크다운 구조 검증

---

## 🎯 워크플로우 설명

### 1️⃣ Wiki Validation (`wiki-validation.yml`)

**언제 실행되나?**
- 모든 push (main 브랜치)
- 회의 파일 변경 시
- 매주 월요일 09:00 UTC (정기 검증)

**무엇을 검증하나?**
```
✅ Frontmatter (YAML 헤더)
   ├─ date 필드
   ├─ type 필드
   ├─ status 필드
   └─ enhanced_date 필드

✅ 액션 아이템
   ├─ 섹션 존재 확인
   ├─ 형식 검증
   └─ 개수 계산

✅ 파일명 규칙
   └─ YYYY-MM-DD-*.enhanced.md 형식

✅ 문서 무결성
   └─ UTF-8 인코딩 검증
```

**결과**
- ✅ PASS: 모든 검증 통과
- ⚠️  WARN: 경미한 문제 (검토 권장)
- ❌ FAIL: 심각한 문제 (수정 필수)

---

### 2️⃣ Python Lint (`python-lint.yml`)

**언제 실행되나?**
- 모든 push (main 브랜치)
- Python 스크립트 변경 시

**무엇을 검증하나?**
```
🎨 Black (코드 포매팅)
   └─ 일관된 코드 스타일

📦 isort (import 정렬)
   └─ 정렬된 import 문

🔍 Flake8 (린팅)
   ├─ 스타일 가이드
   ├─ 오류 감지
   └─ 복잡도 검사

🔎 PyLint (상세 분석)
   └─ 에러와 치명적 오류

🔬 MyPy (타입 검사)
   └─ Python 타입 힌트 검증

✅ 문법 검증
   └─ Python 문법 오류 확인
```

**결과**
- ✅ 모든 검사 통과
- ⚠️ 경고 (권장 수정)
- ❌ 실패 (수정 필수)

---

### 3️⃣ Markdown Validation (포함됨)

**무엇을 검증하나?**
```
📝 UTF-8 인코딩
✓ 제목 구조
🔗 링크 기본 검증
```

---

## 🚀 사용 방법

### 자동 실행 (푸시 시)

```bash
# 회의 파일 변경
git add obsidian-vault/Meetings/2026-08-17-*.md
git commit -m "feat: Add new meeting notes"
git push origin main

# 자동으로 GitHub Actions 실행됨
```

### 수동 실행 (GitHub)

1. GitHub 저장소 접속
2. "Actions" 탭 클릭
3. 원하는 워크플로우 선택
4. "Run workflow" 클릭

### PR에서 자동 검증

```bash
# PR 생성 시
git push origin my-branch
# PR 열기

# 자동으로 모든 검증 실행
# ✅ 검증 통과 시 PR merge 가능
# ❌ 검증 실패 시 수정 필요
```

---

## 📊 결과 확인

### GitHub 대시보드

```
Actions → [워크플로우명]
├─ ✅ All checks passed
│  └─ Job 1: Wiki Validation ✅
│  └─ Job 2: Python Lint ✅
│  └─ Job 3: Markdown Validation ✅
│
└─ 실행 시간: ~2-3분
```

### PR 체크

PR 페이지에서:
```
✅ Wiki Validation — passed
✅ Python Lint & Type Check — passed
✅ Validate Markdown Links — passed

All checks passed — Ready to merge
```

### 상세 리포트

각 Job 클릭 시:
```
📝 Logs
├─ Wiki Validation Report
├─ Python Validation Report
└─ Markdown Validation Report
```

---

## 🔧 커스터마이징

### 스케줄 변경

`.github/workflows/wiki-validation.yml`에서:

```yaml
schedule:
  # 매일 09:00 UTC
  - cron: '0 9 * * *'

  # 매주 월요일
  - cron: '0 9 * * 1'

  # 매달 첫 날
  - cron: '0 9 1 * *'
```

### 실행 조건 변경

```yaml
on:
  push:
    branches: [main, develop]  # 여러 브랜치
    paths:
      - 'obsidian-vault/**'    # 특정 경로만
```

### 린트 규칙 수정

```yaml
flake8 scripts/ \
  --max-line-length=100        # 라인 길이
  --ignore=E501,W503           # 무시할 규칙
```

---

## ⚠️ 문제 해결

### "Workflow failed"

**원인**: 검증 실패

**해결**:
1. "Details" 클릭
2. 실패한 Job 확인
3. 로그에서 오류 메시지 찾기
4. 로컬에서 수정
5. 다시 푸시

예시:
```
❌ Wiki Validation failed
   └─ 2026-08-17-meeting.md is missing Frontmatter

해결: 파일에 YAML 헤더 추가
---
date: 2026-08-17
type: meeting
status: ✅
enhanced_date: 2026-08-17
---
```

### "Action not triggered"

**확인사항**:
1. 파일이 `paths` 조건 충족하는가?
2. 브랜치가 `on.push.branches`에 있는가?
3. `.github/workflows/` 파일이 main에 머지되었는가?

### "API rate limit exceeded"

**해결**: GitHub Actions는 무제한 무료

만약 에러가 뜨면:
1. workflow 파일 문법 확인
2. Actions 로그에서 오류 확인

---

## 📈 모니터링

### GitHub Actions 대시보드

```
Settings → Actions → General
├─ 워크플로우 사용량 확인
├─ 최근 실행 히스토리
└─ 비용 (무료)
```

### 실행 시간

```
Wiki Validation:        ~1-2분
Python Lint:            ~1-2분
Markdown Validation:    ~30초

전체:                   ~2-3분
```

### 성공률 추적

```
Actions 탭에서:
├─ 성공: ✅ 100개
├─ 실패: ❌ 0개
└─ 성공률: 100% ✅
```

---

## 🎯 Best Practices

### 1. 로컬에서 먼저 테스트

```bash
# 로컬에서 validate-wiki.py 실행
python3 scripts/validate-wiki.py ./obsidian-vault/Meetings/

# Black으로 포매팅 확인
black scripts/

# 커밋 전 검증
git status
```

### 2. PR 만들기 전에

```bash
# 최신 main 동기화
git fetch origin
git rebase origin/main

# 로컬 검증 실행
python3 scripts/validate-wiki.py ./obsidian-vault/Meetings/

# PR 생성
gh pr create --title "feat: Add meeting notes"
```

### 3. 정기 검증 모니터링

```
매주 월요일 09:00 UTC:
├─ 전체 Wiki 파일 검증
├─ 오래된 파일 업데이트 확인
└─ 스타일 일관성 체크
```

---

## 📋 체크리스트

GitHub Actions 설정 확인:

```
[ ] .github/workflows/wiki-validation.yml 생성됨
[ ] .github/workflows/python-lint.yml 생성됨
[ ] main 브랜치에 푸시됨
[ ] GitHub Actions 탭에서 워크플로우 보임
[ ] 첫 실행이 성공함
[ ] PR에서 자동 검증 작동함
[ ] 스케줄 워크플로우가 활성화됨
```

---

## 🚀 다음 단계

1. ✅ 워크플로우 파일 main 머지
2. ✅ 첫 검증 실행 확인
3. ⏳ 정기적으로 모니터링
4. ⏳ 필요시 규칙 커스터마이징

---

**버전**: 1.0  
**생성일**: 2026-08-10  
**상태**: ✅ 준비 완료

🎉 **자동화된 CI/CD 파이프라인 설정 완료!**
