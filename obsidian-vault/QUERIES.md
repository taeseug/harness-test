---
type: dashboard
date: 2026-08-14
category: dataview
---

# 📊 Dataview 대시보드 & 쿼리

> 실시간 액션, 회의, 결정사항 추적

---

## 🎯 개요

이 파일은 3개의 핵심 쿼리를 포함합니다:
1. **진행 중인 액션** - 담당자별 책임과제
2. **회의 타임라인** - 연시간 회의 기록
3. **결정사항 현황** - 의사결정 추적

---

## 📌 쿼리 1: 진행 중인 액션

```dataview
TASK
WHERE status = "⏳"
GROUP BY due DESC
```

**목적**: 현재 진행 중인 모든 액션 아이템 조회  
**갱신**: 자동 (ACTION_ITEMS.md 변경 시)  
**표시**: 담당자, 마감일, 우선순위별

---

## 📅 쿼리 2: 회의 타임라인

```dataview
TABLE file.name as "회의", file.mday as "날짜", file.cday as "기록날짜"
FROM "Meetings"
WHERE file.name != "ACTION_ITEMS.md" AND file.name != "MEETINGS_ANALYSIS.md" AND file.name != "_meeting-template.enhanced.md"
SORT file.mday DESC
LIMIT 20
```

**목적**: 시간순 회의 기록 조회  
**갱신**: 자동 (Meetings 폴더 변경 시)  
**표시**: 회의 날짜, 기록 날짜, 최근 20개

---

## ✅ 쿼리 3: 결정사항 현황

```dataview
TABLE status as "상태", owner as "담당자", type as "유형"
FROM "Decisions"
WHERE type != null
SORT type, status
```

**목적**: 의사결정 사항 추적  
**갱신**: 자동 (Decisions 폴더 변경 시)  
**표시**: 결정 상태, 담당자, 유형별 정렬

---

## 🔍 쿼리 4: 액션별 담당자 (선택)

```dataview
TABLE WITHOUT ID file.link as "액션", owner as "담당자"
FROM "Meetings"
WHERE type = "action"
GROUP BY owner
```

**목적**: 담당자별 액션 정리 (선택 사항)  
**갱신**: 자동  
**표시**: 담당자별 그룹핑

---

## 📈 쿼리 5: 월별 회의 통계 (선택)

```dataview
TABLE WITHOUT ID choice(rows.file.mday, "정보없음") as "날짜", length(rows) as "건수"
FROM "Meetings"
WHERE type = "meeting"
GROUP BY dateformat(file.mday, "yyyy-MM")
```

**목적**: 월별 회의 개수 통계 (선택 사항)  
**갱신**: 자동  
**표시**: 월별 통계

---

## 🎯 사용법

### 1️⃣ Obsidian에서 보기

1. 이 파일 (QUERIES.md) 열기
2. 각 쿼리가 테이블로 렌더링되는지 확인
3. 테이블 클릭하면 해당 문서로 이동 가능

### 2️⃣ 쿼리 커스터마이징

각 쿼리는 다음과 같이 수정 가능:

```dataview
TABLE property1, property2
FROM "folder"
WHERE condition
SORT field
LIMIT 10
```

**주요 옵션:**
- `WHERE`: 필터링 (조건)
- `SORT`: 정렬 (필드명 ASC/DESC)
- `LIMIT`: 개수 제한
- `GROUP BY`: 그룹 분류

### 3️⃣ 문제 해결

**쿼리가 렌더링 안 되면:**

1. 저장: `Cmd + S`
2. 새로고침: `Cmd + Shift + R`
3. Obsidian 재시작
4. Dataview 플러그인 재활성화

---

## 📊 대시보드 구성

```
QUERIES.md (이 파일)
├─ 쿼리 1: 진행 중인 액션
│  └─ ACTION_ITEMS.md 기반
├─ 쿼리 2: 회의 타임라인
│  └─ Meetings/ 폴더 기반
├─ 쿼리 3: 결정사항 현황
│  └─ Decisions/ 폴더 기반
├─ 쿼리 4: 담당자별 액션 (선택)
└─ 쿼리 5: 월별 통계 (선택)
```

---

## 🔗 관련 파일

| 파일 | 역할 |
|------|------|
| **ACTION_ITEMS.md** | 액션 목록 (쿼리 1의 데이터) |
| **Meetings/** | 회의 기록 (쿼리 2의 데이터) |
| **Decisions/** | 결정사항 (쿼리 3의 데이터) |
| **PLUGINS_SETUP.md** | Dataview 설정 가이드 |

---

## ✨ 팁

### 자동 갱신
- ACTION_ITEMS.md 저장 → 쿼리 1 자동 갱신
- 새 회의 추가 → 쿼리 2 자동 갱신
- 결정 추가 → 쿼리 3 자동 갱신

### 실시간 필터링
클릭 후 테이블 헤더에서:
- 정렬 변경 가능
- 필터링 가능
- 검색 가능

### 링크 네비게이션
- 액션명 클릭 → ACTION_ITEMS.md로 이동
- 회의명 클릭 → 회의 기록으로 이동
- 담당자명 클릭 → 담당자 프로필로 이동 (있을 경우)

---

## 📝 메타데이터

```yaml
type: dashboard
category: dataview
updated: 2026-08-14
queries: 3 (+ 2 optional)
```

---

**마지막 업데이트**: 2026-08-14  
**Dataview 버전**: 5.3+  
**상태**: ✅ 활성
