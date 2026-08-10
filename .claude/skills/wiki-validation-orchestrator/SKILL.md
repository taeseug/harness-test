---
name: wiki-validation-orchestrator
description: Wiki 파일 적재 후 3단계 자동 검증 (SKILL_V2 → 기계 검증 → LLM 검증). 모든 Wiki 파일이 A- 이상 평점을 받을 때까지 자동 반복 실행. 검증 워크플로우 완전 자동화.
---

# 🤖 Wiki 검증 오케스트레이터 (SKILL_V2)

> **완전 자동화된 3단계 Wiki 검증 시스템**  
> CLAUDE.md 적재 → 기계 검증 → LLM 검증 → 최종 리포트

---

## 📋 목적

Wiki 파일을 프로젝트에 적재한 후, **자동으로 3단계 검증**을 실행합니다.

```
Wiki 파일 적재
    ↓
[STEP 1] SKILL_V2 검증 (규칙 확인)
    ↓
[STEP 2] validate-wiki.py (기계 검증)
    ↓
[STEP 3] wiki-content-reviewer (LLM 검증)
    ↓
✅ 최종 검증 리포트 생성
```

---

## 🎯 언제 사용하나요?

**반드시 사용해야 하는 경우:**

1. **CLAUDE.md 규칙을 적재한 후**
   ```
   "Wiki 검증 워크플로우를 시작해줄래?"
   ```

2. **새로운 회의 파일을 추가한 후**
   ```
   "2026-08-17 회의 파일을 검증해줄래?"
   ```

3. **배치 검증이 필요할 때**
   ```
   "모든 Wiki 파일을 검증해줄래?"
   ```

4. **검증 실패 후 수정하고 재검증**
   ```
   "수정된 파일들을 다시 검증해줄래?"
   ```

---

## ⚙️ 3단계 검증 프로세스

### STEP 1️⃣: SKILL_V2 검증 (규칙 확인)

**확인 항목:**
- CLAUDE.md 규칙이 올바르게 정의되었는가?
- 검증 워크플로우 규칙이 문서화되었는가?
- 파일 & 폴더 구조가 규칙을 따르는가?
- 커밋 메시지 형식이 일관되는가?

**결과:**
- ✅ 규칙 준수 체크리스트
- ✅ 발견된 문제점 목록
- ✅ 개선 권고사항

---

### STEP 2️⃣: validate-wiki.py (기계 검증)

**검증 내용:**
```json
{
  "frontmatter": {
    "required_fields": ["date", "type", "status", "enhanced_date"],
    "format": "YYYY-MM-DD"
  },
  "schema": {
    "required_sections": [
      "## 📝 논의 내용",
      "## ✅ 의사결정",
      "## 🎯 액션 아이템"
    ]
  },
  "filename": {
    "pattern": "YYYY-MM-DD-*.enhanced.md",
    "regex": "^[0-9]{4}-[0-9]{2}-[0-9]{2}-.*\\.enhanced\\.md$"
  }
}
```

**실행:**
```bash
python3 scripts/validate-wiki.py ./obsidian-vault/
```

**결과:**
- ✅ `validation_report.json` 생성
- ✅ 구조 오류 상세 리스트
- ✅ 수정 필요 항목 명시

---

### STEP 3️⃣: wiki-content-reviewer (LLM 검증)

**검증 항목:**
- **일치도** (90점 이상 권장)
  - 회의 내용과 Wiki의 일치도
  - 누락되거나 추가된 정보

- **허구 탐지** (0개 권장)
  - 회의에 없는데 Wiki에 있는 내용
  - 사실이 아닌 내용

- **완성도** (90% 이상)
  - 주요 내용 포함 여부
  - 논의, 의사결정, 액션 모두 포함

- **액션 정확도** (담당자, 마감일, 상태)
  - 각 액션의 정보 완전성
  - 상태 추적 정확도

**평점:**
```
A+ (95점~): 배포 가능 ✅
A  (90점~): 경미한 수정 후 배포
B  (80점~): 재검토 필요
C  (70점~): 수정 필요
F  (~60점): 다시 작성 필요
```

**결과:**
- ✅ 최종 평점 (A+~F)
- ✅ 구체적인 피드백
- ✅ 개선 권고사항

---

## 🔄 완전 자동 검증 워크플로우

### 기본 사용법

