# ✅ 최종 검증 가이드

> Phase 3 완료 전 전체 시스템 점검 (Day 7)

---

## 🎯 검증 목표

```
✅ Obsidian 모든 기능 작동
✅ 문서 마이그레이션 완벽
✅ Dataview 쿼리 렌더링
✅ Claude API 분석 정상
✅ 모든 링크 작동
✅ 자동화 스크립트 정상
✅ 데이터 무결성 확인
✅ 준비 완료 상태
```

---

## 📋 Section 1: Obsidian 시스템 검증

### 1-1. Vault 기본 확인

```
Obsidian 실행 후:

[ ] Vault 정상 열림
    └─ "obsidian-vault" 표시됨

[ ] 폴더 구조 완전
    └─ SSOT, Meetings, Decisions, Daily, Weekly, Templates

[ ] 플러그인 6개 모두 활성화
    ├─ [ ] Dataview
    ├─ [ ] Templater
    ├─ [ ] Breadcrumbs
    ├─ [ ] Calendar
    ├─ [ ] Checklist
    └─ [ ] Periodic Notes

[ ] 오류 메시지 없음
    └─ 콘솔에 빨간 경고 없음
```

### 1-2. 템플릿 검증

```
[ ] meeting-new 템플릿 동작
    명령: Cmd+P → "Templater: Create new note from template"
    결과: 새 파일 생성 + 템플릿 적용

[ ] daily 템플릿 동작
    명령: Cmd+P → "Periodic Notes: Open today note"
    결과: Daily 폴더에 YYYY-MM-DD 파일 생성

[ ] 자동 날짜/시간 입력
    확인: 생성된 파일에 현재 날짜/시간 있음
```

### 1-3. 링크 기능 검증

```
[ ] 링크 자동완성 작동
    방법: [[ 입력 → 자동완성 목록 표시
    확인: [[ACTION_ITEMS]], [[담당자]], [[회의]] 등 나타남

[ ] 링크 클릭 네비게이션
    방법: 링크 Ctrl+클릭 (또는 Cmd+클릭)
    결과: 해당 문서로 이동

[ ] 링크 깨짐 없음
    확인: 문서에 빨간 깨진 링크 없음
```

### 1-4. 검색 & 필터 검증

```
[ ] 전체 검색 작동
    명령: Cmd+F
    확인: 문서 내 검색 정상

[ ] 전체 파일 검색
    명령: Cmd+P
    확인: 파일명 검색 정상

[ ] 필터링 작동
    확인: 검색 결과 필터링 가능
```

---

## 📊 Section 2: Dataview 쿼리 검증

### 2-1. QUERIES.md 검증

```
Obsidian에서 QUERIES.md 열기:

[ ] 쿼리 1: 진행 중인 액션
    표시: 테이블로 렌더링됨
    항목: ACTION_ITEMS.md의 진행 중 액션 표시
    확인: ⏳ 상태인 모든 액션 보임

[ ] 쿼리 2: 회의 타임라인
    표시: 테이블로 렌더링됨
    항목: 회의 날짜, 기록 날짜 표시
    정렬: 최신순으로 정렬됨

[ ] 쿼리 3: 결정사항 현황
    표시: 테이블로 렌더링됨
    항목: 상태, 담당자, 유형 표시
    정렬: 유형, 상태별 정렬됨
```

### 2-2. 쿼리 상호작용 검증

```
[ ] 테이블 정렬 가능
    방법: 테이블 헤더 클릭
    결과: 정렬 순서 변경됨

[ ] 테이블 필터링 가능
    방법: 헤더의 필터 아이콘 클릭
    결과: 데이터 필터링됨

[ ] 테이블 클릭 네비게이션
    방법: 테이블의 링크 클릭
    결과: 해당 문서로 이동
```

### 2-3. 실시간 갱신 검증

```
[ ] ACTION_ITEMS.md 변경 시 자동 갱신
    방법: ACTION_ITEMS.md에 항목 추가 → Cmd+S 저장
    결과: QUERIES.md의 쿼리 1 자동 갱신

[ ] 새 회의 추가 시 자동 갱신
    방법: Meetings 폴더에 새 파일 추가
    결과: QUERIES.md의 쿼리 2 자동 갱신

[ ] 새 결정 추가 시 자동 갱신
    방법: Decisions 폴더에 새 파일 추가
    결과: QUERIES.md의 쿼리 3 자동 갱신
```

