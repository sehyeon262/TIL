## Isolation Level (트랜잭션 격리 수준)


### 개념
- Isolation Level은 여러 트랜잭션이 동시에 실행될 때 서로 얼마나 영향을 주지 않도록 격리할 것인지 정하는 수준이다.
- 즉, 동시성 vs 데이터 정합성 사이의 균형을 조절하는 설정이다.

---

### 왜 필요한가?
동시에 여러 트랜잭션이 실행되면
- 데이터가 꼬일 수 있음
- 잘못된 값 읽을 수 있음

그래서 **격리 수준을 정해서 문제를 방지**

---

### 주요 문제
1. Dirty Read
- 아직 커밋되지 않은 데이터를 읽음

2. Non-Repeatable Read
- 같은 쿼리를 두 번 했는데 값이 다름

3. Phantom Read
- 같은 조건 조회인데 행(row)이 추가/삭제됨

---

### Isolation Level 4단계
1. Read Uncommitted (가장 낮음)
- Dirty Read 발생 가능
- 성능 가장 빠름

2. Read Committed
- Dirty Read 방지
- 대부분 DB 기본 설정

3. Repeatable Read
- Non-Repeatable Read 방지
- 같은 데이터는 동일하게 유지

4. Serializable (가장 높음)
- 모든 문제 방지
- 대신 성능 가장 느림

---

### 정리표
| Level            | Dirty Read | Non-Repeatable | Phantom |
| ---------------- | ---------- | -------------- | ------- |
| Read Uncommitted | O          | O              | O       |
| Read Committed   | X          | O              | O       |
| Repeatable Read  | X          | X              | O       |
| Serializable     | X          | X              | X       |

---

### 핵심 포인트 (면접용)
- 격리 수준이 높을수록 → 정합성 ↑ / 성능 ↓
- 격리 수준이 낮을수록 → 성능 ↑ / 데이터 오류 가능성 ↑

---

### 면접에서 이어지는 질문
- MySQL 기본 격리 수준은? (Repeatable Read)
- Phantom Read는 왜 발생하는가
- 락(Lock)과의 관계
- Optimistic vs Pessimistic Lock

---

### 한 줄 정리
> **Isolation Level은 트랜잭션 간 간섭을 얼마나 허용할지 정하는 기준이다.**