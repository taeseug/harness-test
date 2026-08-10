# 🚀 로컬 Obsidian 설치 & 구성 가이드

**목표**: 로컬 머신에서 Obsidian Vault 완전히 구성  
**소요시간**: 약 2-3시간  
**난이도**: 초급~중급

---

## 📋 사전 확인

### 시스템 요구사항

```
✅ macOS (10.13+) 또는 Windows/Linux
✅ 2GB 이상 RAM
✅ 500MB 이상 디스크 여유
✅ 인터넷 연결
```

### 현재 준비 상황

```
✅ Vault 폴더 구조: 준비됨
  └─ /Users/mac/work/claude/20260810_harness/obsidian-vault/

✅ 설정 파일: 준비됨
  └─ vault.json (플러그인 설정)

✅ 플러그인 설정 가이드: 준비됨
  └─ PLUGINS_SETUP.md

✅ 템플릿: 준비될 예정
```

---

## 🔧 Step 1: Obsidian 설치 (5분)

### 1️⃣ 공식 웹사이트에서 다운로드

```
https://obsidian.md/download
```

**macOS 선택**:
- 최신 버전 (Intel 또는 Apple Silicon)

### 2️⃣ 설치

**macOS**:
```
1. DMG 파일 다운로드
2. Applications 폴더로 드래그
3. Obsidian 실행
```

**Windows/Linux**:
```
1. 설치 파일 다운로드
2. 설치 마법사 따라하기
3. 완료 후 실행
```

### 3️⃣ 초기 설정

Obsidian 시작 시:
```
Create new vault
또는
Open existing vault (다음 단계에서)
```

---

## 📁 Step 2: Vault 열기 (2분)

### 1️⃣ "Open folder as vault" 선택

```
Obsidian 시작 화면
→ "Open folder as vault" 버튼
→ 폴더 선택
```

### 2️⃣ 폴더 경로 입력

```
/Users/mac/work/claude/20260810_harness/obsidian-vault
```

**또는 Finder에서**:
```
1. Finder → 위 경로로 이동
2. obsidian-vault 폴더 우클릭
3. 우측 클릭 메뉴에서 "Open with → Obsidian"
```

### 3️⃣ 신뢰 확인

Obsidian이 vault를 열 때:
```
"Trust author and enable restricted mode"
→ Yes, trust author
```

### 결과

```
✅ Obsidian이 obsidian-vault 폴더를 Vault로 인식
✅ 좌측 파일 탐색기에 폴더 구조 표시됨
```

---

## 🔌 Step 3: 플러그인 설치 (30분)

### 기본 설정

```
Obsidian → Settings (좌측 하단 톱니바퀴)
→ Community Plugins → Turn on community plugins
```

### 설치 순서

#### 1️⃣ Dataview (필수)

```
Settings → Community Plugins
→ Browse 클릭
→ "dataview" 검색
→ Install 클릭
→ Enable 클릭
```

**초기 설정**:
```
Settings → Dataview
├─ Enable JavaScript queries: ✅
├─ Enable Inline Queries: ✅
└─ Save
```

#### 2️⃣ Templater (필수)

```
Settings → Community Plugins
→ Browse
→ "templater" 검색
→ Install → Enable
```

**초기 설정**:
```
Settings → Templater
├─ Template folder location: Templates
├─ Trigger Templater on new file creation: ✅
└─ Save
```

#### 3️⃣ Breadcrumbs (선택)

```
Browse → "breadcrumbs" 검색 → Install → Enable
```

#### 4️⃣ Calendar (선택)

```
Browse → "calendar" 검색 → Install → Enable
```

#### 5️⃣ Checklist (선택)

```
Browse → "checklist" 검색 → Install → Enable
```

#### 6️⃣ Periodic Notes (필수)

```
Browse → "periodic notes" 검색 → Install → Enable
```

**초기 설정**:
```
Settings → Periodic Notes
Daily Notes:
├─ Folder: Daily
└─ Format: YYYY-MM-DD

Weekly Notes:
├─ Folder: Weekly
└─ Format: YYYY-[W]WW

Save
```

---

## 📝 Step 4: 템플릿 생성 (15분)

### Templates 폴더 확인

```
vault.json에 지정된 Templates 폴더
→ obsidian-vault/Templates/
```