---

## 🤖 Section 3: Claude API 검증

### 3-1. API 설정 검증

```
터미널에서:

[ ] API 키 설정 확인
    명령: echo $ANTHROPIC_API_KEY
    결과: sk-ant-... 형태로 출력됨

[ ] anthropic 라이브러리 설치 확인
    명령: python3 -c "import anthropic"
    결과: 오류 없음
```

### 3-2. meeting-processor.py 검증

```
터미널에서:

[ ] 스크립트 문법 검증
    명령: python3 -m py_compile scripts/meeting-processor.py
    결과: 오류 없음

[ ] 스크립트 실행 성공
    명령: python3 scripts/meeting-processor.py <회의파일>
    결과: "✅ 분석 완료" 메시지 표시

[ ] JSON 결과 생성됨
    확인: obsidian-vault/Meetings/analysis_*.json 파일 생성됨

[ ] ACTION_ITEMS.md 자동 갱신됨
    확인: 새 액션이 추가됨
```

### 3-3. 분석 품질 검증

```
생성된 analysis_*.json 확인:

[ ] 요약 생성됨 (3-5문장)
    확인: "summary" 필드가 텍스트로 채워짐

[ ] 액션 추출됨 (3개 이상)
    확인: "actions" 배열에 항목 있음
    항목: item, owner, due_date, priority 포함

[ ] 결정 분석됨 (1개 이상)
    확인: "decisions" 배열에 항목 있음
    항목: decision, reason, owner 포함

[ ] SSOT 영향 분석됨
    확인: "ssot_impact" 배열에 항목 있음
```

---

## 📁 Section 4: 문서 & 데이터 검증

### 4-1. 폴더 구조 검증

```bash
터미널에서:

[ ] obsidian-vault 구조 완전
    명령: ls -R obsidian-vault/
    확인: SSOT, Meetings, Decisions, Daily, Weekly, Templates 모두 있음

[ ] 마이그레이션 파일 모두 있음
    SSOT: 4개 파일
    Meetings: 9개 파일 (회의 6 + 분석 3)
    Decisions: 6개 파일
    Templates: 2개 파일 (meeting-new, daily)

[ ] 메타데이터 파일 있음
    확인: obsidian-vault/.migration_metadata.json 존재
```

### 4-2. 링크 무결성 검증

```
마이그레이션 메타데이터 확인:

[ ] 링크 검증 완료
    명령: cat obsidian-vault/.migration_metadata.json | jq '.links_validated'
    확인: 100+ 링크 검증됨

[ ] 깨진 링크 목록 파악
    확인: 깨진 링크 목록 문서화됨
    다음 단계: 파일 간 참조 수정 계획 가능
```

### 4-3. 데이터 일관성 검증

```
[ ] RAW vs Enhanced 일치 확인
    확인: llm-ssot/와 obsidian-vault/ 데이터 동일

[ ] 메타데이터 일관성
    확인: 모든 파일에 필요한 frontmatter 있음
    포함: date, type, category 등

[ ] 한글 파일명 정상 처리됨
    확인: 한글 파일명이 깨지지 않고 정상 표시됨
```

---

## 🔗 Section 5: 통합 기능 검증

### 5-1. End-to-End 워크플로우

```
다음 순서대로 테스트:

1️⃣ 새 회의 준비
   [ ] Obsidian에서 회의 템플릿 생성
   [ ] 날짜/시간 자동 입력됨
   [ ] [[담당자]] 링크 추가 가능

2️⃣ 회의 중 기록
   [ ] 실시간 작성 가능
   [ ] [[링크]] 자동완성 작동
   [ ] 저장 정상

3️⃣ 회의 후 분석
   [ ] meeting-processor.py 실행 가능
   [ ] 분석 완료
   [ ] ACTION_ITEMS.md 자동 갱신

4️⃣ 대시보드 갱신
   [ ] QUERIES.md에서 새 액션 보임
   [ ] 테이블 정렬/필터링 가능
   [ ] 링크로 문서 이동 가능
```

### 5-2. 자동화 완성도

