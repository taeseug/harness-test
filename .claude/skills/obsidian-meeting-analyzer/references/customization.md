# ⚙️ 회의 분석 스킬 커스터마이징 가이드

이 문서는 스킬을 프로젝트에 맞게 커스터마이징하는 방법을 설명합니다.

---

## 1️⃣ 폴더 구조 커스터마이징

### 기본값 변경

`analyze_meeting.py` 상단의 설정을 수정하세요:

```python
# 설정 섹션
DEFAULT_MODEL = "claude-3-5-sonnet-20241022"  # Claude 모델
MEETINGS_FOLDER = "Meetings"                  # 회의 폴더명
ACTION_ITEMS_FILE = "ACTION_ITEMS.md"         # 액션 아이템 파일명
```

### 예시: 다른 폴더 구조

**시나리오**: 회의 파일이 `meetings/` 폴더에 있고, 액션을 `_actions/actions.md`에 저장

```python
# analyze_meeting.py
MEETINGS_FOLDER = "meetings"
ACTION_ITEMS_FILE = "actions.md"
```

그러면 자동으로 `meetings/` 폴더를 찾고 `_actions/actions.md`를 갱신합니다.

### 예시: 중첩 폴더 구조

**시나리오**: `project/docs/obsidian/vault/` 구조

```python
# 스크립트 실행 시 vault_root 명시
python analyze_meeting.py \
  ./docs/obsidian/vault/meetings/2026-08-17.md \
  ./docs/obsidian/vault
```

---

## 2️⃣ Claude 모델 변경

### 속도 vs 정확도 트레이드오프

```python
# 빠른 분석 (저렴, 3-5초)
model = "claude-3-haiku-20241022"

# 균형 (기본값, 10-30초)
model = "claude-3-5-sonnet-20241022"

# 정확한 분석 (비쌈, 30-60초)
model = "claude-opus-4-1-20250805"
```

### 변경 방법

`analyze_meeting.py`에서:

```python
class MeetingProcessor:
    def __init__(self, meeting_file: str, vault_root: Optional[str] = None):
        # ...
        self.model = "claude-3-haiku-20241022"  # ← 여기 변경
```

또는 환경변수로:

```bash
# 환경변수 설정
export CLAUDE_MODEL="claude-3-haiku-20241022"

# 스크립트에서 사용
self.model = os.getenv("CLAUDE_MODEL", DEFAULT_MODEL)
```

---

## 3️⃣ 분석 프롬프트 커스터마이징

### 분석 항목 추가/제거

`analyze_with_claude()` 함수에서 프롬프트 수정:

```python
def analyze_with_claude(self, meeting_content: str) -> Optional[Dict[str, Any]]:
    prompt = f"""다음 회의 노트를 분석하고 JSON 형식으로 결과를 제공하세요:

회의 노트:
{meeting_content}

다음을 추출하세요:

1. **summary**: 회의 요약 (3-5문장)
2. **actions**: 액션 아이템 (3개 이상)
   각 항목: {{"item": "작업 내용", "owner": "담당자", "due_date": "YYYY-MM-DD", "priority": "높음/중간/낮음"}}
3. **decisions**: 의사결정 사항
   각 항목: {{"decision": "결정 내용", "reason": "근거", "owner": "담당자"}}
4. **risks**: 식별된 위험요소 (NEW!)
   각 항목: {{"risk": "위험 내용", "severity": "높음/중간/낮음"}}
5. **ssot_impact**: SSOT 영향도

JSON 형식으로 정확히 반환하세요...
"""
```

### 결과 처리 업데이트

```python
self.results: Dict[str, Any] = {
    'summary': '',
    'actions': [],
    'decisions': [],
    'risks': [],  # NEW
    'ssot_impact': []
}
```

### 출력 포맷 업데이트

```python
def print_summary(self) -> None:
    # ... 기존 코드 ...
    
    # 위험요소 추가
    if self.results['risks']:
        print(f"{Colors.CYAN}⚠️ 식별된 위험요소:{Colors.END}")
        for risk in self.results['risks']:
            print(f"  • {risk.get('risk')} (심각도: {risk.get('severity')})\n")
```

