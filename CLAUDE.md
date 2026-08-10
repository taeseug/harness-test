# 🎯 CLAUDE.md - 프로젝트 규칙

> Obsidian 기반 회의 관리 시스템 개발 규칙 & 가이드라인

---

## 📋 프로젝트 정보

- **이름**: 회의 기록 & 액션 추적 자동화 시스템
- **기술 스택**: Obsidian, Claude API, Python, Dataview
- **상태**: Phase 3B 진행 중 (2026-08-10~17)
- **목표**: 2026-08-17 첫 회의 테스트 완료

---

## ✅ 해야 할 규칙

### 📁 파일 & 폴더 구조

```
✅ docs/              # 모든 문서
   ├─ guides/        # 설정 가이드
   ├─ references/    # 참고 문서
   └─ handover/      # 세션 정리

✅ scripts/           # 자동화 스크립트
✅ obsidian-vault/    # Obsidian 메인 시스템
✅ llm-ssot/          # 원본 데이터
```

**규칙:**
- 모든 md 파일은 `docs/` 하위 폴더에 보관
- 자동화 스크립트는 `scripts/` 폴더에 보관
- 루트에는 README.md, CLAUDE.md만 허용
- 새 폴더 추가 시 구조도 업데이트

### 📝 커밋 메시지

**형식:**
```
<type>: <description>

<상세 내용>

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
```

**타입:**
- `feat`: 새 기능 (Phase 3A, 3B, 3C 등)
- `fix`: 버그 수정
- `docs`: 문서 추가/수정
- `refactor`: 구조 정리
- `test`: 테스트 추가
- `chore`: 유지보수

**예시:**
```
feat: Phase 3C 완료 - Dataview 쿼리 설정

✅ QUERIES.md 생성
✅ 3개 쿼리 추가 (액션, 회의, 결정)
✅ 렌더링 확인

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
```

### 🔄 Phase 진행 순서

```
✅ Phase 1: 설계 (완료)
✅ Phase 2: 계획 (완료)
🟡 Phase 3: 구현 (진행 중)
   ✅ 3A: Obsidian 설정
   ✅ 3B: 문서 마이그레이션
   ⏳ 3C: Dataview 쿼리
   ⏳ 3D: Claude API 자동화
   ⏳ 3E: 최종 검증
   ⏳ 3F: 첫 회의 테스트 (2026-08-17)
```

**규칙:**
- Phase는 순서대로 진행 (스킵 금지)
- 각 Phase 완료 후 커밋
- Phase 진행 상황을 README.md에 업데이트
- 완료 체크리스트는 SUCCESS_CRITERIA.md 참고

### 🧪 테스트 우선

**규칙:**
- 로컬에서 먼저 테스트 후 커밋
- 자동화 스크립트는 실행 후 결과 확인
- Obsidian은 실제로 열어서 검증
- 마이그레이션/분석은 로그 확인

**테스트 순서:**
```
1. 문법 검증 (Python: py_compile)
2. 의존성 확인 (필요한 라이브러리 import)
3. 실행 테스트 (스크립트 실행)
4. 결과 검증 (로그/파일 확인)
5. 커밋 (완료 후)
```

### 📚 문서화

**규칙:**
- 모든 변경사항은 커밋 메시지로 기록
- Phase 완료마다 진행도 업데이트
- 새 파일/기능 추가 시 README.md 업데이트
- 문제 해결 방법은 TROUBLESHOOTING.md에 추가

**문서 위치:**
- 설정 가이드: `docs/guides/`
- 참고 자료: `docs/references/`
- 세션 정리: `docs/handover/`

### 🔗 링크 관리

**규칙:**
- Obsidian 링크는 `[[파일명]]` 형식 사용
- 문서 간 참조는 상대 경로 사용
- 링크 검증 결과는 메타데이터에 기록
- 깨진 링크는 마이그레이션 로그에 기록

### 🚀 배포 & 푸시

**규칙:**
- 로컬 테스트 완료 후 커밋
- 커밋 전 `git status` 확인
- 선택적으로 파일 추가 (git add -A 금지)
- 백업/임시 폴더는 .gitignore 확인
- 모든 커밋 후 `git push origin main`

**확인 체크리스트:**
```
[ ] 테스트 완료
[ ] 문서 업데이트
[ ] git status 확인
[ ] 커밋 메시지 작성
[ ] git push 실행
```

### 💬 API & 환경변수

**규칙:**
- `ANTHROPIC_API_KEY`는 환경변수로만 관리
- .env 파일은 .gitignore에 포함
- API 키는 절대 코드에 하드코딩 금지
- 로컬 설정은 README.md의 "4️⃣ Claude API 설정" 참고

---

## ❌ 하지 말아야 할 규칙

### 🚫 파일 구조

```
❌ 루트에 md 파일 흩어놓기
   대신: docs/ 폴더 구조 유지

❌ 자동화 스크립트를 다른 곳에 보관
   대신: scripts/ 폴더에만 보관

❌ 큰 파일을 git에 커밋
   대신: .gitignore 확인, 필요시 LFS 사용

❌ 백업/임시 폴더 커밋
   대신: vault_backup_* 제외
```

### 🚫 개발 프로세스