```
[ ] 회의 템플릿 → 자동 생성 (Templater)
[ ] 회의 기록 → 자동 분석 (Claude API)
[ ] 분석 결과 → 자동 저장 (JSON)
[ ] 액션 추출 → 자동 추가 (ACTION_ITEMS.md)
[ ] 데이터 변경 → 자동 갱신 (Dataview 쿼리)
[ ] 링크 네비게이션 → 자동 작동

전체 자동화 체인이 끊김 없이 작동!
```

---

## 📊 Section 6: 성능 & 안정성 검증

### 6-1. 성능

```
[ ] Obsidian 로딩 시간 < 5초
[ ] 파일 열기 반응 즉시
[ ] 쿼리 렌더링 < 2초
[ ] 검색 응답 < 1초
[ ] 링크 클릭 즉시 이동
```

### 6-2. 안정성

```
[ ] 장시간 사용 후 크래시 없음
[ ] 대량 데이터 처리 가능
[ ] 플러그인 충돌 없음
[ ] 저장 시 오류 없음
[ ] API 재연결 정상
```

### 6-3. 데이터 안정성

```
[ ] 백업 파일 존재 (vault_backup_*)
[ ] 마이그레이션 메타데이터 있음
[ ] 원본 데이터 보존됨 (llm-ssot/)
[ ] 손상된 파일 없음
```

---

## 🎯 Section 7: 최종 체크리스트

### 필수 항목 (Tier 1)

```
Obsidian:
[ ] Vault 열 수 있음
[ ] 모든 파일 접근 가능
[ ] 플러그인 6개 활성화
[ ] 템플릿 자동 생성

Dataview:
[ ] 3개 쿼리 모두 렌더링
[ ] 데이터 정확함
[ ] 실시간 갱신됨

Claude API:
[ ] meeting-processor.py 실행 가능
[ ] 분석 결과 생성됨
[ ] ACTION_ITEMS.md 갱신됨

링크:
[ ] 모든 링크 작동
[ ] 깨진 링크 없음
[ ] 자동완성 작동
```

### 중요 항목 (Tier 2)

```
[ ] 템플릿 자동 생성 작동
[ ] 쿼리 실시간 갱신됨
[ ] API 분석 품질 좋음
[ ] 메타데이터 정확함
```

### 추가 항목 (Tier 3)

```
[ ] 백업 자동화
[ ] 성능 최적화
[ ] 알림 기능
[ ] 로그 기록
```

---

## 🎯 검증 점수 계산

### 점수 기준

```
Tier 1: 완료 항목당 10점
Tier 2: 완료 항목당 5점
Tier 3: 완료 항목당 2점
```

### 최종 판정

```
80점 이상: ✅ PASS - 첫 회의 준비 완료
60-79점:  ⚠️ WARNING - 일부 개선 필요
50점 미만: ❌ FAIL - 재검증 필요
```

---

## 📋 실행 순서

### Day 7 아침

```
1️⃣ Obsidian 검증 (30분)
   - Section 1-2 진행
   - 모든 체크박스 완료

2️⃣ Dataview 검증 (30분)
   - Section 2 진행
   - 쿼리 렌더링 확인

3️⃣ Claude API 검증 (30분)
   - Section 3 진행
   - API 분석 완료
```

### Day 7 오후

```
4️⃣ 문서 & 데이터 검증 (30분)
   - Section 4 진행
   - 링크 무결성 확인

5️⃣ 통합 기능 검증 (30분)
   - Section 5 진행
   - End-to-End 테스트

6️⃣ 최종 정리 (30분)
   - 점수 계산
   - 결과 기록
   - Phase 3F 준비
```

---

## ✅ 최종 상태

검증 완료 후 문서 업데이트:

```
[ ] FINAL_VALIDATION_RESULT.md 작성
[ ] 점수 기록
[ ] 문제점 정리
[ ] 개선사항 기록
[ ] Phase 3F 준비 확인
```

---

## 🚀 다음 단계

✅ Phase 3E 검증 완료 → Phase 3F 시작 (2026-08-17)

```
2026-08-17 첫 회의:
[ ] 회의 템플릿 생성
[ ] 실시간 기록
[ ] Claude 자동 분석
[ ] 대시보드 갱신
[ ] 모든 기능 검증 ✅
```

---

**마지막 업데이트**: 2026-08-14  
**버전**: 1.0  
**상태**: 📋 검증 가이드 완비

🎯 **Phase 3E 실행 준비 완료!**
