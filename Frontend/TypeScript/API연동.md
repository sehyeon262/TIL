# 📡 React Native API 연동 가이드 (Expo 기준)
이 문서는 **React Native(Expo) 프로젝트에서 백엔드 API를 연동하는 전체 과정**을 정리한 문서입니다.


---


## 1️⃣ API 연동 개념
- React Native는 **DB에 직접 접근하지 않는다**
- 프론트엔드는 **HTTP 요청(API)** 을 통해 백엔드와 통신한다
- 주고받는 데이터 형식은 보통 **JSON**

```js
React Native → API 요청 → Backend → DB
React Native ← JSON 응답 ← Backend
```


## 2️⃣ 사전 준비 사항
- Expo 기반 React Native 프로젝트
- 백엔드 서버 실행 중 (Django / Spring 등)
- 같은 네트워크 환경 (실기기 사용 시)



## 3️⃣ 서버 주소 설정 (.env)

### 📁 .env
```env
EXPO_PUBLIC_API_URL=http://192.168.30.183:8080
```

### 📌 주의사항
- 반드시 `EXPO_PUBLIC_` 으로 시작해야 함
- 값 변경 후 Expo 재시작 필수
```bash
npx expo start -c
```


## 4️⃣ axios 설치
```bash
npm install axios
```


## 5️⃣ axios 공통 설정 파일 생성 (권장 ⭐)
### 📁 폴더 구조 예시
```bash
frontend/
 ├─ app/
 │   ├─ services/
 │   │   ├─ api.ts
 │   │   ├─ auth.ts
 │   │   └─ statistics.ts
 │   └─ screens/
 └─ .env
```

### 📄 app/services/api.ts
```ts
import axios from 'axios'

const api = axios.create({
  baseURL: process.env.EXPO_PUBLIC_API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 5000,
})

export default api
```


#### 📌 역할
- 서버 주소 관리
- 공통 헤더 설정
- 모든 API 요청의 기준 파일



## 6️⃣ API 함수 분리 작성
### 📄 app/services/auth.ts
```ts
import api from './api'

export const teacherSignup = async (
  email: string,
  password: string,
  teacherName: string
) => {
  const res = await api.post('/teacher/signup', {
    email,
    password,
    teacherName,
  })

  return res.data
}
```

#### 📌 원칙
- UI 코드 작성 ❌
- API 요청/응답만 담당


## 7️⃣ 화면에서 API 사용
### 📄 TeacherSignup.tsx
```tsx
import { teacherSignup } from '../services/auth'

const handleSignup = async () => {
  try {
    const result = await teacherSignup(
      'ssafy@ssafy.com',
      'ssafy204',
      'ssafy'
    )
    console.log('회원가입 성공:', result)
  } catch (error) {
    console.error('회원가입 실패:', error)
  }
}
```

#### 📌 역할 분리
| 파일       | 역할          |
| -------- | ----------- |
| services | 서버 통신       |
| screens  | 화면 + 이벤트 처리 |



## 8️⃣ Android 네트워크 설정 (HTTP 사용 시 필수)
### 📄 app.json
```json
{
  "expo": {
    "android": {
      "usesCleartextTraffic": true
    }
  }
}
```


## 9️⃣ 서버 주소 주의사항
- 실행 환경별 서버 주소
| 환경            | 주소                      |
| ------------- | ----------------------- |
| Android 에뮬레이터 | `http://10.0.2.2:8080`  |
| iOS 시뮬레이터     | `http://localhost:8080` |
| 실제 기기         | `http://내PC_IP:8080`    |


## 1️⃣0️⃣ 자주 발생하는 에러
### ❌ Network Error
- 서버 실행 주소 문제
- 네트워크 차단
- IP 접근 불가

### ❌ undefined response
- 서버에 요청이 도달하지 못함



## 1️⃣1️⃣ API 연동 흐름 요약
```scss
.env 설정
↓
axios 공통 파일(api.ts)
↓
API 함수 분리(auth.ts 등)
↓
화면에서 호출
↓
응답 데이터로 UI 업데이트
```