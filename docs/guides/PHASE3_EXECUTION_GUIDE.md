# 🚀 Phase 3 실행 가이드 (완전 자동화)

**목표**: Obsidian 기반 회의 관리 시스템 완전 구축  
**기간**: 2026-08-10 ~ 2026-08-17 (1주일)  
**결과**: 첫 회의 테스트 (2026-08-17)  
**난이도**: 중급

---

## 📅 일정 (Day-by-Day)

### Day 1-2 (2026-08-10~11): Obsidian 기본 설정

**목표**: 로컬 Obsidian 설치 및 플러그인 설정  
**시간**: 2-3시간  
**가이드**: SETUP_CHECKLIST.md

#### 수행 사항:
1. Obsidian 설치
2. Vault 열기 (`obsidian-vault`)
3. 6개 플러그인 설치
4. 템플릿 2개 생성 (meeting-new, daily)
5. 기본 쿼리 테스트

**체크리스트**:
```
- [ ] Obsidian 설치 완료
- [ ] Vault 열기 성공
- [ ] 6개 플러그인 활성화
- [ ] 템플릿 자동 생성 작동
- [ ] Daily Note 자동 생성 작동
```

**완료 확인**:
- [ ] Obsidian 창에 "obsidian-vault" 표시
- [ ] 좌측 사이드바에 폴더 구조 보임
- [ ] 달력 플러그인 표시됨

---

### Day 3-4 (2026-08-12~13): 문서 마이그레이션

**목표**: 모든 문서를 Obsidian Vault로 자동 복사  
**시간**: 1-2시간  
**도구**: migrate-docs-advanced.py (Python)

#### 준비:
```bash
# Python 설치 확인
python3 --version  # Python 3.7+

# 필요한 패키지 확인 (기본 라이브러리만 사용)
```

#### 수행:
```bash
# 터미널에서 실행
cd /Users/mac/work/claude/20260810_harness

# Python 스크립트 실행
python3 migrate-docs-advanced.py

# 또는 기존 Bash 스크립트 사용
./migrate-docs.sh
```

**체크리스트**:
```
- [ ] 마이그레이션 스크립트 실행
- [ ] SSOT 문서 복사 확인
- [ ] Meetings 문서 복사 확인
- [ ] Decisions 문서 복사 확인
- [ ] 링크 검증 완료
```

**완료 확인**:
- [ ] obsidian-vault/SSOT/ 폴더에 4-6개 파일
- [ ] obsidian-vault/Meetings/ 폴더에 8-10개 파일
- [ ] obsidian-vault/Decisions/ 폴더에 6개 파일
- [ ] 터미널에 "✅ 마이그레이션 완료!" 메시지

---

### Day 5 (2026-08-14): Dataview 쿼리 설정

**목표**: 대시보드 쿼리 구성 및 테스트  
**시간**: 45분-1시간  
**위치**: WIKI/ 디렉토리 또는 루트

#### 수행:

**1. QUERIES.md 파일 생성**:
```bash
# Obsidian에서
# 새 파일 → QUERIES.md
# 또는 WIKI/ 폴더에 저장
```

**2. 3가지 주요 쿼리 추가**:

**쿼리 1: 진행 중인 액션**
```dataview
TASK
WHERE status = "⏳"
GROUP BY due DESC
```

**쿼리 2: 회의 타임라인**
```dataview
TABLE file.name as "회의", date as "날짜"
FROM "Meetings"
SORT date DESC
```

**쿼리 3: 결정사항 현황**
```dataview
TABLE status as "상태", owner as "담당자"
FROM "Decisions"
WHERE type != null
SORT type, status
```

**체크리스트**:
```
- [ ] QUERIES.md 생성
- [ ] 3개 쿼리 모두 추가
- [ ] 모든 쿼리 렌더링됨 (테이블 표시)
- [ ] 결과 데이터 정확함
```

**완료 확인**:
- [ ] QUERIES.md에 3개 쿼리 모두 표시
- [ ] 액션 목록 테이블 보임
- [ ] 회의 목록 테이블 보임
- [ ] 결정사항 테이블 보임

---

### Day 6 (2026-08-15): 회의 자동화 설정

**목표**: Claude API 기반 회의 자동화 구성  
**시간**: 1-2시간  
**도구**: meeting-processor.py (Python + Claude API)

#### 준비:

**1. Claude API 키 설정**:
```bash
# .bash_profile 또는 .zshrc에 추가
export ANTHROPIC_API_KEY="sk-ant-..."

# 적용
source ~/.bash_profile
# 또는
source ~/.zshrc

# 확인
echo $ANTHROPIC_API_KEY
```

**2. Python 스크립트 권한 설정**:
```bash
cd /Users/mac/work/claude/20260810_harness
chmod +x meeting-processor.py
```

#### 테스트:

```bash
# 기존 회의 노트로 테스트
python3 meeting-processor.py \
  ./obsidian-vault/Meetings/2026-05-14-제품주간회의.enhanced.md
```

**체크리스트**:
```
- [ ] ANTHROPIC_API_KEY 설정
- [ ] meeting-processor.py 실행 권한 설정
- [ ] 스크립트 실행 성공
- [ ] JSON 결과 파일 생성됨
- [ ] ACTION_ITEMS.md 갱신됨
```

**완료 확인**:
- [ ] 터미널에 "✅ Claude 분석 완료" 메시지
- [ ] obsidian-vault/Meetings/analysis_*.json 파일 생성
- [ ] 요약, 액션, 결정 출력됨

---

### Day 7 (2026-08-16): 최종 검증 & 준비

**목표**: 첫 회의 테스트를 위한 최종 점검  
**시간**: 1-2시간  
**가이드**: SETUP_CHECKLIST.md (Phase 3F)

#### 전체 시스템 점검:

**1. Obsidian 상태 확인**:
```
- [ ] Vault 정상 열림
- [ ] 모든 폴더 보임
- [ ] 모든 파일 표시됨
- [ ] 플러그인 6개 모두 활성화
```

**2. 문서 링크 확인**:
```
- [ ] [[ACTION_ITEMS]] 링크 작동
- [ ] [[담당자]] 자동 완성
- [ ] [[회의]] 링크 작동
- [ ] 깨진 링크 없음
```

**3. 템플릿 확인**:
```
- [ ] meeting-new 템플릿 생성 작동
- [ ] daily 템플릿 생성 작동
- [ ] 날짜 자동 입력
```

**4. 쿼리 확인**:
```
- [ ] QUERIES.md의 3개 쿼리 모두 작동
- [ ] 데이터 정확함
- [ ] 실시간 업데이트 작동
```

**5. 자동화 스크립트 확인**:
```
- [ ] migrate-docs-advanced.py 실행 가능
- [ ] meeting-processor.py 실행 가능
- [ ] API 키 설정 확인
```

#### 문제 해결 (필요시):

문제 발생 시 TROUBLESHOOTING.md 참고

---

### Day 8 (2026-08-17): 첫 회의 테스트! 🎉

**목표**: 실제 회의에서 시스템 테스트  
**시간**: 1시간 (회의 포함)  
**가이드**: FIRST_MEETING_TEST.md

#### 회의 흐름:

**Pre-Meeting (회의 30분 전)**:
```
1. Templater 테스트
   - Cmd+P → "Insert template: meeting-new"
   - 파일 자동 생성 확인
   - 시간/날짜 입력 확인

2. 아젠다 준비
   - [[ACTION_ITEMS]] 링크로 이전 과제 확인
   - 진행 현황 파악
```

**During Meeting (회의 진행 중)**:
```
1. 실시간 기록
   - 기록자가 Obsidian에서 직접 작성
   - [[담당자]] 형식 사용
   - 마감일 YYYY-MM-DD 형식 사용

2. 링크 작동 확인
   - [[이름]] 자동 완성 확인
   - 링크 클릭 시 작동 확인
```

**Post-Meeting (회의 후 24시간 이내)**:
```
1. Claude 자동화 실행
   python3 meeting-processor.py <회의_파일>

2. 결과 확인
   - 요약 생성됨
   - 액션 추출됨
   - 결정 분석됨

3. ACTION_ITEMS.md 확인
   - 새 액션이 추가됨
   - 형식 정확함
   - 담당자/마감일 입력됨

4. Dataview 쿼리 업데이트 확인
   - QUERIES.md의 쿼리가 새 데이터 표시
   - 액션 목록 갱신됨
```

#### 성공 기준:

```
필수 (Tier 1):
✅ 회의 템플릿 자동 생성
✅ [[링크]] 자동 완성
✅ 회의 기록 저장됨
✅ Claude 분석 실행됨

중요 (Tier 2):
✅ ACTION_ITEMS.md 갱신
✅ Dataview 쿼리 업데이트
✅ 모든 링크 작동

추가 (Tier 3):
✅ Slack 알림 (선택)
✅ 자동 백업 (선택)
```

