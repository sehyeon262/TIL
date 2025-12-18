# 🌐 Java Web (Back-end) Repository

- Java 기반 **웹 백엔드 + DB** 흐름을 이해하고, Servlet → JSP → DB → 세션/필터까지 단계적으로 학습합니다.

## 📌 학습 목표  
- Java 웹의 전체 요청–응답 흐름 이해  
- Servlet / JSP 역할 구분  
- DB 연동(CRUD) 기본 구조 익히기  
- 로그인/권한 처리의 기초 개념 이해


---


## 📚 학습 순서 

- 아래 순서대로 공부하며 각 항목별로 **폴더 생성 + 정리 파일 작성**을 기록했습니다.


### 1️⃣ Servlet 1
📂 `01_Servlet_Basic`

#### 🔹 학습 내용
- 웹의 기본 구조 (Client / Server)
- Servlet 개념과 역할
- 요청(Request) / 응답(Response)
- `doGet`, `doPost`
- URL 매핑 (`@WebServlet`)

#### 🔹 정리 포인트
- Servlet이 왜 필요한가?
- 요청 흐름 (브라우저 → 서버 → Servlet)
- GET vs POST 차이

---

### 2️⃣ Servlet 2
📂 `02_Servlet_Advanced`

#### 🔹 학습 내용
- request / response 객체 심화
- 파라미터 처리 (`getParameter`)
- redirect vs forward
- MVC 패턴 기초 (Controller 역할)

#### 🔹 정리 포인트
- redirect / forward 차이
- Servlet이 Controller인 이유

---

### 3️⃣ JSP 1
📂 `03_JSP_Basic`

#### 🔹 학습 내용
- JSP 개념과 필요성
- JSP 기본 문법
- Scriptlet, Expression
- JSP 동작 원리 (Servlet 변환)

#### 🔹 정리 포인트
- Servlet vs JSP 역할 차이
- JSP가 View인 이유

---

### 4️⃣ JSP 2
📂 `04_JSP_Advanced`

#### 🔹 학습 내용
- JSP 내장 객체
- include / forward
- 페이지 흐름 제어
- MVC 구조에서 JSP 위치

#### 🔹 정리 포인트
- JSP에서 로직을 최소화해야 하는 이유

---

### 5️⃣ Cookie & Session
📂 `05_Cookie_Session`

#### 🔹 학습 내용
- Cookie 개념
- Session 개념
- 로그인 처리 흐름
- 상태 유지 방식

#### 🔹 정리 포인트
- Cookie vs Session 차이
- 로그인 정보는 왜 Session에 저장할까?

---

### 6️⃣ JSTL & EL
📂 `06_JSTL_EL`

#### 🔹 학습 내용
- EL(Expression Language)
- JSTL Core 태그
- 조건문 / 반복문
- JSP에서 Java 코드 제거

#### 🔹 정리 포인트
- Scriptlet을 사용하지 않는 이유
- JSTL을 쓰는 이유

---

### 7️⃣ Filter
📂 `07_Filter`

#### 🔹 학습 내용
- Filter 개념
- 요청/응답 가로채기
- 인코딩 처리
- 인증/권한 필터

#### 🔹 정리 포인트
- Filter가 필요한 상황
- Servlet과 Filter 차이

---

### 8️⃣ DB SELECT 기본
📂 `08_DB_SELECT_Basic`

#### 🔹 학습 내용
- JDBC 개념
- DB 연결 흐름
- SELECT 문 기본
- ResultSet 처리

#### 🔹 정리 포인트
- JDBC 전체 흐름
- SELECT 동작 과정

---

### 9️⃣ DB SELECT 응용
📂 `09_DB_SELECT_Advanced`

#### 🔹 학습 내용
- WHERE / ORDER BY
- PreparedStatement
- 다중 조회
- 페이징 개념

#### 🔹 정리 포인트
- Statement vs PreparedStatement
- SQL Injection 개념

---

### 🔟 DML & DDL
📂 `10_DML_DDL`

#### 🔹 학습 내용
- INSERT / UPDATE / DELETE
- DML 개념
- DDL 개념 (CREATE, DROP)
- CRUD 전체 흐름

#### 🔹 정리 포인트
- CRUD 구조 정리
- 웹에서 DB 처리 흐름 요약


---


## ✨ 한 줄 요약
- **Servlet → JSP → Session → Filter → DB**  
- Java 웹 백엔드의 전체 흐름을 이해하는 것이 목표 🚀