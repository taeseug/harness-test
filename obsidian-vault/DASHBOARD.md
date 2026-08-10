---
type: dashboard
category: overview
date: 2026-08-10
---

# 📊 회의 관리 시스템 대시보드

> **실시간 액션, 회의, 결정사항 추적**  
> 마지막 업데이트: 2026-08-10

---

## 🎯 현재 현황

### 📌 진행 중인 액션

**📊 통계:**
- 총 아이템: 14개
- ✅ 완료: 11개 (79%)
- ⏳ 진행 중: 2개 (14%)
- ⏸️ 보류: 1개 (7%)

**상세 보기:** [[Meetings/QUERIES.md#쿼리-1-진행-중인-액션|액션 조회]]

```dataview
TASK
WHERE status = "⏳"
LIMIT 5
```

**주요 액션:**
- [x] [[2026-04-16-PG사-선정#액션-아이템|박준서] PG사 연동 스펙 확보
- [x] [[2026-05-14-온보딩-개선-전략#액션-아이템|최민아] 온보딩 이탈률 분석
- [ ] 개발팀 - A사 결제 모듈 개발 (진행 중)
- [ ] 마케팅팀 - 결제 화면 메시지 개선 (진행 중)

---

## 📅 회의 타임라인

**기간:** 2026-04-16 ~ 2026-07-23 (14주)  
**총 회의:** 6개

### 최근 회의

```dataview
TABLE 
  file.name as "회의명",
  file.mday as "회의날짜",
  file.cday as "기록날짜"
FROM "Meetings"
WHERE type = "meeting" AND file.name != "QUERIES.md"
SORT file.mday DESC
LIMIT 6
```

**개별 회의:**
1. [[2026-07-23-제품주간회의.enhanced.md]] - 최근 회의
2. [[2026-07-09-제품주간회의.enhanced.md]]
3. [[2026-06-25-온보딩개선회의.enhanced.md]] - 온보딩 전략
4. [[2026-06-11-제품주간회의.enhanced.md]] - A사 스펙 확보
5. [[2026-05-14-제품주간회의.enhanced.md]] - 온보딩 분석
6. [[2026-04-16-제품주간회의.enhanced.md]] - PG사 선정

---

## ✅ 결정사항 현황

**확정된 결정:** 2개  
**진행 중:** 2개

### 주요 결정사항

```dataview
TABLE 
  type as "유형",
  status as "상태",
  owner as "담당자"
FROM "Decisions"
WHERE type = "decision"
SORT status
```

**결정 목록:**
1. **[[2026-04-16-PG사-선정|PG사 선정]]** ✅
   - 담당자: 박준서
   - 상태: 진행 중 (개발 단계)
   - 영향도: 높음

2. **[[2026-05-14-온보딩-개선-전략|온보딩 개선 전략]]** ✅
   - 담당자: 최민아
   - 상태: 진행 중 (실행 단계)
   - 영향도: 높음

---

## 📈 통계 & 성과

### 액션 완료율

| 기간 | 완료 | 진행 | 보류 | 완료율 |
|------|------|------|------|--------|
| 4월 | 3개 | 0 | 1 | 75% |
| 5월 | 4개 | 0 | 0 | 100% |
| 6월 | 3개 | 1 | 0 | 75% |
| 7월 | 1개 | 1 | 0 | 50% |
| **누계** | **11개** | **2개** | **1개** | **79%** |

### 회의 분포

```dataview
TABLE WITHOUT ID 
  choice(rows.file.mday, "정보없음") as "월",
  length(rows) as "회의수"
FROM "Meetings"
WHERE file.name != "QUERIES.md" AND file.name != "MEETINGS_ANALYSIS.md"
GROUP BY dateformat(file.mday, "yyyy-MM")
SORT rows.file.mday DESC
```

---

## 🎯 담당자별 액션

```dataview
TABLE WITHOUT ID 
  file.link as "액션",
  owner as "담당자"
FROM "Meetings"
LIMIT 10
```

---

## 🔗 주요 링크

### 📊 대시보드 & 쿼리
- [[Meetings/QUERIES.md|상세 쿼리 보기]] - 모든 Dataview 쿼리
- [[Meetings/MEETINGS_ANALYSIS.md|회의 분석]] - 타입별 분석

### 📌 핵심 자료
- [[Actions/ACTION_ITEMS.md|액션 아이템]] - 상세 액션 목록
- [[Decisions/README.md|결정사항 관리]] - 모든 의사결정 기록

### 📁 폴더 구조
- [[Meetings/README.md|회의 기록]]
- [[Actions/README.md|액션 관리]]
- [[Decisions/README.md|결정사항]]

---

## 📋 활용 팁

### 빠른 검색
1. **특정 액션 찾기**: `ACTION_ITEMS.md` 에서 Cmd+F
2. **회의별 액션 보기**: 각 회의 파일의 "액션 아이템" 섹션
3. **담당자별 보기**: 이 대시보드의 담당자별 테이블 클릭

### 실시간 갱신
- ACTION_ITEMS.md 저장 → 액션 쿼리 자동 갱신
- 새 회의 추가 → 회의 타임라인 자동 갱신
- 결정사항 추가 → 결정사항 테이블 자동 갱신

### 이동 네비게이션
- **회의명 클릭** → 해당 회의 기록으로 이동
- **액션명 클릭** → ACTION_ITEMS.md로 이동
- **담당자명 클릭** → 담당자의 액션 필터링

---

## 🎯 다음 단계 (Phase 3D)

- [ ] Claude API 자동화 (회의 기록 → 액션 자동 추출)
- [ ] Slack 통합 (액션 알림)
- [ ] 주간 요약 리포트 자동 생성

---

## 📞 문제 해결

### 쿼리가 렌더링 안 됨
```
1. Dataview 플러그인 활성화 확인
2. Obsidian 재시작 (Cmd + Q)
3. 캐시 새로고침 (Cmd + Shift + R)
```

### 데이터가 표시 안 됨
```
1. ACTION_ITEMS.md 저장 상태 확인
2. Decisions/ 폴더 파일 확인
3. Frontmatter 메타데이터 확인
```

---

## 📊 메타데이터

```yaml
type: dashboard
category: overview
queries: 5개
linked_files: 13개
last_updated: 2026-08-10
maintenance_status: 활성
```

---

**관리자**: Claude 시스템  
**버전**: 1.0  
**상태**: ✅ 활성
