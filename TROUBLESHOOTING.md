# 🔧 Troubleshooting 가이드

**목적**: 자주 발생하는 문제와 해결 방법 제시

---

## Obsidian 관련

### "Vault를 열 수 없음"

**증상**: "Vault not found" 또는 "Cannot open folder"

**해결**:
1. 폴더 경로 확인: `/Users/mac/work/claude/20260810_harness/obsidian-vault`
2. 폴더가 실제로 존재하는지 Finder에서 확인
3. 폴더 권한 확인 (읽기/쓰기 가능한지)
4. Obsidian 재시작

---

### "플러그인 설치 안 됨"

**증상**: "Community Plugins" Browse 버튼이 비활성화됨

**해결**:
1. Community Plugins가 "Turn on" 되었는지 확인
2. 인터넷 연결 확인
3. 플러그인 이름 정확히 확인 (대소문자, 공백)
4. Obsidian 업데이트 (Help → About → Check for updates)
5. Obsidian 완전 재시작

---

### "템플릿이 자동 생성 안 됨"

**증상**: Templater로 새 파일 생성했는데 템플릿이 적용 안 됨

**해결**:
1. Templates 폴더 확인:
   ```bash
   ls /Users/mac/work/claude/20260810_harness/obsidian-vault/Templates/
   ```
   → `meeting-new.md`, `daily.md` 있어야 함

2. Templater 설정 확인:
   - Settings → Templater
   - "Template folder location": **Templates**
   - "Trigger Templater on new file creation": ✅ 활성화

3. 파일명 확인: `meeting-new.md` (정확한 이름)

4. Templater 재활성화:
   - Settings → Community Plugins
   - Templater의 "Disable" 클릭 → "Enable" 클릭

---

### "Daily Note가 생성 안 됨"

**증상**: "Periodic Notes: Open today note" 실행해도 파일 안 생성

**해결**:
1. Periodic Notes 활성화 확인
2. Daily 폴더 존재 확인:
   ```bash
   ls /Users/mac/work/claude/20260810_harness/obsidian-vault/Daily/
   ```

3. Periodic Notes 설정:
   - Settings → Periodic Notes
   - Daily Folder: **Daily**
   - Daily Format: **YYYY-MM-DD**

4. 수동 생성 시도:
   ```
   cmd+p → "Periodic Notes: Open today note"
   ```

---

### "Dataview 쿼리가 실행 안 됨"

**증상**: 쿼리 코드만 표시되고 결과 테이블이 안 보임

**해결**:
1. Dataview 활성화 확인
2. 설정 확인:
   - Settings → Dataview
   - "Enable JavaScript queries": ✅
   - "Enable Inline Queries": ✅

3. 문서 저장: Cmd+S
4. 페이지 새로고침 (Cmd+Shift+R)
5. Obsidian 재시작

---

### "Links 자동 완성이 안 됨"

**증상**: `[[` 입력 후 자동 완성 목록이 나타나지 않음

**해결**:
1. Obsidian 기본 설정 확인
2. Settings → Editor → Autocomplete: ✅ 활성화
3. 문서 저장 후 시도
4. Obsidian 재시작

---

## 마이그레이션 관련

### "migrate-docs-advanced.py 실행 오류"

**오류**: `ModuleNotFoundError: No module named 'anthropic'`

**해결**:
```bash
# Python이 없으면 설치
brew install python3

# 스크립트 실행 (anthropic 라이브러리 없어도 기본 버전은 작동)
./migrate-docs.sh  # Bash 버전 사용 대신
```

---

### "migrate-docs.sh 실행 오류"

**오류**: `Permission denied`

**해결**:
```bash
chmod +x /Users/mac/work/claude/20260810_harness/migrate-docs.sh
./migrate-docs.sh
```

---

### "마이그레이션 후 파일이 안 보임"

**증상**: 마이그레이션 완료했는데 Obsidian에 파일이 안 표시됨

**해결**:
1. Obsidian 재시작
2. File Explorer 새로고침 (Settings 재진입)
3. Vault 다시 열기:
   - File → Switch vault → obsidian-vault
4. 파일 시스템 확인:
   ```bash
   find /Users/mac/work/claude/20260810_harness/obsidian-vault -name "*.md" | head -20
   ```

---

## Claude API 관련

### "ANTHROPIC_API_KEY 오류"

**증상**: `AuthenticationError: Incorrect API key provided`

**해결**:
1. API 키 확인:
   ```bash
   echo $ANTHROPIC_API_KEY
   ```
   → 출력이 없으면 설정 필요