---

## 4️⃣ SSOT 영향도 분석 커스터마이징

### 프로젝트의 SSOT 규칙 추가

```python
SSOT_RULES = {
    "Rule 1: 단일 정보 원칙": "모든 정보는 한 곳에만 저장",
    "Rule 2: 데이터 무결성": "링크와 참조는 항상 유효",
    "Rule 3: 권한 관리": "역할과 권한은 명확히 정의",
    "Rule 4: 버전 관리": "모든 변경사항은 기록",
}

# analyze_with_claude() 프롬프트에 추가
prompt = f"""...(기존 내용)...

SSOT 규칙:
{chr(10).join([f"- {k}: {v}" for k, v in SSOT_RULES.items()])}

이 규칙 중 영향받는 항목을 ssot_impact에 명시하세요.
"""
```

---

## 5️⃣ ACTION_ITEMS.md 포맷 커스터마이징

### 마크다운 포맷 변경

현재:
```markdown
- [ ] 🔴 [[담당자]] - 작업 내용 (마감: 2026-MM-DD)
```

변경 예 (테이블 포맷):
```python
def format_actions_markdown(self, actions: List[Dict[str, str]]) -> str:
    markdown = "## 📌 액션 아이템\n\n"
    markdown += "| 우선순위 | 작업 | 담당자 | 마감일 |\n"
    markdown += "|---------|------|--------|--------|\n"

    for action in sorted_actions:
        item = action.get('item', '')
        owner = action.get('owner', '')
        due = action.get('due_date', '')
        priority = action.get('priority', '')

        markdown += f"| {priority} | {item} | {owner} | {due} |\n"

    return markdown
```

### 메타데이터 추가

```python
def format_actions_markdown(self, actions: List[Dict[str, str]]) -> str:
    markdown = "## 📌 액션 아이템\n\n"
    markdown += f"**생성일**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
    # ... 나머지 코드 ...
```

---

## 6️⃣ 결과 저장 위치 변경

### JSON 파일 위치 커스터마이징

기본: `Meetings/analysis_YYYYMMDD_HHMMSS.json`

변경:
```python
def save_results(self) -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # 커스텀 위치: analytics/ 폴더
    results_file = self.vault_root / "analytics" / f"meeting_{timestamp}.json"
    
    # 또는 날짜별 폴더
    date_folder = datetime.now().strftime("%Y/%m")
    results_file = self.vault_root / "analytics" / date_folder / f"analysis_{timestamp}.json"
    results_file.parent.mkdir(parents=True, exist_ok=True)
    
    # ... 저장 코드 ...
```

---

## 7️⃣ 로깅 및 디버깅

### 상세한 로그 출력

```python
class MeetingProcessor:
    def __init__(self, ...):
        # ... 
        self.debug = os.getenv("DEBUG", "false").lower() == "true"
    
    def log_debug(self, msg: str) -> None:
        if self.debug:
            self.log(f"[DEBUG] {msg}", Colors.YELLOW)

    def analyze_with_claude(self, meeting_content: str):
        self.log_debug(f"프롬프트: {prompt[:200]}...")
        # ... 분석 코드 ...
        self.log_debug(f"응답: {response_text[:200]}...")
```

사용:
```bash
DEBUG=true python scripts/analyze_meeting.py ...
```

### 오류 처리 강화

```python
def analyze_with_claude(self, meeting_content: str):
    try:
        # ... 기존 코드 ...
    except anthropic.APIConnectionError as e:
        self.log(f"❌ API 연결 오류: {e}", Colors.RED)
        self.log("💡 인터넷 연결 확인", Colors.YELLOW)
        return None
    except anthropic.RateLimitError as e:
        self.log(f"❌ 속도 제한: {e}", Colors.RED)
        self.log("💡 30초 대기 후 재시도", Colors.YELLOW)
        return None
    except anthropic.AuthenticationError as e:
        self.log(f"❌ 인증 오류: {e}", Colors.RED)
        self.log("💡 ANTHROPIC_API_KEY 확인", Colors.YELLOW)
        return None
```

---

## 8️⃣ 성능 최적화

### 배치 처리 병렬화

