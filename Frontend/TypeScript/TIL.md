## 🔵 accessToken 만료는 어떻게 감지하는가?

### 먼저 결론부터
**프론트는 “토큰이 만료됐는지” 스스로 모른다 => 서버가 알려준다**

---

### 실제 상황 흐름

#### 1️⃣ 정상일 때
```txt
요청 → Authorization: Bearer accessToken
서버 → 200 OK + 데이터
```

#### 2️⃣ 토큰 만료됐을 때
```txt
요청 → Authorization: Bearer accessToken
서버 → 401 Unauthorized ❌
```
**📌 401 = “토큰 문제”**

---

### 프론트에서는 뭘 하냐?
#### 가장 단순한 처리
```ts
try {
  await axios.get(...);
} catch (error: any) {
  if (error.response?.status === 401) {
    // 토큰 만료 or 인증 실패
    dispatch(logout());
  }
}
```
👉 401 오면 로그아웃 + 다시 로그인 유도


---


## 🔵 SecureStore vs Redux

### 한 줄 요약 먼저
| 구분          | 역할               |
| ----------- | ---------------- |
| Redux       | **앱 실행 중** 상태 기억 |
| SecureStore | **앱 껐다 켜도** 유지   |

---

### 🔥 Redux란?
**“지금 앱이 살아있는 동안의 메모장”**

#### 특징
- 앱 종료 → ❌ 다 날아감
- 화면 간 상태 공유
- 빠름

#### authSlice 예시
```ts
state.accessToken
state.isLoggedIn
state.teacherData
```
- 화면에서 바로 쓰기 좋음

---

### 🔥 SecureStore란?
**“폰에 안전하게 저장하는 금고”**

#### 특징
- 앱 종료 → ⭕ 유지됨
- 보안 저장소
- 느리지만 안전

#### 예시
```ts
SecureStore.setItemAsync('accessToken', token)
```
- 새로 앱 켰을 때 로그인 유지용

---

### 이걸 왜 둘 다 쓰냐?

#### ❌ SecureStore만 쓰면?
- 매번 async로 꺼내야 함
- UI 렌더링 느림
- 코드 더러워짐

#### ❌ Redux만 쓰면?
- 앱 껐다 켜면 로그아웃됨
- 새로고침에 취약

---

### ✅ 그래서 정답 구조는 이거
```txt
로그인 성공
   ↓
SecureStore에 저장 (영구 보관)
   ↓
Redux에 저장 (즉시 사용)
```

---

### 실제 흐름을 사람 말로 하면
#### 로그인 순간
**“이 토큰은 지금도 쓰고, 나중에 다시 켜도 써야 해”**
=> 둘 다 저장

#### API 요청할 때
```ts
const token = state.auth.accessToken;
```
👉 **Redux에서만 꺼냄 (빠름)**

#### 앱 재시작 시
```ts
const token = await SecureStore.getItemAsync('accessToken');
dispatch(setToken(token));
```
👉 **SecureStore → Redux 복구**