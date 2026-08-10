# ✅ Obsidian 설정 체크리스트

**목표**: 로컬 Obsidian 완전 구성  
**대상**: 사용자 (로컬 작업)  
**예상 시간**: 2-3시간  
**난이도**: 초급~중급  
**완료 기준**: 모든 항목 ✅

---

## 📋 Phase 3A: Obsidian 설치 & 기본 설정 (30분)

### Step 1: Obsidian 설치

- [ ] macOS 또는 Windows/Linux 선택
- [ ] 공식 웹사이트에서 다운로드: https://obsidian.md/download
- [ ] 설치 파일 실행
- [ ] 응용프로그램 폴더로 이동 (macOS)

**확인**: Obsidian 아이콘이 도크/시작메뉴에 표시됨

---

### Step 2: Vault 열기

- [ ] Obsidian 실행
- [ ] "Open folder as vault" 선택
- [ ] 경로 입력: `/Users/mac/work/claude/20260810_harness/obsidian-vault`
- [ ] "신뢰" 선택 (Trust author)

**확인**: 
- [ ] Vault 열림
- [ ] 좌측 파일 탐색기에 폴더 구조 표시됨
- [ ] .obsidian 폴더 보임

---

### Step 3: 초기 설정

- [ ] Settings 열기 (좌측 하단 톱니바퀴)
- [ ] 언어 설정: English (또는 한국어)
- [ ] Theme: Default 또는 선호하는 테마 선택
- [ ] Editor 설정: 필요한 옵션만 조정

**확인**:
- [ ] Settings 창이 정상 작동
- [ ] 테마가 적용됨

---

## 📋 Phase 3B: 플러그인 설치 (45분)

### Step 1: Community Plugins 활성화

- [ ] Settings → Community Plugins
- [ ] "Turn on community plugins" 클릭
- [ ] "Browse" 버튼 활성화됨 확인

---

### Step 2: 플러그인 설치 (순서대로)

각 플러그인마다:
1. Browse 클릭
2. 이름 검색
3. Install 클릭
4. Enable 클릭

#### 1️⃣ Dataview (필수)

- [ ] 검색: "dataview"
- [ ] 클릭: "Dataview" by blacksmithgu
- [ ] Install → Enable
- [ ] Settings 확인:
  - [ ] Enable JavaScript queries: ✅
  - [ ] Enable Inline Queries: ✅