폴더가 없으면 수동으로 생성:
```
Obsidian 좌측 탐색기
→ New folder (아이콘)
→ 이름: Templates
```

### 회의 템플릿 생성

**파일명**: `meeting-new.md`

**경로**: `obsidian-vault/Templates/meeting-new.md`

**내용**:
```markdown
# 📅 <% tp.date.now("YYYY-MM-DD") %> 회의

## 📊 회의 정보
| 항목 | 내용 |
|------|------|
| **날짜** | <% tp.date.now("YYYY-MM-DD") %> |
| **의장** | [이름] |
| **참석자** | [참석자 목록] |
| **기록자** | [이름] |

## 📝 논의 내용

### 안건 1: 
**배경**: 

**의견**: 
- **[담당자]**: 

**토론 요점**:
- 

**결정**: 

---

## ✅ 결정사항

✅ **결정-001**: [결정 내용]
- 담당자: [[담당자]]
- 마감일: YYYY-MM-DD
- 근거: 
- 영향도: [[SSOT-rule]]
- 상태: ⏳

---

## 📌 액션 아이템

- [ ] **[[담당자]]** - [작업] (마감: YYYY-MM-DD)
- [ ] **[[담당자]]** - [작업] (마감: YYYY-MM-DD)

---

## 🔗 SSOT 영향

- [[결제-연동]]
- [[온보딩-개선]]

---

## 📎 참고자료

- [[ACTION_ITEMS]]
- [[DASHBOARD]]
```

### Daily 템플릿 생성

**파일명**: `daily.md`

**경로**: `obsidian-vault/Templates/daily.md`

**내용**:
```markdown
# 📅 <% tp.date.now("YYYY-MM-DD") %>

## 📋 오늘 할 일
- [ ] 
- [ ] 
- [ ] 

## 📊 진행 현황

### 결제 연동
- 

### 온보딩 개선
- 

### 기타
- 

## 🎯 우선순위
1. 
2. 
3. 

## 📝 메모
- 

## 🏁 오늘의 회고
- 좋았던 점: 
- 개선점: 
- 내일 포커스: 
```

### 템플릿 확인

Obsidian에서:
```
Settings → Templater
→ Template files
→ meeting-new, daily 표시됨
```

---

## ✅ Step 5: 동기화 & 검증 (15분)

### 문서 마이그레이션

#### SSOT 문서 복사

```
소스: llm-ssot/SSOT.md 등
대상: obsidian-vault/SSOT/
```

명령어:
```bash
cp llm-ssot/SSOT.md obsidian-vault/SSOT/
cp llm-ssot/model-selection.md obsidian-vault/SSOT/
# ... 나머지 파일들
```

#### Meetings 문서 복사

```
소스: llm-ssot/Meetings/*.enhanced.md
대상: obsidian-vault/Meetings/
```

명령어:
```bash
cp llm-ssot/Meetings/*.enhanced.md obsidian-vault/Meetings/
cp llm-ssot/Meetings/ACTION_ITEMS.md obsidian-vault/Meetings/
```

#### Wiki 문서 복사

```
소스: llm-ssot/WIKI/*.md
대상: obsidian-vault/Decisions/
```

명령어:
```bash
cp llm-ssot/WIKI/DECISIONS.md obsidian-vault/Decisions/
# ... 나머지 Wiki 파일들
```

### Obsidian 재로드

```
Settings → Plugins
→ Community plugins 재로드
→ 또는 Obsidian 재시작
```

### 문서 링크 확인

Obsidian에서:
```
1. 아무 문서 열기
2. [[문서명]] 입력해보기
3. 자동완성 제안 확인
4. 링크 클릭 시 문서 열림?
```

---

## 🧪 Step 6: 기능 테스트 (15분)

### 플러그인 동작 확인

#### Dataview 테스트

```
1. 아무 문서에서 코드블록 생성
2. ```dataview 입력
3. 간단한 쿼리 작성:
   LIST
   FROM "Meetings"
