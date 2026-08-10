# 안전 설계 구현 가이드

**버전**: v1.0  
**기반**: SAFETY_DESIGN.md  
**목표**: Raw → Wiki 단방향 설계 구현

---

## 🎯 구현 원칙 3가지

### 1️⃣ Raw First (Raw가 진실)

```python
# ❌ 나쁜 예: Wiki에서 상태 업데이트
def update_action_status_in_wiki(action_id, status):
    """이렇게 하면 안 됨"""
    wiki.update(action_id, status)  # Raw와 불일치!

# ✅ 좋은 예: Raw에서만 업데이트
def update_action_status_in_meeting(meeting_file, action_id, status):
    """Raw 파일에서만 상태 변경"""
    meeting = Meeting(meeting_file)
    meeting.update_action(action_id, status)  # Raw 업데이트
    # Wiki는 자동으로 동기화됨
```

### 2️⃣ Minimal Format (최소 프론트매터만)

```yaml
# ✅ 강제 (MUST)
---
date: 2026-08-20
title: "팀 회의"
participants:
  - Alice
  - Bob
---

# ⚠️ 권장 (SHOULD)
---
date: 2026-08-20
title: "팀 회의"
participants:
  - Alice
  - Bob
duration_minutes: 60
location: "온라인"
---

# 📝 자유 (CAN)
자유 형식의 회의록 내용...
```

### 3️⃣ One-Way Sync (Raw → Wiki)

```
Raw 파일 변경
    ↓ (자동 감지)
엔진이 파싱
    ↓ (추출)
Wiki 자동 생성
    ↓ (읽기 전용)
팀이 조회

특징:
- Wiki 수정 불가
- Raw 수정만 효과
- 항상 동기화됨
```

---

## 📝 Raw 회의록 처리 로직

### Step 1: 프론트매터 검증

```python
def validate_frontmatter(meeting_file: str) -> Dict:
    """
    프론트매터 검증 (최소 요구사항)
    
    필수 필드:
    - date (YYYY-MM-DD)
    - title
    - participants (리스트)
    """
    required_fields = ['date', 'title', 'participants']
    
    result = {
        "valid": True,
        "errors": [],
        "warnings": []
    }
    
    # 파일 파싱
    content = read_file(meeting_file)
    frontmatter = extract_frontmatter(content)
    
    # 필수 필드 확인
    for field in required_fields:
        if field not in frontmatter:
            result["valid"] = False
            result["errors"].append(f"필수 필드 누락: {field}")
    
    # 날짜 형식 확인
    try:
        datetime.strptime(frontmatter.get('date', ''), '%Y-%m-%d')
    except:
        result["errors"].append("날짜 형식 오류: YYYY-MM-DD")
    
    # 참석자가 리스트인지 확인
    if not isinstance(frontmatter.get('participants'), list):
        result["errors"].append("participants는 리스트여야 함")
    
    return result
```

### Step 2: 액션 아이템 추출 (Raw에서만)

```python
def extract_actions_from_raw(meeting_file: str) -> List[Dict]:
    """
    Raw 회의록에서 액션 항목 추출
    
    형식:
    - [ ] **담당자** - 작업 내용 - 마감: 2026-08-27
    - [x] **담당자** - 작업 내용 (완료)
    """
    content = read_file(meeting_file)
    
    actions = []
    
    # 패턴: - [ ] 또는 - [x]
    pattern = r'- (\[.\]) \*\*([^*]+)\*\* - ([^-]+)(?:- 마감: (\S+))?'
    
    for match in re.finditer(pattern, content):
        checkbox = match.group(1)  # [ ] 또는 [x]
        assignee = match.group(2).strip()
        task = match.group(3).strip()
        deadline = match.group(4) if match.group(4) else None
        
        actions.append({
            "status": "completed" if checkbox == "[x]" else "pending",
            "assignee": assignee,
            "task": task,
            "deadline": deadline,
            "source_file": meeting_file,  # 어느 회의에서 비롯되었나
            "source_line": match.start()
        })
    
    return actions
```

### Step 3: 결정사항 추출