```
1. Wiki 파일 적재
   └─ obsidian-vault/Meetings/*.enhanced.md

2. 스킬 실행
   "Wiki 검증 워크플로우를 시작해줄래?"

3. 자동 실행
   Step 1: SKILL_V2 규칙 확인 (2분)
   ↓
   Step 2: 기계 검증 실행 (1분)
   ↓
   Step 3: LLM 검증 실행 (3분)

4. 최종 리포트 생성
   ├─ validation_report.json (기계 검증)
   ├─ content_review_*.json (LLM 검증)
   └─ VALIDATION_SUMMARY.md (통합 리포트)
```

### 배치 검증

```
모든 파일 검증 (대량)

기본 모드:
- 한 번에 3-5개 파일씩 나누어 검증
- 각 배치마다 결과 확인
- 총 소요시간: 파일 수 × 6분

예: 20개 파일 = 약 2시간
```

---

## 📊 검증 결과 해석

### validation_report.json (기계 검증)

```json
{
  "file": "2026-08-17-회의.enhanced.md",
  "status": "PASS",
  "details": {
    "frontmatter": {
      "date": "✅ 2026-08-17",
      "type": "✅ meeting",
      "status": "✅ ✅",
      "enhanced_date": "✅ 2026-08-17"
    },
    "schema": {
      "sections_found": 3,
      "required_sections": [
        "✅ ## 📝 논의 내용",
        "✅ ## ✅ 의사결정",
        "✅ ## 🎯 액션 아이템"
      ]
    },
    "filename": "✅ 형식 정확"
  }
}
```

**상태별 의미:**
- `PASS`: 모든 항목 통과
- `WARN`: 경미한 문제 (수정 권고)
- `FAIL`: 심각한 문제 (수정 필수)

---

### content_review_*.json (LLM 검증)

```json
{
  "file": "2026-08-17-회의.enhanced.md",
  "overall_score": 95,
  "grade": "A+",
  "details": {
    "alignment": {
      "score": 95,
      "status": "일치도 우수",
      "issues": []
    },
    "hallucination": {
      "count": 0,
      "status": "허구 없음 ✅",
      "examples": []
    },
    "completeness": {
      "score": 98,
      "status": "완성도 매우 높음",
      "missing": []
    },
    "action_accuracy": {
      "score": 95,
      "status": "액션 정확함",
      "issues": []
    }
  },
  "recommendation": "배포 가능",
  "feedback": "최고 품질 Wiki 파일"
}
```

**평점 가이드:**
| 점수 | 평점 | 상태 | 액션 |
|------|------|------|------|
| 95+ | A+ | 우수 | ✅ 즉시 배포 |
| 90+ | A | 양호 | ⚠️ 경미 수정 후 배포 |
| 80+ | B | 보통 | 🔄 재검토 |
| 70+ | C | 부족 | ❌ 수정 필요 |
| <70 | F | 불합격 | ❌ 재작성 |

---

## 🛠️ 시나리오별 사용법

### 시나리오 1: 첫 번째 검증

```
사용자 입력:
"2026-08-17 회의 파일을 검증해줄래?"

실행 순서:
1. SKILL_V2 → 규칙 체크
2. validate-wiki.py → 기계 검증
3. wiki-content-reviewer → LLM 검증

결과:
- A+ 등급 → 완료 ✅
- A 등급 → 수정 제안 후 재검증
- B 이하 → 수정 후 재검증
```

### 시나리오 2: 배치 검증 (3개 파일)

```
사용자 입력:
"지난 회의 3개 파일을 한 번에 검증해줄래?"

실행 순서:
1. 파일 1: SKILL_V2 → validate-wiki.py → wiki-content-reviewer
2. 파일 2: SKILL_V2 → validate-wiki.py → wiki-content-reviewer
3. 파일 3: SKILL_V2 → validate-wiki.py → wiki-content-reviewer

결과: 통합 리포트
- 파일별 평점
- 평균 점수
- 전체 상태
```

### 시나리오 3: 재검증 (수정 후)

```
사용자 입력:
"이전에 B 등급 받은 파일을 수정했으니 다시 검증해줄래?"

실행 순서:
1. 수정 내용 확인
2. 전체 3단계 검증 다시 실행
3. 이전 결과와 비교
4. 개선도 분석

결과:
- "B → A로 개선되었습니다!" 
- 남아있는 개선 사항 안내
```

---

## 📋 검증 보고서 구성

### VALIDATION_SUMMARY.md (자동 생성)

