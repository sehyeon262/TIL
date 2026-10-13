## Replication (데이터 복제)

### 📌 개념
- **Replication은 동일한 데이터를 여러 서버에 복제하여 저장하는 기술이다.**
- 즉, 하나의 DB만 사용하는 것이 아니라 **여러 DB에 같은 데이터를 복사해서 저장**

---

### 📌 왜 필요할까?
- 서버 장애 발생 시 데이터 손실 위험
- 트래픽 증가 시 성능 저하

그래서
```
Primary DB → Replica DB1
            → Replica DB2
```
=> 데이터 복제 -> **안정성 + 성능 확보**

---

### 📌 구조
#### Primary (Master)
- 쓰기(Write) 담당

#### Replica (Slave)
- 읽기(Read) 담당

=> Write는 한 곳, Read는 여러 곳

---

### 📌 장점
- 가용성(Availability) 향상
- 장애 시 빠른 복구 가능
- Read 성능 향상

---

### 📌 단점
- 데이터 동기화 지연 (Replication Lag)
- 일관성 문제 발생 가능
- 구조 복잡

---

### 📌 Sharding과 차이
| 구분  | Replication | Sharding |
| --- | ----------- | -------- |
| 데이터 | 동일          | 분산       |
| 목적  | 안정성         | 성능       |
| 읽기  | 분산 가능       | 분산       |
| 쓰기  | Primary만    | 분산 가능    |

---

### 📌 핵심 포인트 (면접용)
- Replication = **데이터 복제**
- Sharding = **데이터 분산**
- Read/Write 분리 구조
- 결국 **CAP Theorem과 연결됨**

---

### 📌 한 줄 정리
> Replication은 동일한 데이터를 여러 DB에 복제하여 가용성과 읽기 성능을 높이는 기술이다.