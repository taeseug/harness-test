# 🤖 Claude Skills 완벽 사용 가이드

> **Obsidian 회의 관리 시스템의 3가지 스킬 사용법**

---

## 📋 목차

1. [개요](#개요)
2. [스킬 1: obsidian-meeting-analyzer](#스킬-1-obsidian-meeting-analyzer)
3. [스킬 2: wiki-content-reviewer](#스킬-2-wiki-content-reviewer)
4. [스크립트: validate-wiki.py](#스크립트-validate-wiklipy)
5. [사용 예제](#사용-예제)
6. [트러블슈팅](#트러블슈팅)

---

## 개요

### 🎯 3가지 검증 도구

| 도구 | 타입 | 역할 | 사용 시기 |
|------|------|------|---------|
| **obsidian-meeting-analyzer** | 🤖 Skill | AI 기반 회의 분석 | 회의 기록 후 즉시 |
| **wiki-content-reviewer** | 🤖 Skill | LLM 기반 품질 검증 | 분석 완료 후 |
| **validate-wiki.py** | 🐍 Script | 기계적 구조 검증 | 대량 검증 시 |

---

## 스킬 1: obsidian-meeting-analyzer

### 📌 개요

**목적**: 회의 파일을 Claude AI로 자동 분석하여 요약, 액션, 결정사항 추출

**특징**:
- ✅ API 키 불필요 (Claude가 처리)
- ✅ 한글 완벽 지원
- ✅ 자동 저장 (JSON + ACTION_ITEMS.md)
- ✅ Obsidian 링크 포함
- ✅ 최소 3개 액션 이상 추출

### 🚀 설치 확인

```bash
# 스킬이 설치되어 있는지 확인
ls -la .claude/skills/obsidian-meeting-analyzer/
# 출력: SKILL.md, SKILL_V2.md, scripts/, references/, evals/
```

### 📖 사용 방법

#### 방법 1️⃣: 가장 간단함 (추천)

**Claude Code 입력:**
```
2026-06-11 제품주간회의 분석해줄래?
```

또는

```
회의를 분석해줘
```

**Claude가 자동으로:**
1. obsidian-vault/Meetings/ 폴더 검색
2. 날짜 매칭되는 파일 찾기
3. 분석 실행
4. 결과 저장

---

#### 방법 2️⃣: 파일명 명시

**Claude Code 입력:**
```
obsidian-vault/Meetings/2026-06-11-제품주간회의.enhanced.md 파일을 분석해줄래?
```

**Claude가:**
1. 파일 읽기
2. 분석
3. 결과 저장 및 ACTION_ITEMS.md 갱신

---

#### 방법 3️⃣: 모든 회의 한번에

**Claude Code 입력:**
```
obsidian-vault/Meetings 폴더의 모든 회의를 분석해줄래?
```

**Claude가:**
1. 모든 *.enhanced.md 파일 감지 (6개)
2. 순차적으로 분석
3. 각각 JSON 저장
4. ACTION_ITEMS.md 누적 추가

**소요 시간**: ~3-5분 (6개 회의)

---

#### 방법 4️⃣: 커스텀 요청

**Claude Code 입력:**
```
2026-06-11 회의 분석하는데:
- 액션을 우선순위별로 정렬해줄래?
- 각 액션의 구체적인 목표도 포함해줘
- 위험 요소(Risk)도 식별해줄래?
```

**Claude가:**
맞춤형 분석 결과 제공

---

### 📊 분석 결과 확인

**생성되는 파일들:**

1. **JSON 분석 결과**
```
obsidian-vault/Meetings/analysis_YYYYMMDD_HHMMSS.json
```

예시:
```json
{
  "meeting_date": "2026-06-11",
  "summary": "결제 연동 진행 상황에서 A사의 반복적인...",
  "actions": [
    {
      "item": "A사 테스트 계정 발급",
      "owner": "박준서",
      "due_date": "2026-06-18",
      "priority": "높음",
      "status": "⏳"
    }
  ],
  "decisions": [...],
  "participants": [...],
  "ssot_impact": [...]
}
```

2. **ACTION_ITEMS.md 자동 갱신**
```
obsidian-vault/Actions/ACTION_ITEMS.md
```

추가되는 내용:
```markdown
## 🔄 2026-08-10 15:30 추가

### 액션 아이템

- [ ] 🔴 [[박준서]] - A사 테스트 계정 발급 (마감: 2026-06-18)
- [ ] 🔴 [[최민아]] - 온보딩 개선안 2개 준비 (마감: 2026-06-18)
```

---

### 🎓 예제

#### 예제 1: 기본 분석

**입력:**
```
2026-06-11 회의 분석해줄래?
```

**출력:**
```
✅ 파일 읽음: 2026-06-11-제품주간회의.enhanced.md

📝 요약:
결제 연동 진행 상황에서 A사의 반복적인 커뮤니케이션 지연으로 
인한 일정 재조정(6월 중순 → 7월 초) 합의, 정산 주기 고객사 
맞춤화는 개발 자동화 검토를 위해 보류...

📌 액션 아이템 (2개):
1. 🔴 [[박준서]] - A사 테스트 계정 발급 (마감: 2026-06-18)
2. 🔴 [[최민아]] - 온보딩 개선안 2개 준비 (마감: 2026-06-18)

✅ 의사결정 (3개):
1. 결제 연동 일정 재조정 (7월 초)
2. 정산 주기 보류
3. 온보딩 A/B 테스트 진행

✅ 분석 완료!
- JSON 저장: analysis_20260811_143000.json
- ACTION_ITEMS.md 자동 갱신 완료
```

---

#### 예제 2: 여러 회의 한번에

**입력:**
```
지난 회의들을 모두 분석해줄래?
```

**출력:**
```
✅ 회의 파일 6개 발견

🤖 분석 중...

✅ 2026-04-16-제품주간회의.enhanced.md 완료
✅ 2026-05-14-제품주간회의.enhanced.md 완료
✅ 2026-06-11-제품주간회의.enhanced.md 완료
✅ 2026-06-25-온보딩개선회의.enhanced.md 완료
✅ 2026-07-09-제품주간회의.enhanced.md 완료
✅ 2026-07-23-제품주간회의.enhanced.md 완료

📊 분석 통계:
- 총 액션: 18개
- 총 결정: 12개
- 생성된 JSON 파일: 6개
- ACTION_ITEMS.md 자동 갱신: 완료

✅ 모두 완료!
```

---

## 스킬 2: wiki-content-reviewer

### 📌 개요

**목적**: 생성된 Wiki가 원본 회의록과 정확하게 일치하는지 LLM 검증

**검증 항목:**
- 📊 일치도 (90점 이상 권장)
- 🚫 허구 생성 여부 (0개 권장)
- 📝 누락된 내용 (90% 이상 포함)
- 📌 액션 상태 추적 (담당자, 마감일, 상태)

### 🚀 설치 확인

```bash
# 스킬이 설치되어 있는지 확인
ls -la .claude/skills/wiki-content-reviewer/
# 출력: SKILL.md
```

### 📖 사용 방법

#### 방법 1️⃣: 단일 회의 검증

**Claude Code 입력:**
```
2026-06-11 회의 wiki를 검증해줄래?
원본: llm-ssot/Meetings/2026-06-11-제품주간회의.enhanced.md
Wiki: obsidian-vault/Meetings/2026-06-11-제품주간회의.enhanced.md
```

**Claude가:**
1. 원본과 wiki 비교
2. 일치도 점수 계산
3. 허구 탐지
4. 누락 확인
5. 최종 평점 제시

---

#### 방법 2️⃣: 여러 회의 한번에

**Claude Code 입력:**
```
지난 회의들 (4월~7월) wiki를 모두 검증해줄래?
각각의 일치도, 허구 여부, 누락을 보고해줘
```

**Claude가:**
6개 회의 모두 검증 후 종합 리포트 제시

---

#### 방법 3️⃣: 특정 항목만 검증

**Claude Code 입력:**
```
2026-06-11 회의:
- 액션 아이템들의 담당자가 정확한가?
- 누락된 결정사항이 있나?
- 허구로 생성된 내용이 있나?
를 중점적으로 검증해줄래?
```

**Claude가:**
액션 정확성, 결정사항 완성도, 허구 탐지 중심으로 검증

---

#### 방법 4️⃣: 액션 상태 추적

**Claude Code 입력:**
```
현재까지의 회의들에서:
- 어떤 액션들이 여전히 '열림' 상태인가?
- 홀드된 액션은?
- 조용히 사라진 액션은?
추적해줄래?
```

**Claude가:**
시간 흐름에 따른 액션 상태 변화 추적

---

### 📊 검증 결과 해석

#### 평점 기준

```
A+ (95점~)   : 탁월 - 배포 가능
A  (90점~)   : 우수 - 경미한 수정 후 배포
B+ (85점~)   : 양호 - 주석 추가 권장
B  (80점~)   : 보통 - 재검토 권장
C  (70점~)   : 미흡 - 수정 필요
D  (60점~)   : 부족 - 상당한 수정 필요
F  (~60점)   : 불가 - 다시 작성 권장
```

#### 결과 해석

**일치도 (Alignment)**
- 95점+: ✅ 원본과 거의 동일
- 85점+: ✅ 대부분 일치, 사소한 누락
- 75점+: ⚠️ 일부 누락, 명확하지 않음
- 75점-: ❌ 주요 내용 누락

**허구 (Hallucination)**
- 없음: ✅ 완벽
- 1-2개: ⚠️ 영향 작음
- 3-5개: ❌ 일부 신뢰 저하
- 5개+: ❌ 신뢰도 낮음

**완성도 (Completeness)**
- 95%+: ✅ 모든 내용 포함
- 90%+: ✅ 대부분 포함
- 85%+: ⚠️ 주요 포함
- 80%-: ❌ 주요 누락

**액션 정확도 (Action Accuracy)**
- 90%+: ✅ 거의 완벽
- 80%+: ✅ 양호
- 75%+: ⚠️ 개선 필요
- 75%-: ❌ 상당한 수정 필요

---

### 🎓 예제

#### 예제 1: 단일 회의 검증

**입력:**
```
2026-06-11 회의를 검증해줄래?
```

**출력:**
```
검증 시작: 2026-06-11 제품주간회의

📊 일치도 (Alignment): 95점
  ✅ 요약이 정확함
  ✅ 주요 논점 모두 포함
  ✅ 표현이 원본과 유사

🚫 허구 탐지 (Hallucination): 없음
  ✅ 모든 내용이 원본과 일치

📝 완성도 (Completeness): 98%
  ✅ 액션 아이템 완전 포함
  ✅ 결정사항 완전 포함
  ⚠️ 주석 추가 권장

📌 액션 정확도 (Action Accuracy): 95%
  ✅ 담당자: 100% 정확
  ✅ 마감일: 100% 정확
  ✅ 상태: 100% 정확

🎯 최종 평점: A+ (95/100)
→ 배포 가능! 완벽한 wiki입니다.
```

---

#### 예제 2: 문제가 있는 경우

**입력:**
```
이 회의 wiki를 검증해줄래?
```

**출력:**
```
검증 시작...

📊 일치도 (Alignment): 75점
  ⚠️ 일부 표현 다름
  ⚠️ 2개 주제 순서 다름
  ❌ 온보딩 이탈률 정확도 부족

🚫 허구 탐지 (Hallucination): 발견됨
  ❌ "API 개선" 액션 (원본에 없음)
  ⚠️ "마이그레이션" 의사결정 (원본에 없음)

📝 완성도 (Completeness): 82%
  ✅ 주요 액션 포함
  ❌ 3개 결정사항 누락
  ⚠️ 위험 요소 누락

📌 액션 정확도 (Action Accuracy): 75%
  ❌ 1개 액션 담당자 미정
  ⚠️ 2개 액션 마감일 불확실

🎯 최종 평점: C (75/100)
→ 수정 필요!

권장 조치:
1. 허구 제거 (API 개선, 마이그레이션)
2. 누락된 결정사항 3개 추가
3. 액션 담당자 명시
4. 위험 요소 섹션 추가
5. 재검증
```

---

## 스크립트: validate-wiki.py

### 📌 개요

**목적**: 모든 Wiki 파일의 기계적 구조 자동 검증

**검증 항목:**
- ✅ Frontmatter (필수 필드 4개)
- ✅ 스키마 (필수 섹션 3개)
- ✅ 파일명 규칙 (YYYY-MM-DD-*.enhanced.md)

### 🚀 실행 방법

```bash
# 기본 사용
python3 scripts/validate-wiki.py ./obsidian-vault/

# 또는 특정 폴더만
python3 scripts/validate-wiki.py ./obsidian-vault/Meetings
```

### 📊 검증 결과 확인

**생성 파일:**
```
obsidian-vault/validation_report.json
```

**JSON 구조:**
```json
{
  "timestamp": "2026-08-10T15:30:00",
  "stats": {
    "total_files": 6,
    "valid_files": 5,
    "files_with_issues": 1
  },
  "results": [
    {
      "file": "Meetings/2026-06-11-제품주간회의.enhanced.md",
      "valid": true,
      "frontmatter": {"valid": true, "issues": []},
      "schema": {"valid": true, "issues": []},
      "filename": {"valid": true, "issues": []}
    }
  ],
  "summary": {
    "total": 6,
    "valid": 5,
    "invalid": 1,
    "pass_rate": "83.3%"
  }
}
```

### 🎓 예제

**실행:**
```bash
python3 scripts/validate-wiki.py ./obsidian-vault/
```

**출력:**
```
============================================================
🔍 Wiki 기계 검증 시작
============================================================

📊 발견된 파일: 6개

✅ [1/6] 2026-04-16-제품주간회의.enhanced.md
✅ [2/6] 2026-05-14-제품주간회의.enhanced.md
✅ [3/6] 2026-06-11-제품주간회의.enhanced.md
✅ [4/6] 2026-06-25-온보딩개선회의.enhanced.md
✅ [5/6] 2026-07-09-제품주간회의.enhanced.md
❌ [6/6] 2026-07-23-제품주간회의.enhanced.md
   ⚠️ [frontmatter] 필수 필드 'enhanced_date' 누락
   ⚠️ [schema] 필수 섹션 '액션 아이템' 없음

============================================================
📈 검증 결과
============================================================
총 파일: 6
통과: 5 (83.3%)
실패: 1

⚠️ 수정이 필요한 파일들:
  - Meetings/2026-07-23-제품주간회의.enhanced.md

💾 리포트 저장: obsidian-vault/validation_report.json
```

---

## 사용 예제

### 📚 실제 사용 시나리오

#### 시나리오 1: 회의 기록부터 검증까지 (15분)

```
1️⃣ 회의 진행 중 (60분)
   └─ Obsidian에 실시간 기록

2️⃣ 회의 종료 후 (즉시)
   └─ 파일 저장

3️⃣ 자동 분석 실행 (2분)
   Claude Code: "회의를 분석해줄래?"
   
   ✅ analysis_*.json 생성
   ✅ ACTION_ITEMS.md 갱신
   ✅ 요약/액션/결정 추출 완료

4️⃣ 기계 검증 (1분)
   Terminal: python3 scripts/validate-wiki.py ./obsidian-vault/
   
   ✅ validation_report.json 생성
   ✅ Frontmatter/스키마/파일명 검증 완료

5️⃣ LLM 검증 (2분)
   Claude Code: "wiki를 검증해줄래?"
   
   ✅ 일치도/허구/누락/액션 검증 완료
   ✅ 최종 평점 (A+ 등급) 제시

6️⃣ 완료!
   └─ 모든 검증 통과 → 배포 가능
```

---

#### 시나리오 2: 대량 회의 검증 (30분)

```
1️⃣ 여러 회의 분석 (5분)
   Claude Code: "4월~7월 회의들을 모두 분석해줄래?"
   
   ✅ 6개 회의 모두 분석 완료
   ✅ 6개 JSON 파일 생성
   ✅ ACTION_ITEMS.md 누적 갱신

2️⃣ 기계 검증 (1분)
   Terminal: python3 scripts/validate-wiki.py ./obsidian-vault/
   
   ✅ 모든 파일 구조 검증
   ✅ validation_report.json 생성

3️⃣ LLM 검증 (10분)
   Claude Code: "모든 wiki들을 검증해줄래?"
   
   ✅ 각 회의별 평점 제시
   ✅ 공통 문제점 식별

4️⃣ 개선 (14분)
   └─ 문제점 수정 및 재검증

5️⃣ 완료!
   └─ 전체 wiki 품질 평가 완료
```

---

#### 시나리오 3: 회의 진행도 추적 (10분)

```
1️⃣ Obsidian 열기
   └─ Analysis/MEETINGS_HISTORY/INDEX.md

2️⃣ 6개월 분석 조회
   ├─ 외부 의존성 추적 (4월~7월)
   ├─ 의사결정 품질 평가
   ├─ 팀의 학습 곡선
   └─ 액션 상태 변화 (열림→완료)

3️⃣ 패턴 파악
   ├─ 반복되는 문제 식별
   ├─ 성공 사례 분석
   └─ 개선 전략 수립

4️⃣ 완료!
   └─ 팀의 역량과 성장 파악
```

---

## 트러블슈팅

### ❓ Q1: "스킬을 찾을 수 없습니다" 오류

**원인**: 스킬이 설치되지 않음

**해결:**
```bash
# 스킬 설치 위치 확인
ls -la .claude/skills/

# 없으면 다시 설치
# → README.md의 설치 방법 참고
```

---

### ❓ Q2: API 키 오류

**오류**: `ANTHROPIC_API_KEY 환경변수가 설정되지 않음`

**해결:**
```bash
# API 키 설정
export ANTHROPIC_API_KEY="sk-ant-..."

# 확인
echo $ANTHROPIC_API_KEY

# 영구 설정 (선택)
echo 'export ANTHROPIC_API_KEY="sk-ant-..."' >> ~/.zshrc
source ~/.zshrc
```

---

### ❓ Q3: 파일을 찾을 수 없습니다

**원인**: 파일명 또는 경로 오류

**해결:**
```bash
# Obsidian vault 폴더 확인
ls obsidian-vault/Meetings/

# 파일명 확인
ls obsidian-vault/Meetings/ | grep "2026-06-11"

# 전체 경로로 명시
/Users/mac/work/claude/20260810_harness/obsidian-vault/Meetings/2026-06-11-제품주간회의.enhanced.md
```

---

### ❓ Q4: Frontmatter 오류

**오류**: `Frontmatter가 없음 (시작이 '---'이 아님)`

**해결:**
```markdown
# ❌ 잘못된 예
date: 2026-06-11
type: meeting

# ✅ 올바른 예
---
date: 2026-06-11
type: meeting
status: ✅
enhanced_date: 2026-08-10
---

# 회의록 제목
...
```

---

### ❓ Q5: 분석 결과가 JSON으로 안 나옵니다

**원인**: Claude API 응답 형식 오류

**해결:**
```
Claude Code에 명시적으로:
"JSON 형식으로 분석해줄래?"

또는

"다음 JSON 스키마로 분석 결과를 반환해줄래:
{
  'summary': '...',
  'actions': [...],
  'decisions': [...]
}"
```

---

### ❓ Q6: ACTION_ITEMS.md가 갱신 안 됨

**원인**: 파일 권한 또는 경로 오류

**확인:**
```bash
# 파일 존재 확인
ls -la obsidian-vault/Actions/ACTION_ITEMS.md

# 쓰기 권한 확인
chmod 644 obsidian-vault/Actions/ACTION_ITEMS.md

# 스킬 다시 실행
Claude Code: "회의를 분석해줄래?"
```

---

## 📞 지원

### 문제 해결 순서

1. **스킬 메타데이터 확인**
   ```bash
   ls -la .claude/skills/*/SKILL.md
   ```

2. **로그 확인**
   ```bash
   # Claude Code 에러 메시지 복사
   # → 이 문서에서 검색
   ```

3. **수동 실행**
   ```bash
   python3 scripts/validate-wiki.py ./obsidian-vault/
   ```

4. **파일 권한 확인**
   ```bash
   chmod 755 scripts/validate-wiki.py
   ```

5. **API 키 재설정**
   ```bash
   export ANTHROPIC_API_KEY="sk-ant-..."
   ```

---

## 📚 참고 문서

- **아키텍처**: [SYSTEM_ARCHITECTURE.md](SYSTEM_ARCHITECTURE.md)
- **검증 가이드**: [WIKI_VALIDATION_GUIDE.md](WIKI_VALIDATION_GUIDE.md)
- **회의 분석 가이드**: [OBSIDIAN_MEETING_ANALYZER_GUIDE.md](OBSIDIAN_MEETING_ANALYZER_GUIDE.md)
- **스킬 설정**: [.claude/skills/obsidian-meeting-analyzer/](../../.claude/skills/obsidian-meeting-analyzer/)

---

**스킬 가이드 최종 버전**: 1.0  
**작성일**: 2026-08-10  
**상태**: ✅ 운영 준비 완료