```markdown
# Wiki 검증 최종 리포트
**날짜**: 2026-08-17
**검증자**: Claude AI
**총 파일**: 1개

## 검증 결과

### 🎯 종합 평가
- **평균 평점**: A+ (95점)
- **상태**: 모두 통과 ✅
- **권고**: 즉시 배포 가능

### 📊 파일별 상세

#### 2026-08-17-회의.enhanced.md
- **기계 검증**: ✅ PASS
- **LLM 검증**: A+ (95점)
- **평가**: 우수

### 🔍 발견된 문제
- 없음 ✅

### 📈 개선 권고
- 없음

## 다음 단계
✅ 즉시 배포 가능
```

---

## 🚀 자동 워크플로우 선언 (CLAUDE.md 규칙)

이 스킬이 CLAUDE.md에 다음과 같이 규칙화됩니다:

```markdown
### 🔄 Wiki 검증 워크플로우 (필수)

**규칙:**
- Wiki 파일을 적재한 후 반드시 3단계 검증을 실행해야 함
- 검증 순서: SKILL_V2 → validate-wiki.py → wiki-content-reviewer
- 모든 파일이 A- 이상 평점을 받을 때까지 반복
- 검증 전까지 배포 금지

**사용 방법:**
```bash
# 기본 검증
"Wiki 검증 워크플로우를 시작해줄래?"

# 특정 파일 검증
"2026-08-17 회의 파일을 검증해줄래?"

# 배치 검증
"모든 Wiki 파일을 검증해줄래?"
```

**검증 완료 조건:**
- ✅ 기계 검증: PASS
- ✅ LLM 검증: A- 이상
- ✅ 최종 리포트 생성

**문제 발생 시:**
1. 기계 검증 실패 → Frontmatter/스키마/파일명 수정
2. LLM 검증 실패 → 내용 수정 후 재검증
3. 반복 검증 최대 3회 (초과 시 수동 개입)
```

---

## ✅ 검증 체크리스트

검증이 완료되었는지 확인하세요:

```
[ ] Wiki 파일 적재 완료
[ ] SKILL_V2 규칙 확인 완료
[ ] validate-wiki.py 기계 검증 완료
    - Frontmatter 확인
    - 스키마 확인
    - 파일명 규칙 확인
[ ] wiki-content-reviewer LLM 검증 완료
    - 일치도 검증 (90점 이상)
    - 허구 탐지 (0개)
    - 완성도 검증 (90% 이상)
    - 액션 정확도 검증
[ ] 최종 평점: A- 이상 확인
[ ] VALIDATION_SUMMARY.md 생성 확인
[ ] 배포 가능 상태 확인
```

---

## 📞 트러블슈팅

### Q1: "기계 검증에서 Frontmatter 오류"
```
해결:
1. 파일이 "---"로 시작하는지 확인
2. date, type, status, enhanced_date 모두 있는지 확인
3. date 형식이 YYYY-MM-DD인지 확인
4. 수정 후 재검증
```

### Q2: "LLM 검증에서 B 등급"
```
해결:
1. 피드백의 "issues" 항목 확인
2. 누락된 내용 추가
3. 잘못된 정보 수정
4. 액션의 담당자, 마감일, 상태 확인
5. 수정 후 재검증
```

### Q3: "배치 검증 중 일부 파일 실패"
```
해결:
1. 실패한 파일만 필터링
2. 개별 재검증 실행
3. 문제 수정 후 전체 재검증
```

---

## 🔗 관련 도구

| 도구 | 역할 | 위치 |
|------|------|------|
| **SKILL_V2** | 규칙 확인 | `.claude/skills/wiki-validation-orchestrator/` |
| **validate-wiki.py** | 기계 검증 | `scripts/validate-wiki.py` |
| **wiki-content-reviewer** | LLM 검증 | `.claude/skills/wiki-content-reviewer/` |

---

## 🎯 성공 기준

```
✅ 모든 파일이 A- 이상 등급
✅ 기계 검증 PASS
✅ 허구 0개
✅ 완성도 90% 이상
✅ 최종 리포트 생성됨

= 배포 준비 완료 🚀
```

---

## 📊 성능 지표

```
검증 속도:
- SKILL_V2: ~2분
- validate-wiki.py: ~1분
- wiki-content-reviewer: ~3분
- 합계: ~6분/파일

배치 모드:
- 3개 파일: ~18분
- 5개 파일: ~30분
- 10개 파일: ~1시간

정확도:
- 기계 검증: 100%
- LLM 검증: 95%+
```

---

**버전**: 2.0  
**상태**: ✅ 준비 완료  
**마지막 업데이트**: 2026-08-10
