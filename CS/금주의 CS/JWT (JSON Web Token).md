## JWT (JSON Web Token)

### 개념
- JWT는 인증 정보를 JSON 형태로 담아 안전하게 전달하기 위한 토큰 기반 인증 방식이다.
- 즉, 서버에 세션을 저장하지 않고 **토큰 하나로 인증 처리 (Stateless)**

---

### 구조
- JWT는 3부분으로 구성된다
```
Header.Payload.Signature
```

1. **Header**
- 토큰 타입
- 암호화 알고리즘

2. **Payload**
- 사용자 정보 (userId 등)
- 클레임 (Claim)

3. **Signature**
- 위 데이터들을 암호화한 값
- 위조 방지

---

### 동작 흐름
1. 로그인 요청
2. 서버 -> JWT 생성
3. 클라이언트에 전달 (보통 쿠키 or localStorage)
4. 이후 요청마다 JWT 포함
5. 서버는 토큰 검증 후 인증 처리

---

### 왜 사용하는가?
- 서버에 세션 저장 안 함 -> 확장성 좋음
- 인증 속도 빠름
- MSA 환경에 적합

---

### 단점 (면접 포인트!)
- 토큰 탈취 시 위험
- 로그아웃 처리 어려움
- 토큰 길이 큼

---

### Session vs JWT 핵심 차이
| 구분    | Session  | JWT       |
| ----- | -------- | --------- |
| 저장 위치 | 서버       | 클라이언트     |
| 상태    | Stateful | Stateless |
| 확장성   | 낮음       | 높음        |

---

### 한 줄 정리
- JWT는 서버 상태를 저장하지 않고 토큰 기반으로 인증을 처리하는 방식이다.

---

### 면접에서 이어지는 질문
- JWT 왜 쓰는가?
- JWT 단점 해결 방법? (Refresh Token)
- Access Token vs Refresh Token
- Stateless vs Stateful