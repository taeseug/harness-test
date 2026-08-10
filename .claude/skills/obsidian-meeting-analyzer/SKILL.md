---
name: obsidian-meeting-analyzer
description: |
  Obsidian vault 기반 프로젝트에서 회의 기록을 Claude API로 자동 분석합니다. 
  요약(3-5문장), 액션 아이템(담당자/마감일), 의사결정 사항을 추출해 JSON으로 저장하고, 
  ACTION_ITEMS.md를 자동 갱신합니다. 
  Obsidian 기반 회의 관리 시스템을 구축하는 모든 프로젝트에서 사용하세요.
  매 회의 후 기록된 노트를 이 스킬로 처리해 자동 분석 결과를 얻으세요.
compatibility: |
  - Python 3.7+
  - anthropic 라이브러리 (pip install anthropic)
  - ANTHROPIC_API_KEY 환경변수 설정 필요
---

# 🤖 Obsidian 회의 자동 분석 스킬

## 📋 개요

Obsidian vault 구조를 가진 프로젝트에서 회의 기록을 **Claude API로 자동 분석**합니다.

- ✅ 회의 요약 자동 생성 (3-5문장)
- ✅ 액션 아이템 추출 (담당자, 마감일, 우선순위)
- ✅ 의사결정 사항 추출 (결정, 근거, 담당자)
- ✅ ACTION_ITEMS.md 자동 갱신
- ✅ 분석 결과 JSON 저장
- ✅ SSOT 영향도 분석 (선택사항)

---

## 🎯 언제 사용하나요?

회의가 끝나고 노트를 Obsidian에 기록한 후:

```bash
# 회의 자동 분석 실행
python scripts/analyze_meeting.py ./obsidian-vault/Meetings/2026-08-17-product-meeting.md
```

결과:
- ✅ `analysis_YYYYMMDD_HHMMSS.json` 생성
- ✅ `ACTION_ITEMS.md` 자동 갱신
- ✅ 콘솔에 요약 출력

---

## 📊 입출력

### 입력
- **파일 경로**: Obsidian Meetings 폴더의 회의 기록 Markdown 파일
- **파일 형식**: 마크다운 (`.md`)
- **경로 패턴**: `./obsidian-vault/Meetings/*.md`

### 출력
- **분석 결과**: `analysis_YYYYMMDD_HHMMSS.json`
  ```json
  {
    "summary": "회의 요약 (3-5문장)",
    "actions": [
      {
        "item": "작업 내용",
        "owner": "담당자명",
        "due_date": "2026-MM-DD",
        "priority": "높음/중간/낮음"
      }
    ],
    "decisions": [
      {
        "decision": "결정 내용",
        "reason": "근거",
        "owner": "담당자명"
      }
    ],
    "ssot_impact": ["SSOT 영향 항목"]
  }
  ```
- **자동 갱신**: `Meetings/ACTION_ITEMS.md`에 새 액션 추가

---

## 🚀 설치 및 실행

### 1️⃣ 사전 요구사항

```bash
# Python 라이브러리 설치
pip install anthropic

# API 키 설정 (환경변수)
export ANTHROPIC_API_KEY="sk-ant-..."
```

### 2️⃣ 스크립트 배치

프로젝트 루트에 다음 구조로 배치:
```
project-root/
├── scripts/
│   └── analyze_meeting.py      ← 이 스킬의 스크립트
├── obsidian-vault/
│   ├── Meetings/
│   │   ├── 2026-08-17-*.md     ← 회의 파일
│   │   └── ACTION_ITEMS.md     ← 액션 아이템 (자동 갱신)
│   └── ...
└── README.md
```

### 3️⃣ 실행

```bash
# 기본 사용
python scripts/analyze_meeting.py ./obsidian-vault/Meetings/2026-08-17-meeting.md

# 결과 확인
cat obsidian-vault/Meetings/analysis_*.json
tail -50 obsidian-vault/Meetings/ACTION_ITEMS.md
```

---

## 🔧 Obsidian 구조 요구사항

이 스킬이 정상 작동하려면 Obsidian vault가 다음 구조를 가져야 합니다:

```
obsidian-vault/
├── Meetings/
│   ├── [회의파일].md           ← 회의 기록
│   ├── ACTION_ITEMS.md         ← 액션 아이템 모음
│   ├── DECISIONS.md (선택)     ← 의사결정 (선택사항)
│   └── analysis_*.json         ← 분석 결과 (자동 생성)
│
├── SSOT/                       ← SSOT 문서 (선택)
├── Decisions/                  ← 결정사항 (선택)
└── Templates/
    └── meeting-new.md          ← 회의 템플릿 (선택)
```

**필수:**
- `Meetings/` 폴더 존재
- `Meetings/ACTION_ITEMS.md` 파일 존재

---

## 📝 회의 파일 형식

분석 품질을 높이기 위해 회의 파일을 다음처럼 작성하세요:

```markdown
---
date: 2026-08-17
type: meeting
participants: [담당자1, 담당자2]
---

# 📋 회의록 - 2026-08-17

## 📌 안건
- 안건 1
- 안건 2

## 💬 주요 논의 사항

### 주제 1
...논의 내용...

## ✅ 의사결정

| 항목 | 결정 | 담당자 |
|-----|------|--------|
| ... | ... | ... |

## 🎯 액션 아이템

- [ ] 작업 1 (담당: 담당자1, 마감: 2026-MM-DD)
- [ ] 작업 2 (담당: 담당자2, 마감: 2026-MM-DD)
```

---

## ⚙️ 커스터마이징

### 1. Obsidian 폴더 구조 변경

기본값: `Meetings/ACTION_ITEMS.md`

다른 구조를 사용하려면 스크립트 수정:

```python
# analyze_meeting.py 상단
MEETINGS_FOLDER = "Meetings"        # 변경 가능
ACTION_ITEMS_FILE = "ACTION_ITEMS.md"  # 변경 가능
```

### 2. Claude 모델 변경

기본값: `claude-3-5-sonnet-20241022`

더 빠른 분석을 원하면:
```python
model="claude-3-haiku-20241022"     # 빠르고 저렴
```

더 정확한 분석을 원하면:
```python
model="claude-opus-4-1-20250805"    # 더 정확
```

### 3. 분석 프롬프트 커스터마이징

스크립트의 `analyze_with_claude()` 함수에서 프롬프트 수정:

```python
prompt = """다음 회의 노트를 분석하고:
- 5항목의 액션 최소 추출
- 각 액션의 우선순위 명시
- [프로젝트에 맞게 커스터마이징]
"""
```

---

## 🔗 Obsidian 링크 자동화

스킬의 출력이 Obsidian 링크를 포함합니다:

- `[[담당자명]]` → 담당자 프로필로 링크
- `[[ACTION_ITEMS#작업명]]` → 특정 액션으로 링크

Obsidian 설정:
- Dataview 플러그인 활성화 (쿼리 렌더링용)
- Periodic Notes 플러그인 활성화 (Daily/Weekly 노트용)

---

## 📊 API 비용 및 성능

### 비용 (Claude API 기준)
- **입력**: ~1,500-3,000 토큰/회의 = $0.0045-0.009 / 회의
- **출력**: ~500-1,000 토큰/회의 = $0.015-0.03 / 회의
- **총합**: ~$0.02/회의 (매우 저렴)

### 성능
- **분석 시간**: 10-30초/회의
- **JSON 저장**: <1초
- **ACTION_ITEMS.md 갱신**: <1초

---

## ⚠️ 주의사항

1. **API 키 보안**
   - `.env`에 저장 (git 제외)
   - 환경변수로만 관리
   - 절대 코드에 하드코딩 금지

2. **회의 파일 인코딩**
   - UTF-8로 저장 (한글 지원)
   - 파일명에 특수문자 피하기

3. **ACTION_ITEMS.md 초기화**
   - 스크립트는 `ACTION_ITEMS.md` 끝에 추가만 함
   - 필요시 직접 정리 (스크립트가 기존 내용을 덮지 않음)

4. **SSOT 영향 분석**
   - 프로젝트의 SSOT 규칙을 알아야 정확한 분석 가능
   - `SSOT/` 폴더에 SSOT 문서가 있으면 분석 품질 향상

---

## 🧪 테스트

스킬이 정상 작동하는지 확인:

```bash
# 1. API 키 확인
echo $ANTHROPIC_API_KEY

# 2. 스크립트 실행 권한 확인
ls -l scripts/analyze_meeting.py

# 3. 샘플 회의 파일로 테스트
python scripts/analyze_meeting.py ./obsidian-vault/Meetings/2026-08-17-test.md

# 4. 결과 확인
ls -l obsidian-vault/Meetings/analysis_*.json
tail -20 obsidian-vault/Meetings/ACTION_ITEMS.md
```

---

## 🔄 워크플로우 예시

### 전체 흐름

```
1️⃣ 회의 진행 중
   └─ Obsidian에서 실시간 기록
   
2️⃣ 회의 종료
   └─ 파일 저장

3️⃣ 자동 분석 실행 (이 스킬)
   python scripts/analyze_meeting.py ./obsidian-vault/Meetings/2026-08-17-meeting.md
   
4️⃣ 결과 확인
   └─ JSON 분석 결과
   └─ ACTION_ITEMS.md 자동 갱신
   └─ Dataview 대시보드 자동 반영

5️⃣ 팀 공유
   └─ ACTION_ITEMS.md 공유
   └─ 각자 액션 처리
```

---

## 📚 참고 자료

- [Claude API 문서](https://docs.anthropic.com)
- [Obsidian 플러그인 가이드](https://docs.obsidian.md)
- [Dataview 플러그인](https://blacksmithgu.github.io/obsidian-dataview/)

---

## 🎯 다음 단계

1. ✅ 스크립트 설치
2. ✅ API 키 설정
3. ✅ 회의 파일 작성
4. ✅ 스크립트 실행
5. ✅ 결과 확인
6. ⏳ 팀에 공유
7. ⏳ 지속적 개선 (프롬프트 커스터마이징)

---

**버전**: 1.0  
**마지막 업데이트**: 2026-08-10  
**상태**: ✅ 준비 완료
