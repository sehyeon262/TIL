## Load Balancing (로드 밸런싱)

### 1. 개념
- **Load Balancing은 여러 서버에 트래픽을 분산하여 서버 부하를 줄이고 시스템 성능과 안정성을 높이는 기술**이다.
- 즉, 사용자의 요청을 여러 서버에 나눠서 처리하게 만드는 것이다.

```
Client → Load Balancer → Server1
→ Server2
→ Server3
```

---

### 2. Load Balancing이 필요한 이유

서버가 한 대만 있을 경우

- 트래픽 증가 시 서버 과부하 발생
- 응답 속도 저하
- 서버 장애 시 서비스 전체 중단

Load Balancer를 사용하면

- 트래픽 분산
- 서버 과부하 방지
- 가용성(Availability) 향상
- 확장성(Scalability) 확보

---

### 3. 주요 Load Balancing 알고리즘
#### Round Robin
- 요청을 **순서대로 서버에 분배**하는 방식
```
요청1 → Server1
요청2 → Server2
요청3 → Server3
```

**장점**  
- 구현이 단순함

**단점**  
- 서버 성능 차이를 고려하지 않음

---

#### Least Connection
- **현재 연결 수가 가장 적은 서버**로 요청을 전달

**장점**  
- 트래픽 분배 효율적

**단점**  
- 연결 수 계산 필요

---

#### IP Hash
- **클라이언트 IP 기반으로 서버를 선택**

**장점**  
- 동일 사용자가 같은 서버에 연결됨  
- 세션 유지 가능

**단점**  
- 서버 부하 불균형 가능

---

### 4. Load Balancer 종류

#### L4 Load Balancer
- 전송 계층 기준으로 분산

**기준**
- IP
- Port
- TCP / UDP

**특징**
- 속도 빠름
- 네트워크 레벨 처리

**예시**
- AWS NLB

---

#### L7 Load Balancer
- 애플리케이션 계층 기준으로 분산

**기준**
- HTTP
- URL
- Header
- Cookie

**특징**
- 더 정교한 트래픽 제어
- 콘텐츠 기반 분산

**예시**
- Nginx
- AWS ALB

---

## 5. 실제 사용 예

대표적인 Load Balancer

- Nginx
- HAProxy
- AWS ALB
- AWS NLB

---

### 7. 면접에서 자주 나오는 질문

- Load Balancing이 필요한 이유는 무엇인가?
- L4와 L7 Load Balancer의 차이는 무엇인가?
- Round Robin 방식의 단점은 무엇인가?
- Scale Up과 Scale Out의 차이는 무엇인가?
- Sticky Session이란 무엇인가?

---

### 8. 한 줄 정리

> Load Balancing은 여러 서버에 요청을 분산하여 시스템의 성능, 가용성, 확장성을 높이는 기술이다.