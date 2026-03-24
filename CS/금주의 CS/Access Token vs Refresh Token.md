## Access Token vs Refresh Token

### 🔑 Access Token
**API 요청 시 인증에 사용되는 토큰**
- 유효기간이 짧음 (보통 몇 분 ~ 1시간)
- 실제 요청에 사용됨

---

### 🔄 Refresh Token
**Access Token을 재발급 받기 위한 토큰**
- 유효기간이 김 (며칠 ~ 몇 주)
- 서버에 저장되는 경우 많음

---

### 동작 흐름
1. 로그인 성공
2. 서버 → Access Token + Refresh Token 발급
3. 클라이언트 요청 시 -> Access Token 사용
4. Access Token 만료 X -> Refresh Token으로 재발급 요청
5. 서버 → 새 Access Token 발급

---

### 왜 두 개를 나눌까?
- 핵심 이유 = 보안 + 사용자 경험
- Access Token만 사용하면
  - 유효기간 길게 하면 → 탈취 시 위험
  - 짧게 하면 → 계속 로그인해야 함

---

### 해결 (Access + Refresh 구조)
- Access Token → 짧게 (보안)
- Refresh Token → 길게 (편의성)

=> 보안 + UX 둘 다 잡음

---

### 저장 위치
| 토큰            | 저장 위치            |
| ------------- | ---------------- |
| Access Token  | 메모리 / 쿠키         |
| Refresh Token | httpOnly 쿠키 / DB |

---

### 주의할 점
- Refresh Token은 서버에서 관리해야 안전
- 탈취 대비 → 재발급 시 기존 토큰 폐기
- HTTPS 필수

---

## 한 줄 정리 (면접용)
- **Access Token은 인증에 사용되는 짧은 토큰이고, Refresh Token은 Access Token을 재발급하기 위한 긴 토큰이다.**