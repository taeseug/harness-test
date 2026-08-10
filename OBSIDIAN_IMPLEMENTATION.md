# 🎯 Obsidian Vault 구현 계획

**상태**: 🟡 Phase 2 (구현 시작)  
**기간**: 2026-08-10 ~ 2026-08-24 (2주)  
**목표**: Obsidian Vault 완전 구성 및 첫 회의 테스트

---

## 📋 Phase 2A: Obsidian 기본 설정 (Week 1)

### Step 1: Vault 구조 구성 (1일)

**상태**: ✅ 진행 중

```
obsidian-vault/
├─ .obsidian/
│  ├─ vault.json (설정)
│  └─ plugins.json (플러그인)
│
├─ SSOT/
│  ├─ 모델-선택.md
│  ├─ 프롬프트-엔지니어링.md
│  ├─ 추론-전략.md
│  ├─ 평가-방법론.md
│  ├─ 스케일링-법칙.md
│  └─ 에러-처리.md
│
├─ Meetings/
│  ├─ 2026-04-16.md
│  ├─ 2026-05-14.md
│  ├─ ... (6개 회의)
│  └─ ACTION_ITEMS.md
│
├─ Decisions/
│  ├─ ADR-001.md
│  ├─ ADR-002.md
│  └─ ... (모든 결정)
│
├─ Templates/
│  ├─ meeting-template.md
│  ├─ adr-template.md
│  └─ action-template.md
│
├─ Daily/
│  └─ 2026-08-10.md (자동 생성)
│
└─ Weekly/
   └─ 2026-[W]WW.md (자동 생성)
```

**태스크**:
- [ ] vault.json 생성 ✅
- [ ] SSOT 문서 복사
- [ ] Meetings 문서 복사
- [ ] Decisions 문서 생성
- [ ] Templates 생성

---

### Step 2: 플러그인 설치 가이드 상세화 (2일)

**파일**: `OBSIDIAN_PLUGINS_SETUP.md` (작성 예정)

```
설치 순서:
1️⃣ Dataview (쿼리 자동화)
2️⃣ Templater (템플릿 자동 생성)
3️⃣ Breadcrumbs (관계 시각화)
4️⃣ Calendar (날짜 관리)
5️⃣ Checklist (액션 체크)
6️⃣ Periodic Notes (일일/주간 자동화)
```

**각 플러그인별**:
- 설치 방법
- 초기 설정
- 사용 예시
- 트러블슈팅

---

### Step 3: 회의 템플릿 최적화 (2일)

**현재**: Enhanced 템플릿 (마크다운)  
**목표**: Obsidian 최적화 버전

```markdown
# 📅 {{date}} {{title}}

**Templater**: 자동 생성 (회의 생성 시)

## 📊 회의 정보
- 날짜: `<% tp.date.now("YYYY-MM-DD") %>`
- 의장: [[person]]
- 참석자: [[person1]], [[person2]]

## 📝 논의
### 안건 1: {{topic}}
**배경**:
- 

**의견**:
- **[[담당자]]**: 

## ✅ 결정
- 결정: 
- 담당자: [[person]]
- 마감: YYYY-MM-DD
- SSOT 영향: [[SSOT-doc]]

## 📌 액션
- [ ] **[[담당자]]** - {{action}} (마감: YYYY-MM-DD)

## 🔗 참고
- [[관련문서]]
```

---

## 📋 Phase 2B: 자동화 설정 (Week 1-2)

### Dataview 쿼리 설정

**액션 아이템 자동 표시**:
```dataview
TASK
WHERE status = "⏳"
GROUP BY due DESC
```

**회의 타임라인**:
```dataview
TABLE file.name as "회의", date as "날짜"
FROM "Meetings"
SORT date DESC
```

**결정사항 현황**:
```dataview
TABLE status as "상태", owner as "담당자"
FROM "Decisions"
SORT type, status
```

---

## 📋 Phase 2C: 첫 회의 테스트 (Week 2)

### 테스트 시나리오: 2026-08-17 제품 회의

**목표**: 모든 시스템 정상 동작 확인

**회의 흐름**:

```
1️⃣ Pre-Meeting (회의 24시간 전)
   └─ Templater로 회의록 자동 생성
      └─ 아젠다, 배경 자료 자동 삽입
   └─ Slack 알림 (자동)
   
2️⃣ During Meeting (회의 중, 실시간)
   └─ 기록자가 회의록 작성
      └─ [[담당자]] 형식으로 링크
      └─ 날짜 YYYY-MM-DD 형식
   
3️⃣ Post-Meeting (회의 후 24시간)
   └─ Claude 자동화 스크립트 실행
      ├─ 요약 생성
      ├─ 액션 추출
      ├─ 결정 분석
      └─ SSOT 링크 추가
   └─ ACTION_ITEMS.md 자동 갱신
   └─ Slack 알림 (결과 공유)
```

**테스트 체크리스트**:

- [ ] 회의 템플릿 자동 생성
- [ ] [[담당자]] 링크 자동 완성
- [ ] Dataview 쿼리 자동 갱신
- [ ] Daily Note 자동 생성
- [ ] 액션 아이템 추출 정확성
- [ ] SSOT 링크 자동 생성
- [ ] Slack 알림 정상 작동

---

## 🛠️ 구현 진행도

### Week 1 (2026-08-10 ~ 2026-08-16)

- [ ] Vault 폴더 구조 완성
- [ ] 플러그인 설치 가이드 작성
- [ ] SSOT 문서 마이그레이션
- [ ] Meetings 문서 마이그레이션
- [ ] 템플릿 최적화
- [ ] 플러그인 기본 설정

**완료율**: 0% → 50% (예정)

### Week 2 (2026-08-17 ~ 2026-08-23)

- [ ] Dataview 쿼리 설정
- [ ] 자동화 스크립트 검증
- [ ] 첫 회의 테스트 진행 (8/17)
- [ ] 피드백 수집 및 개선

**완료율**: 50% → 100% (예정)

---

## 📊 성공 기준

### 기능 체크

```
✅ Vault 정상 열림
✅ 모든 플러그인 활성화됨
✅ 회의 템플릿 자동 생성됨
✅ [[링크]] 자동 완성됨
✅ Dataview 쿼리 정상 동작
✅ Daily Note 자동 생성
✅ 액션 아이템 자동 추출
✅ SSOT 자동 링크
```

### 사용자 체험

```
✅ 신규자가 5분 안에 사용 시작 가능
✅ 회의자가 추가 작업 없이 기록
✅ PM이 한눈에 진행도 파악 가능
✅ 90% 이상 자동화율
```

---

## 🎯 다음 회의 (2026-08-17)

**목표**: 첫 회의 테스트 실행

**아젠다**:
1. Obsidian 시스템 안정성 확인
2. 회의 자동화 파이프라인 검증
3. 팀 피드백 수집
4. 개선 사항 도출

**예상 결과**:
- 80% 이상 자동화 달성
- 핵심 문제 발견 및 수정
- 2차 개선 계획 수립

---

## 📝 산출물

### Week 1
- ✅ vault.json
- [ ] OBSIDIAN_PLUGINS_SETUP.md
- [ ] 마이그레이션된 SSOT 문서들
- [ ] Obsidian 최적화 템플릿

### Week 2
- [ ] Dataview 쿼리 모음
- [ ] 첫 회의 기록 (실제)
- [ ] 자동화 스크립트 검증 리포트
- [ ] 팀 피드백 & 개선사항

---

## ⏭️ 그 다음 단계 (Month 2)

```
9월:
├─ 주간 회의 3회 진행
├─ 월간 SSOT 리뷰 회의
├─ 팀 트레이닝 완료
└─ 완전 자동화 달성

10월:
├─ 분기별 SSOT 감사
├─ 고급 기능 추가 (대시보드 심화)
└─ 조직 확대 (다른 팀에 전파)
```

---

**🎯 목표**: 2주 후 (8/24), 완전히 작동하는 Obsidian 기반 회의 관리 시스템 구축

**📍 현재 위치**: Phase 2A Step 1 시작

---

**생성일**: 2026-08-10  
**상태**: 🟡 구현 중  
**다음 검토**: 2026-08-17 (첫 회의)
