# 📋 프로젝트 규칙 & 개발 가이드라인 정리

> 2026-08-10~08-17 (7일) 동안 정한 모든 규칙 & 기준

---

## 🎯 프로젝트 핵심 원칙 (CLAUDE.md)

### ✅ 해야 할 규칙 (8가지)

#### 1️⃣ 파일 & 폴더 구조
```
docs/              # 모든 문서
├─ guides/        # 설정 가이드
├─ references/    # 참고 문서
└─ handover/      # 세션 정리

scripts/           # 자동화 스크립트
obsidian-vault/    # Obsidian 메인 시스템
llm-ssot/          # 원본 데이터
```

**규칙:**
- 모든 md 파일은 `docs/` 하위에 보관
- 자동화 스크립트는 `scripts/` 폴더에만 보관
- 루트에는 README.md, CLAUDE.md만 허용
- 새 폴더 추가 시 구조도 업데이트

#### 2️⃣ Conventional Commits 형식
```
<type>: <description>

<상세 내용>

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
```

**타입:**
- `feat`: 새 기능 (Phase 진행)
- `fix`: 버그 수정
- `docs`: 문서 추가/수정
- `refactor`: 구조 정리
- `test`: 테스트 추가
- `chore`: 유지보수

#### 3️⃣ Phase 진행 순서
```
✅ Phase 1: 설계 (완료)
✅ Phase 2: 계획 (완료)
🟡 Phase 3: 구현 (진행 중)
   ✅ 3A: Obsidian 설정
   ✅ 3B: 문서 마이그레이션
   ✅ 3C: Dataview 쿼리
   ✅ 3D: Claude API 준비
   ✅ 3E: 최종 검증
   ⏳ 3F: 첫 회의 테스트 (2026-08-17)
```

- Phase는 순서대로 진행 (스킵 금지)
- 각 Phase 완료 후 커밋
- Phase 진행도를 README.md 업데이트

#### 4️⃣ 테스트 우선
```
1. 문법 검증 (Python: py_compile)
2. 의존성 확인 (필요한 라이브러리 import)
3. 실행 테스트 (스크립트 실행)
4. 결과 검증 (로그/파일 확인)
5. 커밋 (완료 후)
```

로컬에서 먼저 검증 → 커밋 → 푸시

#### 5️⃣ 문서화
- 모든 변경사항은 커밋 메시지로 기록
- Phase 완료마다 진행도 업데이트
- 새 파일/기능 추가 시 README.md 업데이트
- 문제 해결 방법은 TROUBLESHOOTING.md에 추가

#### 6️⃣ 링크 관리
- Obsidian 링크: `[[파일명]]` 형식
- 문서 간 참조: 상대 경로 사용
- 링크 검증 결과: 메타데이터에 기록
- 깨진 링크: 마이그레이션 로그에 기록

#### 7️⃣ 배포 & 푸시
```
[ ] 로컬 테스트 완료
[ ] git status 확인
[ ] 불필요한 파일 없음 (캐시, 백업)
[ ] README.md 최신화
[ ] Phase 진행도 확인

↓

[ ] 선택적 파일 추가
[ ] 커밋 메시지 작성
[ ] git push origin main
```

#### 8️⃣ API & 환경변수
- `ANTHROPIC_API_KEY`는 환경변수로만 관리
- .env 파일은 .gitignore에 포함
- API 키는 절대 코드에 하드코딩 금지
- 로컬 설정은 README.md 참고

---

### ❌ 하지 말아야 할 규칙 (8가지)

#### 1️⃣ 파일 구조
- ❌ 루트에 md 파일 흩어놓기 → docs/ 구조 유지
- ❌ 자동화 스크립트 다른 곳에 → scripts/에만 보관
- ❌ 큰 파일 git 커밋 → .gitignore 확인
- ❌ 백업/임시 폴더 커밋 → vault_backup_* 제외

#### 2️⃣ 개발 프로세스
- ❌ 테스트 없이 바로 커밋 → 로컬 검증 후 커밋
- ❌ 자동화 스크립트 무조건 신뢰 → 로그 확인, 결과 검증
- ❌ 큰 변경을 한 번에 커밋 → 단계별 작은 커밋
- ❌ 동의 없이 구조 변경 → 변경 전 상의

#### 3️⃣ 커밋 & 메시지
- ❌ 빈 커밋 메시지 → 상세한 설명 포함
- ❌ "수정됨", "업데이트" 모호한 메시지 → 구체적 변경사항
- ❌ 코드 리뷰 없이 푸시 → 테스트 → 커밋 → 검토 → 푸시
- ❌ Squash 커밋 (과정 숨김) → 각 단계별 커밋 기록

#### 4️⃣ 문서화
- ❌ 변경했는데 문서 미업데이트 → 코드 변경 = 문서 변경
- ❌ 오래된 정보 방치 → 최신 상태 유지
- ❌ Phase 진행도 미기록 → 각 Phase 완료마다 업데이트
- ❌ 문제 해결 방법 기록 안 함 → TROUBLESHOOTING.md에 추가