```python
def extract_decisions_from_raw(meeting_file: str) -> List[Dict]:
    """
    Raw 회의록에서 결정사항 추출
    
    섹션: ## ✅ 결정사항 또는 ## 결정
    형식 (추천, 강제 아님):
    | 결정 | 근거 | Owner |
    |------|------|-------|
    | 결정 내용 | 이유 | 담당자 |
    """
    content = read_file(meeting_file)
    
    decisions = []
    
    # 섹션 찾기
    decision_section = extract_section(content, r'## .*결정')
    
    if decision_section:
        # 테이블 또는 자유 형식 파싱
        decisions = parse_decisions(decision_section)
    else:
        # 폴백: "결정" 또는 "DECISION" 포함된 라인
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if '결정' in line or 'DECISION' in line:
                decisions.append({
                    "content": line,
                    "source_line": i
                })
    
    return decisions
```

### Step 4: SSOT 영향 분석

```python
def analyze_ssot_impact(meeting_file: str) -> Dict:
    """
    회의록이 SSOT에 미치는 영향 분석
    
    자동 분석:
    - "모델" → model-selection 영향
    - "프롬프트" → prompt-engineering 영향
    - 등등
    """
    content = read_file(meeting_file)
    
    ssot_keywords = {
        "model-selection": ["모델", "haiku", "sonnet", "opus", "가격", "비용"],
        "prompt-engineering": ["프롬프트", "명확성", "구조화", "예제"],
        "inference-strategy": ["추론", "temperature", "배치", "캐싱"],
        "evaluation": ["평가", "벤치마크", "테스트", "정확도"],
        "scaling-laws": ["스케일링", "성능", "데이터"],
        "error-handling": ["에러", "실패", "복구", "타임아웃"]
    }
    
    affected_sections = []
    
    for section, keywords in ssot_keywords.items():
        for keyword in keywords:
            if keyword in content.lower():
                affected_sections.append(section)
                break
    
    return {
        "has_impact": len(affected_sections) > 0,
        "affected_sections": list(set(affected_sections)),
        "requires_adr": len(affected_sections) > 0
    }
```

### Step 5: 아젠다 생성 (이전 회의 기반)

```python
def generate_agenda_from_previous_meeting(
    previous_meeting_file: str
) -> Dict:
    """
    이전 회의의 Raw 파일을 기반으로 다음 회의 아젠다 생성
    
    구성:
    - Type A: 마감 지난 액션 (우선순위 1)
    - Type B: 진행 중인 액션 (우선순위 2)  
    - Type C: 새로운 논의 항목 (우선순위 3)
    """
    
    # 이전 회의 파싱
    previous_actions = extract_actions_from_raw(previous_meeting_file)
    previous_decisions = extract_decisions_from_raw(previous_meeting_file)
    
    today = datetime.now()
    
    agenda = {
        "type_a_overdue": [],  # 마감 지난 항목
        "type_b_pending": [],  # 진행 중 항목
        "type_c_new": [],      # 새 항목
        "decisions_follow_up": []  # 결정 후속
    }
    
    # Type A: 마감 지난 액션
    for action in previous_actions:
        if action['status'] == 'pending' and action['deadline']:
            deadline_date = datetime.strptime(action['deadline'], '%Y-%m-%d')
            if deadline_date < today:
                agenda["type_a_overdue"].append({
                    "action": action,
                    "days_overdue": (today - deadline_date).days
                })
    
    # Type B: 진행 중인 액션
    for action in previous_actions:
        if action['status'] == 'pending' and (not action['deadline'] or 
            datetime.strptime(action['deadline'], '%Y-%m-%d') >= today):
            agenda["type_b_pending"].append(action)
    
    # 결정사항 후속 확인
    agenda["decisions_follow_up"] = [
        {
            "decision": dec,
            "status": "실행 중"  # 또는 "완료" / "지연"
        }
        for dec in previous_decisions
    ]
    
    return agenda
```

---

## 🔄 Raw → Wiki 자동화 파이프라인

### 파이프라인 구조

```python
def process_meeting_pipeline(meeting_file: str) -> Dict:
    """
    Raw 회의록을 처리하는 전체 파이프라인
    
    Flow:
    1. 프론트매터 검증
    2. 액션 추출
    3. 결정사항 추출
    4. SSOT 영향 분석
    5. Wiki 생성 (자동)
    6. 알림 (Phase 2)
    """
    
    result = {}
    
    # Step 1: 검증
    validation = validate_frontmatter(meeting_file)
    if not validation["valid"]:
        return {"error": "프론트매터 검증 실패", "details": validation}
    result["validation"] = validation
    
    # Step 2-4: 콘텐츠 추출
    result["actions"] = extract_actions_from_raw(meeting_file)
    result["decisions"] = extract_decisions_from_raw(meeting_file)
    result["ssot_impact"] = analyze_ssot_impact(meeting_file)
    
    # Step 5: Wiki 자동 생성 (읽기 전용)
    wiki_content = generate_wiki_content(result)
    wiki_file = meeting_file.replace(".md", "_wiki.md")
    write_file(wiki_file, wiki_content, readonly=True)
    
    result["wiki_generated"] = wiki_file
    
    return result
```