```
❌ 테스트 없이 바로 커밋
   대신: 로컬에서 먼저 검증

❌ 자동화 스크립트 무조건 신뢰
   대신: 로그 확인, 결과 검증

❌ 큰 변경을 한 번에 커밋
   대신: 단계별로 작은 커밋

❌ 동의 없이 프로젝트 구조 변경
   대신: 변경 전 상의
```

### 🚫 커밋 & 메시지

```
❌ 빈 커밋 메시지
   대신: 상세한 설명 포함

❌ "수정됨", "업데이트" 같은 모호한 메시지
   대신: 구체적인 변경사항 기술

❌ 코드 리뷰 없이 푸시
   대신: 테스트 → 커밋 → 검토 → 푸시

❌ Squash 커밋 (과정 숨김)
   대신: 각 단계별 커밋 기록
```

### 🚫 문서화

```
❌ 변경했는데 문서 미업데이트
   대신: 코드 변경 = 문서 변경

❌ 오래된 정보 방치
   대신: 최신 상태 유지

❌ Phase 진행도 미기록
   대신: 각 Phase 완료마다 업데이트

❌ 문제 해결 방법 기록 안 함
   대신: TROUBLESHOOTING.md에 추가
```

### 🚫 API & 보안

```
❌ API 키를 코드에 하드코딩
   대신: 환경변수 사용

❌ 민감정보 로그에 출력
   대신: API 키는 마스킹

❌ .env 파일을 git에 커밋
   대신: .gitignore 확인

❌ 테스트용 API 키 노출
   대신: 로컬에서만 사용
```

### 🚫 데이터 무결성

```
❌ 마이그레이션 없이 데이터 이동
   대신: migrate-docs-advanced.py 사용

❌ 백업 없이 변경
   대신: 자동 백업 확인

❌ 링크 검증 없이 파일 정리
   대신: 마이그레이션 로그 확인

❌ 원본 데이터 직접 수정
   대신: llm-ssot/ 원본 보존
```

---

## 🎯 상황별 행동 가이드

### 새 기능 추가할 때

```
1. Phase 확인 (현재 3C?)
2. 로컬에서 구현 & 테스트
3. 커밋 메시지 작성 (feat: ...)
4. 문서 업데이트 (README.md)
5. git push
```

### 버그 찾았을 때

```
1. TROUBLESHOOTING.md에 기록
2. 로컬에서 재현 & 수정
3. 커밋 메시지 작성 (fix: ...)
4. 테스트 재실행
5. git push
```

### 구조 변경할 때

```
1. CLAUDE.md에서 승인 확인
2. 변경 범위 정의
3. 폴더 정리 (git mv 사용)
4. README.md 업데이트
5. 한 번의 refactor 커밋으로 통합
6. git push
```

### 로컬 테스트할 때

```
1. docs/guides/OBSIDIAN_SETUP_GUIDE.html 참고
2. 각 단계 검증 (체크리스트)
3. 문제 발생 → TROUBLESHOOTING.md 확인
4. 테스트 완료 → 커밋
5. 추가 작업 필요 → 반복
```

---

## 📊 체크리스트 (매 커밋마다)

```
커밋 전:
[ ] 로컬 테스트 완료
[ ] git status 확인
[ ] 불필요한 파일 없음 (캐시, 백업)
[ ] README.md 최신화
[ ] Phase 진행도 확인

커밋:
[ ] 선택적 파일 추가 (git add <file>)
[ ] 커밋 메시지 작성 (conventional commits)
[ ] 메시지에 Co-Authored-By 포함

푸시:
[ ] git push origin main
[ ] GitHub 저장소 확인
[ ] 파일이 올바르게 반영됨
```

---

## 🚀 다음 단계 (2026-08-10~17)

| 날짜 | Phase | 작업 | 상태 |
|------|-------|------|------|
| 8/10-11 | 3A | Obsidian 설정 | ✅ |
| 8/12-13 | 3B | 문서 마이그레이션 | ✅ |
| 8/14 | 3C | Dataview 쿼리 | ⏳ |
| 8/15 | 3D | Claude API | ⏳ |
| 8/16 | 3E | 최종 검증 | ⏳ |
| 8/17 | 3F | 첫 회의 테스트 | 🎯 |

---

## 📞 기타 규칙

### 파일 이름 규칙

```
✅ 설정 가이드: SETUP_*.md, *_GUIDE.md
✅ 참고 문서: *_CRITERIA.md, TROUBLESHOOTING.md
✅ 자동화 스크립트: *-*.py (snake_case)
✅ 회의록: YYYY-MM-DD-*.enhanced.md
```

### 주석 & 로깅

```
✅ Python 스크립트: logging 모듈 사용
✅ 색상 출력: 진행/완료/오류 구분
✅ 자세한 로그: 문제 진단 가능하도록
❌ print() 직접 사용 금지 (logging 사용)
```

### Git 작업 흐름

```
1. 변경 작업
2. 로컬 테스트
3. git add <files>
4. git commit -m "..."
5. git push origin main
6. GitHub 확인
```

---

## ✍️ 마지막 원칙

> **단순성**: 복잡한 것을 간단하게  
> **명확성**: 모호함을 없애기  
> **추적성**: 모든 변경을 기록하기  
> **안정성**: 테스트 후 배포하기  
> **협력성**: 문서로 소통하기

---

**작성일**: 2026-08-10  
**버전**: 1.0  
**상태**: 🟢 활성
