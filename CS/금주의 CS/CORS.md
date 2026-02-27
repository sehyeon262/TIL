## CORS (Cross-Origin Resource Sharing)

1. **한 줄 정의**
- 서로 다른 출처(Origin)로 보내는 브라우저 요청을 서버가 "허용/차단" 하도록 하는 규칙

2. **Origin(출처)이란?**
- 프로토콜 + 도메인 + 포트
- 예) `https://a.com:3000` <-> `https://a.com:4000` 도 포트가 달라서 다른 출처

3. **왜 필요해?**
- 브라우저 기본 보안 정책 **SOP(동일 출처 정책)** 때문에 다른 출처로의 요청/응답 접근을 막음 => 필요한 경우만 예외 허용하려고 CORS 사용

4. **동작 방식 (핵심만)**
- **Simple Request** : 조건이 단순하면 바로 요청
- **Preflight Request(OPTIONS)**: 조건이 복잡하면 먼저 “해도 돼?” 확인 후 본 요청

5. **서버가 내려주는 주요 헤더**
- `Access-Control-Allow-Origin` : 허용할 출처
- `Access-Control-Allow-Methods` : 허용 메서드
- `Access-Control-Allow-Headers` : 허용 헤더
- `Access-Control-Allow-Credentials` : 쿠키/세션 포함 허용 여부

6. **자주 하는 실수/주의**
- CORS는 브라우저에서만 적용(서버-서버 통신은 보통 영향 X)
- 문제는 대부분 프론트가 아니라 서버 설정(응답 헤더) 쪽 쿠키/세션 (credentials) 쓰면 `Allow-Origin: *` 불가 → 특정 도메인 명시해야 함

7. **면접 단골 질문**
- CORS가 뭔가요? SOP랑 차이는?
- Preflight는 언제 왜 발생하나요?
- 쿠키/세션 인증에서 CORS 설정은 어떻게 하나요?