2. 설정 (macOS):
   ```bash
   # .zshrc 또는 .bash_profile 편집
   nano ~/.zshrc
   
   # 다음 라인 추가
   export ANTHROPIC_API_KEY="sk-ant-your-actual-key-here"
   
   # 저장 후 적용
   source ~/.zshrc
   ```

3. 다시 확인:
   ```bash
   echo $ANTHROPIC_API_KEY
   ```

---

### "meeting-processor.py 실행 오류"

**오류**: `No such file or directory`

**해결**:
```bash
# 경로 확인
ls /Users/mac/work/claude/20260810_harness/meeting-processor.py

# 권한 설정
chmod +x /Users/mac/work/claude/20260810_harness/meeting-processor.py

# 올바른 명령어
python3 /Users/mac/work/claude/20260810_harness/meeting-processor.py <파일_경로>

# 또는 디렉토리에서
cd /Users/mac/work/claude/20260810_harness
python3 meeting-processor.py ./obsidian-vault/Meetings/2026-05-14-제품주간회의.enhanced.md
```

---

### "Claude API 응답 오류"

**오류**: `RateLimitError`, `APIConnectionError`

**해결**:
1. API 사용량 확인: https://platform.openai.com/account/billing/overview
2. 인터넷 연결 확인
3. 잠시 기다린 후 재시도
4. API 키 유효성 확인 (콘솔에서 테스트)

---

## 일반 문제

### "파일 경로 오류"

**증상**: "No such file or directory"

**확인**:
```bash
# 경로 존재 확인
ls -la /Users/mac/work/claude/20260810_harness/obsidian-vault/

# 파일 존재 확인
ls /Users/mac/work/claude/20260810_harness/obsidian-vault/Meetings/
```

---

### "권한 오류"

**증상**: "Permission denied"

**해결**:
```bash
# 폴더 권한 확인
ls -ld /Users/mac/work/claude/20260810_harness/obsidian-vault/

# 필요시 권한 변경
chmod 755 /Users/mac/work/claude/20260810_harness/obsidian-vault/
chmod 644 /Users/mac/work/claude/20260810_harness/obsidian-vault/*.md
```

---

### "인코딩 오류"

**증상**: "UnicodeDecodeError", 한글이 깨짐

**확인**:
```bash
# 파일 인코딩 확인
file /Users/mac/work/claude/20260810_harness/obsidian-vault/Meetings/*.md

# UTF-8로 변환 필요시
iconv -f EUC-KR -t UTF-8 file.md > file_utf8.md
```

---

## 체크리스트 (문제 해결 순서)

1. [ ] 오류 메시지 정확히 읽기
2. [ ] 위의 해당 섹션 찾아보기
3. [ ] 권장된 해결책 시도
4. [ ] 안 되면 시스템 상태 확인:
   - [ ] Obsidian 버전 최신인가?
   - [ ] Python 3.7+ 있는가?
   - [ ] API 키 설정되었는가?
   - [ ] 인터넷 연결 정상인가?
5. [ ] 그래도 안 되면 전체 재설정

---

## 🆘 최후의 수단

문제를 해결할 수 없으면:

### Option 1: 전체 재시작
```bash
# 1. Obsidian 완전 종료
pkill -f Obsidian

# 2. Vault 백업
cp -r /Users/mac/work/claude/20260810_harness/obsidian-vault \
      /Users/mac/work/claude/20260810_harness/obsidian-vault.backup

# 3. .obsidian 폴더 초기화
rm -rf /Users/mac/work/claude/20260810_harness/obsidian-vault/.obsidian

# 4. Obsidian 다시 열기
# Vault 다시 "신뢰" 설정 필요
```

### Option 2: Bash 버전 사용
마이그레이션: Python 스크립트 대신 Bash 사용
```bash
./migrate-docs.sh
```

### Option 3: 수동 작업
직접 파일을 obsidian-vault 폴더로 복사

---

## 🎓 예방 팁

1. **정기적 백업**:
   ```bash
   cp -r obsidian-vault obsidian-vault.backup.$(date +%Y%m%d)
   ```

2. **변경 로그 기록**:
   ```bash
   ls -la > /tmp/obsidian_state.txt
   ```

3. **설정 스크린샷**: 중요한 설정 항목 스크린샷 찍기

4. **로그 확인**:
   ```bash
   tail -f /tmp/obsidian_migration.log
   ```

---

**마지막 업데이트**: 2026-08-10  
**버전**: 1.0