---

## 🔐 무결성 보장

### Raw 파일 보호

```python
def protect_raw_file(meeting_file: str):
    """
    Raw 파일의 무결성 보장
    
    1. Git 히스토리 추적
    2. 자동 백업
    3. 변경 감지
    """
    
    # 1. Git에 자동 커밋
    os.system(f"git add {meeting_file}")
    os.system(f"git commit -m 'Meeting: {extract_date(meeting_file)}'")
    
    # 2. 백업 생성
    backup_dir = Path(meeting_file).parent / ".backup"
    backup_dir.mkdir(exist_ok=True)
    shutil.copy(meeting_file, backup_dir / f"{meeting_file.name}.bak")
    
    # 3. 체크섬 저장
    checksum = hash_file(meeting_file)
    save_checksum(meeting_file, checksum)
```

### Wiki 읽기 전용

```python
def generate_read_only_wiki(content: str, filepath: str):
    """
    Wiki 파일을 읽기 전용으로 생성
    """
    # 파일 생성
    with open(filepath, 'w') as f:
        f.write(content)
    
    # 권한 설정 (Unix)
    os.chmod(filepath, 0o444)  # Read-only
    
    # 헤더 추가
    header = """<!-- 
⚠️ AUTO-GENERATED FILE - 수정하지 마세요!
Raw 파일을 수정해서 다시 생성하세요.
파일: Meetings/YYYY-MM-DD_*.md
-->
"""
    with open(filepath, 'r+') as f:
        old_content = f.read()
        f.seek(0)
        f.write(header + old_content)
```

---

## 📊 상태 변경 흐름

### 시나리오: 액션 완료

```
시간 T1: 회의 A (2026-08-10)
┌────────────────────────────┐
│ Raw 파일: meeting_20260810 │
│ - [ ] Alice: 보고서 작성   │
└────────────────────────────┘
        ↓ (엔진 처리)
┌────────────────────────────┐
│ Wiki (자동 생성)            │
│ - [ ] Alice: 보고서 작성   │
└────────────────────────────┘

시간 T2: 회의 B (2026-08-17)
┌────────────────────────────┐
│ Raw 파일: meeting_20260817 │
│ - [x] Alice: 보고서 작성   │ ← 이 회의에서만 변경!
│        (from meeting_20260810)
└────────────────────────────┘
        ↓ (엔진 처리)
┌────────────────────────────┐
│ Wiki (자동 갱신)            │
│ - [x] Alice: 보고서 작성   │
└────────────────────────────┘
```

**규칙**: 상태 변경은 **후속 회의 Raw 파일에서만** 가능

---

## 🛠️ 구현 체크리스트

Phase 1 이후 구현할 것:

### Raw 처리 엔진
- [ ] `validate_frontmatter()` 함수
- [ ] `extract_actions_from_raw()` 함수
- [ ] `extract_decisions_from_raw()` 함수
- [ ] `analyze_ssot_impact()` 함수
- [ ] `generate_agenda_from_previous()` 함수
- [ ] `process_meeting_pipeline()` 통합

### Wiki 자동 생성
- [ ] `generate_wiki_content()` 함수
- [ ] 읽기 전용 설정
- [ ] 자동 헤더 추가
- [ ] 한눈에 보기 (요약)

### 무결성 보장
- [ ] Git 자동 커밋
- [ ] 자동 백업
- [ ] 체크섬 검증
- [ ] 복구 스크립트

### 테스트
- [ ] 단위 테스트 (각 함수)
- [ ] 통합 테스트 (전체 파이프라인)
- [ ] 안전 테스트 (Raw 수정 방지)

---

## 🚀 다음 단계

### 즉시 (Phase 1 완료 후)
1. SAFETY_DESIGN.md 팀과 공유
2. 이 구현 가이드 검토
3. Raw 파일 포맷 확정

### Phase 2에서
1. 위 함수들 구현
2. Wiki 자동 생성
3. 아젠다 자동 생성 완성

### Phase 3에서
1. 팀 운영 매뉴얼 작성
2. 온보딩 가이드 완성
3. 팀 첫 회의 진행

---

**준비됨? Safety Design을 기반으로 Phase 2 시작!**

