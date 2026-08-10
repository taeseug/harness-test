# 🚀 Phase 3D: Claude API 자동화 가이드

> **Status**: 준비 중 (2026-08-10)  
> **목표**: 회의 기록 → 액션 자동 추출 (Claude API)  
> **예상 완료**: 2026-08-15  

---

## 📋 Phase 3D 개요

### 현재 상태 ❌
```
회의 기록 파일 (6개)
         ↓
    수동 작업 (사람이 읽고 추출)
         ↓
    ACTION_ITEMS.md 작성
    (시간 소요, 실수 가능)
```

### 목표 상태 ✅
```
회의 기록 파일 (6개)
         ↓
    Claude API 자동 분석
         ↓
    JSON으로 액션 추출
         ↓
    ACTION_ITEMS.md 자동 생성
    (빠르고 정확함)
```

---

## 🎯 Phase 3D 목표

### 주요 목표
1. **회의 파일 자동 분석**: 6개 회의 파일 분석
2. **액션 자동 추출**: "액션 아이템" 섹션 파싱
3. **JSON 생성**: 구조화된 데이터 추출
4. **ACTION_ITEMS.md 자동 생성**: 마크다운 자동 생성
5. **검증**: 추출된 데이터 정확도 확인

### 예상 효과
- ⏱️ **시간 단축**: 수동 작업 → 자동화 (80% 시간 절약)
- ✅ **정확도 향상**: 놓친 항목 최소화
- 🔄 **반복 가능**: 새 회의 추가 시 자동 처리
- 📊 **추적 용이**: JSON 기반으로 분석 가능

---

## 🛠️ 구현 계획

### Step 1️⃣: Claude API 연동 스크립트 작성

**파일**: `scripts/extract-actions-from-meetings.py`

**기능**:
```python
1. 회의 파일 읽기 (obsidian-vault/Meetings/*.md)
2. 파일 내용을 Claude API로 전송
3. 액션 아이템 추출 요청
4. JSON 형식으로 결과 반환
5. 중복 제거 & 검증
```

**입력 형식**:
```markdown
# 2026-04-16-제품주간회의.enhanced.md

## 🎯 액션 아이템
- [ ] [박준서] PG사 3곳 비교표 작성
  - 마감: 2026-04-23
  - 목표: A/B/C 비교표 (수수료, 문서 완성도, 연동 난도)
  ...
```

**출력 형식** (JSON):
```json
{
  "meeting_date": "2026-04-16",
  "meeting_title": "제품주간회의",
  "actions": [
    {
      "title": "PG사 3곳 비교표 작성",
      "owner": "박준서",
      "status": "진행 중",
      "due_date": "2026-04-23",
      "goal": "A/B/C 비교표 (수수료, 문서 완성도, 연동 난도)",
      "criteria": "각 PG사마다 3개 항목 비교 완료",
      "related_meeting": "2026-04-16-제품주간회의.enhanced.md"
    }
  ]
}
```

---

### Step 2️⃣: 액션 아이템 병합 로직

**파일**: `scripts/merge-actions.py`

**기능**:
```python
1. 모든 회의 파일의 JSON 수집
2. 중복 액션 제거
3. 상태별 정렬 (완료, 진행중, 보류)
4. 마감일별 정렬
5. 통계 계산 (완료율, 담당자별 분포)
```

**프로세스**:
```
회의 1 JSON + 회의 2 JSON + ... → 병합 로직 → 최종 JSON
                                     ↓
                            중복 제거 (title 기준)
                                     ↓
                            상태/마감일별 정렬
                                     ↓
                            통계 계산
                                     ↓
                            최종 OUTPUT JSON
```

---

### Step 3️⃣: 마크다운 생성

**파일**: `scripts/generate-action-items-md.py`

**기능**:
```python
1. 병합된 JSON 읽기
2. ACTION_ITEMS.md 형식으로 변환
3. 테이블, 섹션 등 포맷팅
4. 링크 생성 (회의 파일 링크)
5. 메타데이터 추가 (업데이트 시간, 버전)
```

**생성 포맷**:
```markdown
# 📌 액션 아이템 추적 (2026-04-16 ~ 2026-07-23)

**최종 업데이트**: YYYY-MM-DD (자동 생성)
**기간**: 4월 16일 ~ 7월 23일
**총 아이템**: 14개

---

## 📊 요약

| 상태 | 수량 | 비율 |
|------|------|------|
| ✅ 완료 | 11개 | 79% |
| ⏳ 진행 중 | 2개 | 14% |
| ⏸️ 보류 | 1개 | 7% |

---

## 🎯 액션 (상태별)

### ✅ 완료 (11개)
- [x] [박준서] PG사 3곳 비교표 작성 (2026-04-23)
...

### ⏳ 진행 중 (2개)
- [ ] [개발팀] A사 결제 모듈 개발 (2026-06-30)
...

### ⏸️ 보류 (1개)
- [⏸️] [최민아] Q3 대시보드 스펙 초안 (보류 중)
...
```

---

## 📊 기술 스택

### 사용 기술
```
Python 3.11
├─ anthropic (Claude API)
├─ pyyaml (설정 파일)
├─ json (데이터 처리)
└─ datetime (날짜 처리)
```

### 환경 설정
```bash
# 필수 환경변수
ANTHROPIC_API_KEY=sk-...

# 선택 환경변수
CLAUDE_MODEL=claude-opus-5  # 또는 claude-sonnet-5
LOG_LEVEL=INFO
```

---