**테스트**:
- [ ] 문서 생성하여 ```dataview 입력
- [ ] 쿼리 실행되는지 확인

---

#### 2️⃣ Templater (필수)

- [ ] 검색: "templater"
- [ ] 클릭: "Templater" by SilentVoid
- [ ] Install → Enable
- [ ] Settings 확인:
  - [ ] Template folder location: **Templates**
  - [ ] Trigger on file creation: ✅

**테스트**:
- [ ] Cmd+P → "Insert template"
- [ ] 작동하는지 확인

---

#### 3️⃣ Breadcrumbs (선택)

- [ ] 검색: "breadcrumbs"
- [ ] 클릭: "Breadcrumbs" by SkepticMystic
- [ ] Install → Enable
- [ ] 좌측 사이드바에 그래프 보임 확인

---

#### 4️⃣ Calendar (선택)

- [ ] 검색: "calendar"
- [ ] 클릭: "Calendar" by Kevintab95
- [ ] Install → Enable
- [ ] 좌측 사이드바에 달력 보임 확인

---

#### 5️⃣ Checklist (선택)

- [ ] 검색: "checklist"
- [ ] 클릭: "Checklist" by delashum
- [ ] Install → Enable

**테스트**:
- [ ] 체크박스 생성: `- [ ] item`
- [ ] 클릭 시 체크되는지 확인

---

#### 6️⃣ Periodic Notes (필수)

- [ ] 검색: "periodic notes"
- [ ] 클릭: "Periodic Notes" by Joleary
- [ ] Install → Enable
- [ ] Settings 확인:
  - [ ] Daily Folder: **Daily**
  - [ ] Daily Format: **YYYY-MM-DD**
  - [ ] Weekly Folder: **Weekly**
  - [ ] Weekly Format: **YYYY-[W]WW**

**테스트**:
- [ ] Cmd+P → "Periodic Notes: Open today note"
- [ ] Daily/YYYY-MM-DD.md 생성됨 확인

---

### Step 3: 플러그인 최종 확인

- [ ] Settings → Community Plugins 열기
- [ ] 모든 플러그인 활성화 상태 확인:

| 플러그인 | 상태 | 체크 |
|---------|------|------|
| Dataview | Enabled | [ ] |
| Templater | Enabled | [ ] |
| Breadcrumbs | Enabled | [ ] |
| Calendar | Enabled | [ ] |
| Checklist | Enabled | [ ] |
| Periodic Notes | Enabled | [ ] |

**확인**:
- [ ] 모든 플러그인이 "Enabled" 상태
- [ ] 에러 메시지 없음

---

## 📋 Phase 3C: 템플릿 생성 (30분)

### Step 1: Templates 폴더 확인

- [ ] 좌측 파일 탐색기에서 Templates 폴더 보임
- [ ] 없으면: New folder → "Templates"

---

### Step 2: meeting-new.md 템플릿 생성

**파일 생성**:
- [ ] Templates 폴더 우클릭
- [ ] "New file" 클릭
- [ ] 파일명: `meeting-new.md`

**내용 복사** (LOCAL_SETUP_GUIDE.md의 템플릿 참고):
- [ ] 마크다운 내용 붙여넣기
- [ ] Templater 코드 확인:
  - [ ] `<% tp.date.now("YYYY-MM-DD") %>` 포함

**저장**:
- [ ] Cmd+S 저장

---

### Step 3: daily.md 템플릿 생성

**파일 생성**:
- [ ] Templates 폴더 우클릭
- [ ] "New file" 클릭
- [ ] 파일명: `daily.md`

**내용 복사** (LOCAL_SETUP_GUIDE.md의 템플릿 참고):
- [ ] 마크다운 내용 붙여넣기
- [ ] 필드 확인: 오늘 할 일, 진행 현황, 메모

**저장**:
- [ ] Cmd+S 저장

---

### Step 4: 템플릿 테스트

**meeting-new 테스트**:
- [ ] Cmd+P 입력
- [ ] "Insert template: meeting-new" 선택
- [ ] 새 파일이 자동 생성되는지 확인
- [ ] 날짜가 자동 입력되는지 확인
- [ ] 파일 삭제: Cmd+Delete

**daily 테스트**:
- [ ] Cmd+P 입력
- [ ] "Periodic Notes: Open today note" 선택
- [ ] Daily/YYYY-MM-DD.md 생성 확인
- [ ] 템플릿이 적용되는지 확인

**확인**:
- [ ] meeting-new 자동 생성 ✅
- [ ] daily 자동 생성 ✅
- [ ] 템플릿 내용 정확함 ✅

---

## 📋 Phase 3D: 문서 마이그레이션 (45분)

### Step 1: 마이그레이션 스크립트 실행

**터미널에서**:
```bash
cd /Users/mac/work/claude/20260810_harness
./migrate-docs.sh
```

**진행 확인**:
- [ ] 스크립트 실행 시작
- [ ] 각 단계별 메시지 표시됨
- [ ] 오류 없이 완료

**확인할 메시지**:
- [ ] "Step 1: SSOT 문서 마이그레이션"
- [ ] "Step 2: Meetings 문서 마이그레이션"
- [ ] "Step 3: Wiki/Decisions 문서 마이그레이션"
- [ ] "마이그레이션 완료!" 메시지

---

### Step 2: 마이그레이션 검증

**Obsidian에서 확인**:

| 폴더 | 파일 수 | 체크 | 확인 |
|------|--------|------|------|
| SSOT/ | 4-6개 | [ ] | SSOT.md, model-selection.md 등 |
| Meetings/ | 8-10개 | [ ] | 6개 회의 + ACTION_ITEMS + ANALYSIS |
| Decisions/ | 6개 | [ ] | DECISIONS.md, WIKI_INDEX.md 등 |

---

### Step 3: 파일 링크 확인

- [ ] 임의의 회의 파일 열기
- [ ] [[문서명]] 형식의 링크 확인
- [ ] 링크 클릭 시 해당 문서 열림 확인

**테스트 링크**:
- [ ] [[ACTION_ITEMS]] 클릭
- [ ] [[DASHBOARD]] 클릭
- [ ] [[담당자이름]] 클릭

**확인**:
- [ ] 모든 링크 작동 ✅
- [ ] 깨진 링크 없음 ✅

---

## 📋 Phase 3E: Dataview 쿼리 설정 (30분)

### Step 1: Dataview 쿼리 문서 생성

**파일 생성**:
- [ ] Obsidian에서 새 파일: "QUERIES.md"
- [ ] 루트 또는 WIKI/ 폴더에 저장

---

### Step 2: 주요 쿼리 추가

다음 쿼리들을 QUERIES.md에 추가:

#### 쿼리 1: 진행 중인 액션

```dataview
TASK
WHERE status = "⏳"
GROUP BY due DESC
```

**테스트**:
- [ ] 결과가 표시됨
- [ ] 마감일 순서대로 정렬됨

---

#### 쿼리 2: 회의 타임라인

```dataview
TABLE file.name as "회의", date as "날짜"
FROM "Meetings"
SORT date DESC
```

**테스트**:
- [ ] 회의 목록이 표시됨
- [ ] 최신순 정렬됨

---

#### 쿼리 3: 결정사항 현황

```dataview
TABLE status as "상태", owner as "담당자"
FROM "Decisions"
WHERE type != null
SORT type, status
```

**테스트**:
- [ ] 결정사항이 표시됨
- [ ] 담당자별로 정렬됨

---

### Step 3: 쿼리 검증

**Dataview 작동 확인**:
- [ ] QUERIES.md 파일에 쿼리 3개 모두 표시됨
- [ ] 결과가 테이블 형식으로 렌더링됨
- [ ] 데이터가 올바르게 표시됨

**확인**:
- [ ] 쿼리 1: 액션 목록 ✅
- [ ] 쿼리 2: 회의 목록 ✅
- [ ] 쿼리 3: 결정사항 ✅

---

## 📋 Phase 3F: 최종 검증 (15분)

### Step 1: 전체 시스템 점검

| 항목 | 상태 | 체크 |
|------|------|------|
| **Vault 구조** | | |
| - .obsidian/ | ✅ 있음 | [ ] |
| - SSOT/ | ✅ 있음 | [ ] |
| - Meetings/ | ✅ 있음 | [ ] |
| - Decisions/ | ✅ 있음 | [ ] |
| - Templates/ | ✅ 있음 | [ ] |
| - Daily/ | ✅ 있음 | [ ] |
| - Weekly/ | ✅ 있음 | [ ] |
| **플러그인** | | |
| - Dataview | ✅ 활성화 | [ ] |
| - Templater | ✅ 활성화 | [ ] |
| - Breadcrumbs | ✅ 활성화 | [ ] |
| - Calendar | ✅ 활성화 | [ ] |
| - Checklist | ✅ 활성화 | [ ] |
| - Periodic Notes | ✅ 활성화 | [ ] |
| **템플릿** | | |
| - meeting-new.md | ✅ 생성됨 | [ ] |
| - daily.md | ✅ 생성됨 | [ ] |
| **문서** | | |
| - SSOT 문서 | ✅ 복사됨 | [ ] |
| - Meetings 문서 | ✅ 복사됨 | [ ] |
| - Decisions 문서 | ✅ 복사됨 | [ ] |
| **쿼리** | | |
| - Dataview 쿼리 | ✅ 작동 | [ ] |
| - 링크 작동 | ✅ OK | [ ] |

---

### Step 2: 기능 테스트

**템플릿 테스트**:
- [ ] Cmd+P → "Insert template: meeting-new"
- [ ] 새 파일이 생성되고 날짜가 자동 입력됨
- [ ] 파일 삭제

**Daily Note 테스트**:
- [ ] Cmd+P → "Periodic Notes: Open today note"
- [ ] Daily/오늘날짜.md가 생성됨
- [ ] 템플릿 내용이 자동 입력됨

**링크 테스트**:
- [ ] 회의 파일에서 [[ACTION_ITEMS]] 클릭
- [ ] ACTION_ITEMS.md 파일로 이동됨
- [ ] [[담당자]] 링크도 자동 완성 작동 확인

**검색 테스트**:
- [ ] Cmd+P (또는 Ctrl+P)
- [ ] 문서명 입력하여 검색
- [ ] 검색 결과가 표시됨

**그래프 보기 테스트**:
- [ ] Cmd+Shift+G (또는 메뉴 → Graph view)
- [ ] 문서들의 관계도 시각화됨

---

### Step 3: 성공 기준 확인

모든 항목에 체크가 되어 있는가?

```
최종 점수:
✅ 50-60개 체크 → 성공! 🎉
⚠️ 40-49개 체크 → 대부분 성공 (트러블슈팅 필요)
❌ 40개 미만 → 문제 있음 (지원 필요)
```

---

## 🆘 문제 해결

### 문제 1: "Vault를 열 수 없음"

**해결**:
1. 폴더 경로 다시 확인
2. 폴더 권한 확인 (읽기/쓰기)
3. Obsidian 재시작

---

### 문제 2: "플러그인 설치 안 됨"

**해결**:
1. 인터넷 연결 확인
2. Community Plugins 활성화 확인
3. 플러그인 이름 정확히 확인
4. Obsidian 업데이트

---

### 문제 3: "템플릿 자동 생성 안 됨"

**해결**:
1. Templates 폴더명 확인 (정확히 "Templates")
2. Templater 설정에서 "Trigger on file creation" 확인
3. Templater 재활성화

---

### 문제 4: "쿼리가 실행 안 됨"

**해결**:
1. Dataview 활성화 확인
2. 문서 저장 (Cmd+S)
3. 문서 새로고침
4. Dataview 재활성화

---

## ✅ 완료 체크리스트

- [ ] 모든 Phase 완료
- [ ] 모든 플러그인 활성화
- [ ] 모든 템플릿 생성
- [ ] 모든 문서 마이그레이션
- [ ] 모든 쿼리 작동
- [ ] 모든 링크 작동
- [ ] 성공 기준 50개 이상 체크

---

## 🎉 완료!

모든 체크리스트를 완료했다면 **Obsidian 시스템 구성이 완료**되었습니다!

**다음 단계**:
- 🗓️ 2026-08-17 첫 회의 테스트 준비
- 📋 PHASE3_EXECUTION_GUIDE.md 참고
- 💬 Slack 알림 설정 (선택)

---

**생성일**: 2026-08-10  
**예상 소요시간**: 2-3시간  
**난이도**: 초급~중급  
**지원**: LOCAL_SETUP_GUIDE.md 참고
