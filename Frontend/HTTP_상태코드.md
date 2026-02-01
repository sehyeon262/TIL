## HTTP 상태 코드 (웹 브라우저 에러)
**웹사이트에 접속할 때 발생하는 코드로, 크게 5가지 카테고리로 나뉩니다.**

### 🟢 2xx (성공: Success)
- **200 OK** : 요청이 성공적으로 처리됨.
- **201 Created** : 요청이 성공적이었고, 새로운 리소스가 생성됨.

---

### 🟡 3xx (리다이렉션: Redirection)
- **301 Moved Permanently** : 주소가 영구적으로 바뀜.
- **302 Found** : 주소가 일시적으로 이동함.

---

### 🟠 4xx (클라이언트 오류: Client Error) - 사용자 잘못
- **400 Bad Request** : 요청 자체가 잘못됨 (오타나 형식 오류).
- **401 Unauthorized** : 권한 없음 (로그인 필요).
- **403 Forbidden** : 접근 금지 (로그인은 했으나 권한이 없는 페이지).
- **404 Not Found** : 가장 흔한 에러. 페이지를 찾을 수 없음 (주소 오타 등).
- **408 Request Timeout** : 요청 대기 시간 초과.

---

### 🔴 5xx (서버 오류: Server Error) - 관리자 잘못
- **500 Internal Server Error** : 서버 내부의 알 수 없는 오류.
- **502 Bad Gateway** : 서버 간의 통신 불량 (게이트웨이 오류).
- **503 Service Unavailable** : 서버 과부하 또는 점검 중.
- **504 Gateway Timeout** : 서버 응답 시간이 너무 오래 걸림.