## 🎯 Claude API 프롬프트

### 시스템 프롬프트
```
당신은 회의 기록 분석 전문가입니다.
주어진 회의 기록에서 다음 정보를 추출하세요:

1. 각 액션 아이템의:
   - 제목
   - 담당자
   - 마감일
   - 상태 (완료/진행중/보류)
   - 목표
   - 성공 기준

2. JSON 형식으로 반환

3. 중복되는 액션은 병합

4. 불명확한 부분은 [불명] 표시
```

### 사용자 프롬프트 템플릿
```
다음 회의 기록에서 액션 아이템을 추출해주세요:

회의명: {meeting_title}
회의일: {meeting_date}

내용:
{meeting_content}

JSON 형식으로 반환해주세요.
```

---

## 🧪 테스트 계획

### Step 1: 단일 파일 테스트
```bash
python3 scripts/extract-actions-from-meetings.py \
  --file obsidian-vault/Meetings/2026-04-16-제품주간회의.enhanced.md \
  --output test_output.json
```

**확인 항목**:
- [ ] JSON 형식 유효성
- [ ] 액션 개수 맞음
- [ ] 담당자 정보 정확
- [ ] 날짜 형식 올바름

### Step 2: 전체 파일 테스트
```bash
python3 scripts/extract-actions-from-meetings.py \
  --input-dir obsidian-vault/Meetings/ \
  --output-dir ./test_outputs/
```

**확인 항목**:
- [ ] 6개 파일 모두 처리
- [ ] 중복 제거 정상
- [ ] 통계 계산 정확
- [ ] 에러 없음

### Step 3: 마크다운 생성 테스트
```bash
python3 scripts/generate-action-items-md.py \
  --input test_merged.json \
  --output test_ACTION_ITEMS.md
```

**확인 항목**:
- [ ] 마크다운 형식 정상
- [ ] 링크 유효성
- [ ] 테이블 렌더링
- [ ] 메타데이터 포함

### Step 4: 기존 데이터와 비교
```bash
diff obsidian-vault/Actions/ACTION_ITEMS.md test_ACTION_ITEMS.md
```

**확인 항목**:
- [ ] 액션 개수 같음 (14개)
- [ ] 정보 누락 없음
- [ ] 형식 일치

---

## 📋 체크리스트

### 준비 단계
- [ ] ANTHROPIC_API_KEY 확인
- [ ] Python 3.11+ 설치 확인
- [ ] anthropic 라이브러리 설치
- [ ] 회의 파일 구조 확인

### 개발 단계
- [ ] extract-actions 스크립트 작성
- [ ] merge-actions 스크립트 작성
- [ ] generate-markdown 스크립트 작성
- [ ] 에러 처리 추가
- [ ] 로깅 추가

### 테스트 단계
- [ ] 단일 파일 테스트
- [ ] 전체 파일 테스트
- [ ] 마크다운 생성 테스트
- [ ] 기존 데이터 비교
- [ ] CI/CD 통합 테스트

### 배포 단계
- [ ] 최종 검증
- [ ] 문서화 완료
- [ ] git commit & push
- [ ] GitHub Actions 트리거 확인

---

## ⚠️ 주의사항

### API 호출 제한
```
- Rate limit: 주의 (API 호출 비용)
- 배치 처리: 여러 회의 → 1개 API 호출
- 캐싱: 동일 파일은 재분석 금지
```

### 데이터 정확도
```
- Claude API 결과는 검증 필요
- 불명확한 항목은 수동 검수
- 기존 ACTION_ITEMS.md와 비교
```

### 환경 설정
```
- .env 파일에 API 키 저장
- .gitignore에 .env 추가
- 로컬 테스트에서만 실행
```

---

## 🚀 실행 방법

### 한 번에 모든 것 실행
```bash
# 1단계: 회의 파일에서 액션 추출
python3 scripts/extract-actions-from-meetings.py

# 2단계: 액션 병합
python3 scripts/merge-actions.py

# 3단계: 마크다운 생성
python3 scripts/generate-action-items-md.py

# 4단계: 결과 확인
diff obsidian-vault/Actions/ACTION_ITEMS.md output/ACTION_ITEMS.md
```

### 세부 옵션
```bash
# 특정 회의만 처리
python3 scripts/extract-actions-from-meetings.py \
  --start-date 2026-06-01 \
  --end-date 2026-07-31

# 출력 형식 변경
python3 scripts/generate-action-items-md.py \
  --format markdown|json|html
```

---

## 📊 기대 효과

### 자동화 전
- 시간: 약 30분 (6개 파일 수동 분석)
- 정확도: 90% (사람의 실수 가능)
- 반복성: 낮음 (새 회의마다 다시 작업)

### 자동화 후
- 시간: 약 2분 (API 호출)
- 정확도: 95%+ (Claude AI)
- 반복성: 높음 (재사용 가능한 스크립트)

---

## 🔗 관련 문서

- Phase 3C: [[obsidian-vault/QUERIES.md|대시보드 쿼리]]
- ACTION_ITEMS 구조: [[obsidian-vault/Actions/ACTION_ITEMS.md|액션 추적]]
- 회의 기록: [[obsidian-vault/Meetings|회의 폴더]]
- GitHub Actions: [[docs/references/GITHUB_ACTIONS_SETUP.md|CI/CD 설정]]

---

**작성자**: Claude Haiku 4.5  
**작성일**: 2026-08-10  
**상태**: 📋 준비 단계  
**예상 완료**: 2026-08-15
