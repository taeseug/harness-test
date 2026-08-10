# 🚀 PR 자동 생성 스크립트 가이드

> **GitHub PR을 자동으로 생성해주는 Python 스크립트**  
> 커밋 분석 → PR 제목 자동화 → 설명 생성 → PR 생성

---

## 📋 개요

`scripts/create-pr.py`는 다음을 자동으로 처리합니다:

- ✅ 현재 브랜치 확인
- ✅ Base 브랜치와의 커밋 차이 분석
- ✅ PR 제목 자동 제안
- ✅ PR 설명 자동 생성
- ✅ GitHub PR 자동 생성
- ✅ 성공 후 PR URL 출력

---

## 🚀 빠른 시작

### 1️⃣ 사전 요구사항

```bash
# GitHub CLI 설치 확인
gh --version

# 설치 필요 시:
# macOS: brew install gh
# Windows: choco install gh
# Linux: https://cli.github.com/
```

### 2️⃣ 기본 사용법

```bash
# 대화형 모드 (추천) ⭐
python3 scripts/create-pr.py --interactive

# 기본 (자동 제목 생성)
python3 scripts/create-pr.py

# 미리보기만
python3 scripts/create-pr.py --dry-run

# 커스텀 제목
python3 scripts/create-pr.py --title "feat: 새로운 기능"

# develop 브랜치로 PR
python3 scripts/create-pr.py --base develop
```

---

## 📖 자세한 사용법

### 모드별 사용

#### 🎯 대화형 모드 (추천)

```bash
python3 scripts/create-pr.py --interactive
```

**단계별:**
1. 현재 브랜치 확인
2. Base 브랜치 확인
3. 커밋 목록 표시
4. **PR 제목 입력** (사용자 입력)
5. PR 미리보기 표시
6. **생성 확인** (yes/no 선택)
7. PR 생성 및 URL 출력

**예시:**
```
🚀 GitHub PR 자동 생성
============================================================

📍 현재 브랜치: release/v1.0.0
📍 대상 브랜치: main

📝 커밋 수: 10
최근 커밋:
  07d07c6 feat: GitHub Actions CI/CD 파이프라인 구축
  3c52461 chore: Update Obsidian workspace state
  5efa88c docs: 세션 작업 로그 기록 (2026-08-10)
  ... 외 7개

📝 PR 제목을 입력하세요:
> feat: v1.0.0 - Wiki 검증 시스템 & GitHub Actions

📌 PR 제목: feat: v1.0.0 - Wiki 검증 시스템 & GitHub Actions

────────────────────────────────────────────────────────────
📄 PR 미리보기:
────────────────────────────────────────────────────────────
제목: feat: v1.0.0 - Wiki 검증 시스템 & GitHub Actions

## 📋 Summary

**release/v1.0.0** → **main** (총 10개 커밋)

### FEAT
- GitHub Actions CI/CD 파이프라인 구축
...

────────────────────────────────────────────────────────────
이 내용으로 PR을 생성하시겠습니까? (yes/no): yes

✅ PR 생성 성공!
🔗 PR URL: https://github.com/taeseug/harness-test/pull/1
```

#### 🔍 미리보기 모드

```bash
python3 scripts/create-pr.py --dry-run
```

**용도:**
- PR이 어떻게 생성될지 미리 확인
- 제목/설명 확인
- 실제 생성 전 테스트

**출력:**
```
✅ [DRY-RUN] PR 생성 준비 완료!
============================================================

실행할 명령어:
  gh pr create \
    --base main \
    --head release/v1.0.0 \
    --title "feat: v1.0.0 - Wiki 검증 시스템 & GitHub Actions" \
    --body "..."

옵션 제거:
  --dry-run 옵션을 제거하고 실행하면 실제 PR이 생성됩니다.
```

#### 🎨 커스텀 모드

```bash
# 특정 제목으로 PR 생성
python3 scripts/create-pr.py --title "feat: 내 기능"

# 다른 브랜치로 PR
python3 scripts/create-pr.py --base develop

# 조합
python3 scripts/create-pr.py \
  --base develop \
  --title "feat: 개발 버전 기능" \
  --dry-run
```

---

## 🔧 고급 사용법

### 1. 여러 PR을 순차적으로 생성

```bash
#!/bin/bash

# 첫 번째 PR
git checkout feature/wiki-validation
python3 scripts/create-pr.py --interactive

# 두 번째 PR
git checkout feature/github-actions
python3 scripts/create-pr.py --interactive

# 세 번째 PR
git checkout feature/documentation
python3 scripts/create-pr.py --interactive
```

### 2. 자동화된 CI/CD 파이프라인

```yaml
# .github/workflows/auto-pr.yml
name: Auto PR Creation

on:
  workflow_dispatch:
    inputs:
      branch:
        description: 'Feature branch'
        required: true
      title:
        description: 'PR title'
        required: false

jobs:
  create-pr:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4

      - name: Create PR
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          python3 scripts/create-pr.py \
            --title "${{ inputs.title }}" \
            --dry-run
```

### 3. 커밋 메시지로 PR 제목 자동화

스크립트가 자동으로 첫 커밋의 메시지를 제목으로 사용합니다.