4. 결과 표시됨?
```

#### Templater 테스트

```
Cmd+P (또는 Ctrl+P)
→ "Insert template" 입력
→ meeting-new 선택
→ 템플릿 자동 생성됨?
```

#### Daily Note 테스트

```
Cmd+P
→ "Periodic Notes: Open today note"
→ Daily/2026-08-10.md 생성됨?
```

#### Calendar 확인

```
왼쪽 사이드바에 달력 표시됨?
날짜 클릭하면 Daily Note 열림?
```

---

## 📊 설정 확인 체크리스트

### 플러그인 활성화

```
✅ Dataview: 활성화됨
✅ Templater: 활성화됨
✅ Breadcrumbs: 활성화됨 (선택)
✅ Calendar: 활성화됨 (선택)
✅ Checklist: 활성화됨 (선택)
✅ Periodic Notes: 활성화됨
```

### 폴더 구조

```
✅ obsidian-vault/
  ├─ .obsidian/
  ├─ SSOT/
  ├─ Meetings/
  ├─ Decisions/
  ├─ Templates/ (meeting-new.md, daily.md)
  ├─ Daily/
  └─ Weekly/
```

### 문서 마이그레이션

```
✅ SSOT 문서 복사됨
✅ Meetings 문서 복사됨
✅ Wiki/Decisions 복사됨
✅ ACTION_ITEMS 복사됨
```

### 링크 작동

```
✅ [[문서명]] 자동완성 작동
✅ 링크 클릭 시 문서 열림
✅ 문서 이름 변경 시 자동 업데이트
```

### 쿼리 작동

```
✅ Dataview 쿼리 실행됨
✅ 결과 표시됨
✅ 동적 업데이트 작동
```

---

## 🎯 다음 단계

### 즉시 (오늘)

- [ ] Obsidian 설치
- [ ] Vault 열기
- [ ] 플러그인 설치 (6개)
- [ ] 템플릿 생성
- [ ] 문서 마이그레이션

### 내일 (2026-08-11)

- [ ] 기능 테스트
- [ ] Dataview 쿼리 작성
- [ ] 링크 구조 검증

### 준비 (2026-08-17까지)

- [ ] 첫 회의 준비
- [ ] 자동화 스크립트 검증
- [ ] 팀 알림 설정

---

## 🔧 트러블슈팅

### "Vault를 열 수 없음"

```
해결:
1. 폴더 경로 확인 (공백, 특수문자 없음)
2. 폴더 권한 확인 (읽기/쓰기 가능한지)
3. .obsidian 폴더가 있는지 확인
4. Obsidian 재시작
```

### "플러그인 설치 안 됨"

```
해결:
1. 인터넷 연결 확인
2. Community Plugins 활성화 확인
3. 플러그인 이름 정확히 확인
4. Obsidian 업데이트 확인
```

### "템플릿이 자동 생성 안 됨"

```
해결:
1. Templates 폴더명 정확히 확인
2. 파일 이름 정확히 확인 (예: meeting-new.md)
3. Templater 설정에서 "Trigger on file creation" ✅
4. Templater 재활성화
```

### "Daily Note가 생성 안 됨"

```
해결:
1. Periodic Notes 활성화 확인
2. Daily 폴더가 있는지 확인
3. Cmd+P → "Periodic Notes: Open today note" 직접 실행
4. Obsidian 재시작
```

---

## 📞 필요 시 연락

만약 설치 중에 문제가 생기면:

```
1. handover/SESSION_2_SUMMARY.md 읽기
2. PLUGINS_SETUP.md 상세 가이드 참고
3. 각 플러그인 공식 문서 확인
4. Obsidian 커뮤니티 포럼 검색
```

---

## ⏰ 예상 일정

```
2026-08-10: 설치 & 기본 구성 (2-3시간)
2026-08-11~15: 문서 마이그레이션 & 테스트 (2-3시간)
2026-08-16: 최종 검증 (30분)
2026-08-17: 첫 회의 테스트 🎯
```

---

## 🎉 완료했을 때

```
✅ Obsidian Vault 완전히 구성됨
✅ 6가지 플러그인 모두 활성화
✅ 템플릿 자동 생성 작동
✅ [[링크]] 자동 완성 작동
✅ 모든 문서 마이그레이션됨
✅ 첫 회의 준비 완료
```

이제 2026-08-17의 첫 회의를 준비할 수 있습니다! 🚀

---

**생성일**: 2026-08-10  
**예상 완료**: 2026-08-16  
**목표**: 첫 회의 테스트 (2026-08-17)