---

## 🎯 주요 파일 및 역할

| 파일 | 역할 | 사용자 |
|------|------|--------|
| **SETUP_CHECKLIST.md** | 단계별 설정 가이드 | 로컬 설정 담당자 |
| **migrate-docs-advanced.py** | 자동 마이그레이션 | 개발자 |
| **meeting-processor.py** | Claude 회의 분석 | 회의 기록자 |
| **PHASE3_EXECUTION_GUIDE.md** | 전체 일정표 (이 파일) | 프로젝트 매니저 |
| **TROUBLESHOOTING.md** | 문제 해결 가이드 | 모두 |
| **SUCCESS_CRITERIA.md** | 성공 기준 | QA/검증 담당 |

---

## 🔄 병렬 작업 (Day 3-4 권장)

만약 여러 사람이 동시에 작업 가능하면:

```
담당자 A: Obsidian 플러그인 설치 (Day 1-2)
담당자 B: 템플릿 생성 (Day 2)
담당자 C: 마이그레이션 스크립트 준비 (Day 2-3)

Day 3: 모두 함께 마이그레이션 실행

담당자 A: Dataview 쿼리 설정 (Day 5)
담당자 B: Claude API 설정 (Day 5)
담당자 C: 최종 검증 (Day 6)
```

---

## 📋 체크리스트 (전체)

### Phase 3A: 기본 설정
- [ ] Obsidian 설치
- [ ] Vault 열기
- [ ] 플러그인 6개 설치
- [ ] 템플릿 생성

### Phase 3B: 문서 마이그레이션
- [ ] SSOT 복사
- [ ] Meetings 복사
- [ ] Decisions 복사
- [ ] 링크 검증

### Phase 3C: Dataview 쿼리
- [ ] QUERIES.md 생성
- [ ] 3개 쿼리 추가
- [ ] 모든 쿼리 작동 확인

### Phase 3D: 회의 자동화
- [ ] API 키 설정
- [ ] meeting-processor.py 테스트
- [ ] JSON 결과 생성 확인
- [ ] ACTION_ITEMS 갱신 확인

### Phase 3E: 최종 검증
- [ ] 전체 시스템 점검
- [ ] 모든 링크 작동
- [ ] 모든 쿼리 작동
- [ ] 문제 해결

### Phase 3F: 첫 회의
- [ ] 템플릿 테스트
- [ ] 실시간 기록
- [ ] Claude 분석
- [ ] 결과 확인

---

## 🚨 긴급 연락처

문제 발생 시:

1. **TROUBLESHOOTING.md** 참고
2. **SETUP_CHECKLIST.md**의 트러블슈팅 섹션 확인
3. 해결 안 되면 아래 확인:
   - Obsidian 버전 확인
   - Python 버전 확인 (`python3 --version`)
   - API 키 설정 확인 (`echo $ANTHROPIC_API_KEY`)

---

## 📊 예상 진행률

```
Day 1-2: ████░░░░░░░░░░░░ 25% (기본 설정)
Day 3-4: █████████░░░░░░░░ 50% (마이그레이션)
Day 5:   █████████████░░░░ 75% (쿼리 설정)
Day 6:   ██████████████████ 90% (자동화 설정)
Day 7:   ████████████████░░ 95% (최종 검증)
Day 8:   ████████████████░░ 100% (첫 회의 테스트!)
```

---

## 🎉 완료 후

첫 회의가 성공적으로 끝나면:

1. **결과 평가**:
   - 자동화율 측정
   - 팀 피드백 수집
   - 개선사항 도출

2. **정상 운영**:
   - 매주 회의 진행
   - ACTION_ITEMS 자동 관리
   - DASHBOARD 실시간 갱신

3. **확대**:
   - 다른 팀에 확산
   - 월간/분기별 회의 추가
   - 자동화 고도화

---

## 📞 도움말

**Obsidian 설정**: SETUP_CHECKLIST.md  
**마이그레이션**: migrate-docs-advanced.py --help  
**회의 자동화**: meeting-processor.py --help  
**문제 해결**: TROUBLESHOOTING.md  
**성공 기준**: SUCCESS_CRITERIA.md

---

**마지막 업데이트**: 2026-08-10  
**목표 완료일**: 2026-08-17  
**상태**: 🟡 준비 중

🚀 **행운을 빕니다! 첫 회의에서 만나요!**