```python
# batch_analyze_parallel.py
import concurrent.futures
from pathlib import Path

def analyze_files_parallel(vault_root: str, max_workers: int = 3):
    """여러 회의 파일을 병렬로 분석"""
    meetings_dir = Path(vault_root) / "Meetings"
    files = [f for f in meetings_dir.glob("*.md") 
             if f.name != "ACTION_ITEMS.md"]
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(
                lambda f: MeetingProcessor(str(f)).run(),
                f
            ): f for f in files
        }
        
        for future in concurrent.futures.as_completed(futures):
            file = futures[future]
            try:
                future.result()
                print(f"✅ {file.name}")
            except Exception as e:
                print(f"❌ {file.name}: {e}")
```

### 캐싱

```python
import hashlib

class MeetingProcessor:
    def __init__(self, ...):
        self.cache_dir = self.vault_root / ".analysis_cache"
        self.cache_dir.mkdir(exist_ok=True)
    
    def _get_cache_key(self, content: str) -> str:
        return hashlib.md5(content.encode()).hexdigest()
    
    def _load_from_cache(self, content: str) -> Optional[Dict]:
        cache_file = self.cache_dir / f"{self._get_cache_key(content)}.json"
        if cache_file.exists():
            with open(cache_file) as f:
                return json.load(f)
        return None
    
    def _save_to_cache(self, content: str, result: Dict) -> None:
        cache_file = self.cache_dir / f"{self._get_cache_key(content)}.json"
        with open(cache_file, 'w') as f:
            json.dump(result, f)
    
    def analyze_with_claude(self, meeting_content: str):
        # 캐시 확인
        cached = self._load_from_cache(meeting_content)
        if cached:
            self.log("📦 캐시에서 로드됨", Colors.CYAN)
            return cached
        
        # ... 분석 ...
        
        # 결과 캐시
        self._save_to_cache(meeting_content, result)
        return result
```

---

## 9️⃣ 웹훅 통합

### Slack 알림

```python
import requests

class MeetingProcessor:
    def __init__(self, ..., slack_webhook: Optional[str] = None):
        self.slack_webhook = slack_webhook or os.getenv("SLACK_WEBHOOK")
    
    def notify_slack(self, summary: str) -> None:
        if not self.slack_webhook:
            return
        
        message = {
            "text": "📋 회의 분석 완료",
            "blocks": [
                {"type": "section", "text": {"type": "mrkdwn", "text": f"📝 요약\n{summary}"}},
                {"type": "section", "text": {"type": "mrkdwn", "text": f"📌 액션: {len(self.results['actions'])}개"}},
            ]
        }
        
        requests.post(self.slack_webhook, json=message)
    
    def run(self):
        # ... 기존 코드 ...
        self.notify_slack(self.results['summary'])
```

---

## 🔟 테스트 및 검증

### 단위 테스트

```python
# test_analyze_meeting.py
import pytest

def test_format_actions():
    processor = MeetingProcessor("dummy.md")
    actions = [
        {"item": "작업 1", "owner": "담당자", "due_date": "2026-08-20", "priority": "높음"},
    ]
    result = processor.format_actions_markdown(actions)
    assert "작업 1" in result
    assert "담당자" in result

def test_extract_json():
    processor = MeetingProcessor("dummy.md")
    response = '```json\n{"test": "value"}\n```'
    json_str = processor._extract_json(response)
    assert '"test": "value"' in json_str
```

실행:
```bash
pytest test_analyze_meeting.py -v
```

---

## ✅ 커스터마이징 체크리스트

```
[ ] 폴더 구조 확인 및 설정 수정
[ ] Claude 모델 선택 (속도/정확도 고려)
[ ] 분석 프롬프트 커스터마이징
[ ] SSOT 규칙 추가 (해당되는 경우)
[ ] ACTION_ITEMS.md 포맷 확인
[ ] 로깅 및 디버깅 설정
[ ] 성능 최적화 고려
[ ] 테스트 케이스 작성 및 실행
[ ] 문서 업데이트
```

---

더 많은 커스터마이징이 필요하면 `analyze_meeting.py`의 코드를 직접 수정하세요!