```bash
# 커밋 메시지가 곧 PR 제목
git commit -m "feat: 새로운 기능 추가"

# 이제 이 커밋의 메시지가 PR 제목이 됨
python3 scripts/create-pr.py
→ PR 제목: "feat: 새로운 기능 추가"
```

---

## 📊 PR 생성 흐름

```
┌─────────────────────────┐
│  create-pr.py 실행      │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  현재 브랜치 확인       │
│  Base 브랜치 확인       │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  커밋 분석              │
│  - 커밋 수             │
│  - 메시지 파싱        │
│  - 타입별 분류        │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  PR 제목 결정           │
│  (자동 or 사용자 입력)  │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  PR 설명 자동 생성      │
│  - Summary              │
│  - Changes              │
│  - Test Plan            │
│  - Checklist            │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  미리보기 표시          │
│  (대화형 모드 확인)     │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  브랜치 푸시            │
│  (필요시)               │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  gh pr create 실행      │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  ✅ PR 생성 완료        │
│  🔗 PR URL 출력         │
└─────────────────────────┘
```

---

## 🐛 문제 해결

### "GitHub CLI (gh)가 설치되지 않았습니다"

```bash
# 설치
# macOS
brew install gh

# Windows
choco install gh

# Linux
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo gpg --dearmor -o /usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh
```

### "git 저장소가 아닙니다"

```bash
# 프로젝트 루트에서 실행하는지 확인
pwd
# /Users/mac/work/claude/20260810_harness

ls -la | grep ".git"
# .git이 있는지 확인
```

### "base 브랜치와의 커밋 차이가 없습니다"

```bash
# 커밋 확인
git log --oneline main..HEAD
# 최소 1개 이상의 커밋이 있어야 함

# 없으면: 먼저 커밋 생성
git add .
git commit -m "feat: 새로운 기능"

# 다시 시도
python3 scripts/create-pr.py
```

### "PR 생성 실패"

```bash
# 1. GitHub 인증 확인
gh auth status

# 2. 저장소 접근 권한 확인
gh repo view

# 3. 로그인
gh auth login
```

---

## 📋 옵션 참고

```bash
python3 scripts/create-pr.py --help

선택 사항:
  -h, --help            도움말
  --base BRANCH         Base 브랜치 (기본값: main)
  --title TITLE         PR 제목
  --dry-run             생성하지 말고 미리보기만
  --interactive         대화형 모드 (추천)
```

---

## 🎯 실전 예시

### 예시 1: v1.0.0 릴리스 PR

```bash
# 1. release 브랜치 생성
git checkout -b release/v1.0.0

# 2. PR 생성 (대화형)
python3 scripts/create-pr.py --interactive
> PR 제목 입력: feat: v1.0.0 - Wiki 검증 시스템 & GitHub Actions
> 생성 확인: yes

# 3. PR merge 대기
# GitHub에서 PR 검토 및 merge
```

### 예시 2: 피처 개발

```bash
# 1. feature 브랜치 생성
git checkout -b feature/new-dashboard

# 2. 작업 & 커밋
git add .
git commit -m "feat: 새로운 대시보드 추가"
git commit -m "docs: 대시보드 사용 가이드"

# 3. PR 생성 (자동 제목)
python3 scripts/create-pr.py
> PR 제목: "feat: 새로운 대시보드 추가" (자동 생성)

# 4. develop으로 PR도 가능
python3 scripts/create-pr.py --base develop
```

### 예시 3: 버그 수정

```bash
# 1. fix 브랜치 생성
git checkout -b fix/wiki-validation-bug

# 2. 수정 & 테스트
git add .
git commit -m "fix: Wiki Frontmatter 검증 실패 문제"

# 3. PR 생성 (미리보기)
python3 scripts/create-pr.py --dry-run

# 4. 문제 없으면 실제 생성
python3 scripts/create-pr.py
```

---

## ✅ 체크리스트

PR 생성 전:

```
[ ] GitHub CLI 설치됨 (gh --version)
[ ] GitHub 인증 완료 (gh auth status)
[ ] 현재 브랜치 확인 (git branch)
[ ] 새 커밋 있음 (git log main..HEAD)
[ ] 커밋 메시지 규칙 준수 (feat:, fix:, docs: 등)
[ ] CLAUDE.md 규칙 준수 확인
[ ] 로컬 테스트 완료
```

PR 생성 후:

```
[ ] PR URL 확인
[ ] GitHub에서 PR 자동 검증 대기
[ ] CI/CD 성공 확인
[ ] 코드 리뷰 요청
[ ] Merge 승인 받기
[ ] Merge 실행
```

---

## 🚀 다음 단계

1. ✅ `python3 scripts/create-pr.py --help` 실행
2. ✅ `python3 scripts/create-pr.py --dry-run` 미리보기
3. ✅ `python3 scripts/create-pr.py --interactive` 대화형 모드
4. ✅ GitHub에서 PR 검토 및 merge

---

**버전**: 1.0  
**생성일**: 2026-08-10  
**상태**: ✅ 준비 완료

🎉 **PR 자동 생성 스크립트를 사용해보세요!**