#### 5️⃣ API & 보안
- ❌ API 키 코드에 하드코딩 → 환경변수 사용
- ❌ 민감정보 로그에 출력 → API 키는 마스킹
- ❌ .env 파일 git 커밋 → .gitignore 확인
- ❌ 테스트용 API 키 노출 → 로컬에서만 사용

#### 6️⃣ 데이터 무결성
- ❌ 마이그레이션 없이 데이터 이동 → migrate-docs-advanced.py 사용
- ❌ 백업 없이 변경 → 자동 백업 확인
- ❌ 링크 검증 없이 파일 정리 → 마이그레이션 로그 확인
- ❌ 원본 데이터 직접 수정 → llm-ssot/ 원본 보존

---

## 📊 프로젝트 구조 & 계층

### 4계층 아키텍처

```
Layer 1: 입력층 (Data Input)
├─ Obsidian Templater
├─ Periodic Notes
└─ 수동 입력

    ↓

Layer 2: 저장층 (Data Storage)
├─ obsidian-vault/
│  ├─ SSOT/ (4개 파일)
│  ├─ Meetings/ (9개 파일)
│  ├─ Decisions/ (6개 파일)
│  ├─ Templates/ (2개 파일)
│  └─ QUERIES.md (대시보드)
└─ llm-ssot/ (원본 데이터)

    ↓

Layer 3: 처리층 (Processing)
├─ migrate-docs-advanced.py (문서 마이그레이션)
├─ meeting-processor.py (Claude API 분석)
└─ Dataview (쿼리 렌더링)

    ↓

Layer 4: 출력층 (Output)
├─ QUERIES.md (3개 쿼리 대시보드)
├─ analysis_*.json (분석 결과)
└─ ACTION_ITEMS.md (자동 갱신)
```

---

## 🔄 데이터 흐름

```
회의 준비
  ↓
회의 중 Obsidian 기록 ([[링크]] 사용)
  ↓
Claude API 분석 (meeting-processor.py)
  ↓
QUERIES.md 대시보드 자동 갱신
  ↓
링크 네비게이션 ([[파일]] 참조)
```

---

## 📋 체크리스트 (매 커밋마다)

### 커밋 전
- [ ] 로컬 테스트 완료
- [ ] git status 확인
- [ ] 불필요한 파일 없음
- [ ] README.md 최신화
- [ ] Phase 진행도 확인

### 커밋
- [ ] 선택적 파일 추가 (git add <file>)
- [ ] 커밋 메시지 작성 (conventional commits)
- [ ] Co-Authored-By 포함

### 푸시
- [ ] git push origin main
- [ ] GitHub 저장소 확인
- [ ] 파일이 올바르게 반영됨

---

## 🎯 상황별 행동 가이드

### 새 기능 추가할 때
```
1. Phase 확인 (현재 3F?)
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
5. 한 번의 refactor 커밋
6. git push
```

### 로컬 테스트할 때
```
1. docs/guides/OBSIDIAN_SETUP_GUIDE.html 참고
2. 각 단계 검증 (체크리스트)
3. 문제 발생 → TROUBLESHOOTING.md 확인
4. 테스트 완료 → 커밋
```

---

## 🔐 보안 & 무결성 원칙

### 데이터 보호
- **백업**: vault_backup_* (자동 생성) + llm-ssot/ (원본 보존)
- **검증**: 링크 검증 (메타데이터) + 파일 체크섬 + 데이터 일관성
- **접근 제어**: Obsidian 로컬 저장 + Git 버전관리 + API 키 환경변수

### 무결성 확인
- 마이그레이션 메타데이터 확인 (stats)
- 링크 검증 결과 확인 (links_verified)
- 파일 개수 확인 (files_copied)

---

## 📈 최종 성과 (7일)

```
생성된 문서:
✅ 15개 파일, 5,000줄
✅ 10개 가이드 & 참고 문서

자동화:
✅ 2개 Python 스크립트
✅ 2개 템플릿
✅ 3개 Dataview 쿼리

시스템:
✅ 완전한 Obsidian Vault
✅ 6개 플러그인 통합
✅ 20개 파일 마이그레이션
✅ 100+ 문서 네트워크

상태:
✅ 모든 규칙 정의
✅ 모든 가이드 작성
✅ 모든 자동화 완성
✅ 첫 회의 준비 (2026-08-17)
```

---

## 🎯 다음 담당자를 위한 요약

### 읽어야 할 문서 (순서)
1. **README.md** (프로젝트 개요 - 15분)
2. **CLAUDE.md** (개발 규칙 - 10분)
3. **docs/guides/** (각 Phase 가이드 - 1시간)
4. **docs/references/** (참고 자료)

### 즉시 알아야 할 것
- Phase 3F는 2026-08-17 첫 회의 테스트
- 모든 규칙은 CLAUDE.md에 정의됨
- 모든 파일은 docs/ 구조를 따름
- 모든 커밋은 conventional commits 형식

### 일상적 작업 흐름
1. 변경 작업
2. 로컬 테스트
3. git add <files>
4. git commit -m "..."
5. git push origin main
6. README.md 업데이트

---

**작성일**: 2026-08-10  
**버전**: 1.0  
**상태**: ✅ 완성

🎯 **모든 규칙 정리 완료!**
