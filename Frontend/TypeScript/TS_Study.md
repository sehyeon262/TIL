## 📌 목차
- [Props](#Props)
- [Interface](#Interface)


---


# Props

## 1️⃣ props란?
**props = 부모가 자식에게 주는 값(데이터)**

## 2️⃣ 비유로 이해하자! (버튼에 글자 넣기)
### ❌ props 없는 컴포넌트
```tsx
const MyButton = () => {
  return <Text>확인</Text>
}
```
이 버튼은 **무조건 '확인'만 나옴**


### ✅ props 있는 컴포넌트
```tsx
const MyButton = ({ text }) => {
  return <Text>{text}</Text>
}
```
이제 이 버튼은 **넣어주는 값에 따라 달라짐**


### props를 “넣어주는 쪽” (부모)
```tsx
<MyButton text="확인" />
<MyButton text="취소" />
<MyButton text="뒤로가기" />
```
**결과**
- 첫 번째 버튼 -> 확인
- 두 번째 버튼 -> 취소
- 세 번째 버튼 -> 뒤로가기

👉 **같은 컴포넌트, 다른 결과** 이게 props임!! 



## 3️⃣ props 기본 구조
### 🔹 부모 컴포넌트
```tsx
<BackButton size={32} />
```

### 🔹 자식 컴포넌트
```tsx
const BackButton = ({ size }: { size: number }) => {
  ...
}
```
👉 부모 → 자식 방향 단방향 전달


## 4️⃣ BackButton 예제로 props 흐름 보기
### 1. 부모가 props를 넘김
```tsx
<BackButton size={40} />
```

### 2. props가 객체로 전달됨
```ts
props = {
  size: 40
}
```


### 3. 구조 분해 할당으로 꺼냄
```ts
const BackButton = ({ size }) => {
```
👉 props.size 대신 size 바로 사용



## 5️⃣ props + interface 같이 보기
```ts
interface BackButtonProps {
  size?: number
  onPress?: () => void
}
```
```ts
const BackButton = ({ size = 24, onPress }: BackButtonProps) => {
```
| 항목          | 의미            |
| ----------- | ------------- |
| `size?:`    | 안 줘도 됨        |
| `size = 24` | 안 주면 기본값 24   |
| `onPress?:` | 함수일 수도, 없을 수도 |



## 6️⃣ props로 함수 전달하기



## 7️⃣



## 8️⃣

---


# Interface

## ◼️ Interface 란?
**interface = 이 컴포넌트 사용 설명서**



## ◼️ 비유로 비교해보자 !

### ❌ interface 없을 때
```tsx 
<BackButton 뭐 넣어야 하지... ?>
```
- onPress 넣어야 하나?
- size는 숫자야? 문자열이야?
- 안 넣어도 돼?

  👉 아무도 모름.. 혼돈!!


### ✅ interface 있을 때
```ts
interface BackButtonProps {
  onPress?: () => void
  size?: number
}
```
- BackButton 사용법
  - `onPress` : 함수 or 안 줘도 됨
  - `size` : 숫자 or 안 줘도 됨



## ◼️ ? (물음표)의 의미
```ts
onPress?: () => void
```
### 🔹 무슨 의미냐?
- `onPress`는 있어도 되고 없어도 된다!


### 🔹 예시
**1번**
```tsx
<BackButton />
```

**2번**
```tsx
<BackButton size={32} />
```

**3번**
```tsx
<BackButton onPress={() => console.log('뒤로')} />
```

**4번**
```tsx
<BackButton
  size={40}
  onPress={() => router.replace('/home')} 
/>
```



## ◼️ interface가 없으면 생기는 문제
- size에 문자열을 넣어도 에러가 안 남
- onPress를 숫자로 넣어도 모름
- 팀원이 잘못 써도 막을 방법 없음



## ◼️ interface의 핵심 역할 3가지
### 1. 타입 안전성
```tsx
<BackButton size="크게" />
```

### 2. 자동 완성
VSCode에서 `<BackButton` 입력 시 `onPress`, `size` 자동으로 뜸

### 3. 협업용 설명서
- "이 컴포넌트 이렇게 쓰세요" 라고 말 안 해도 됨



## 📑 한 문장 요약
**interface는 컴포넌트가 받을 props의 타입과 구조를 미리 정의하는 설계도이다.**


---


# State(상태)

## ◼️ 예시 코드 : `WeeklyCalendar.tsx`

### 1️⃣ 전체 구조 한 번에 보기
```ts
const [
  상태값,
  상태를바꾸는함수
] = useState<상태의타입>(초기값)
```

### 2️⃣ useState는 배열을 반환한다
```tsx
useState(...)  // 결과
→ [값, 값을바꾸는함수]
```

그래서 **배열 구조 분해 할당**을 쓰는 거야.
```ts
const arr = [10, () => {}]

const [a, b] = arr
// a = 10
// b = 함수
```

👉 리액트의 useState도 정확히 이 구조


### 3️⃣ selectedDate의 타입 구조 (가장 중요)
```ts
useState<Date | null>
```
- `selectedDate`는 `Date`일 수도 있고, `null`일 수도 있다

- 왜 null이 필요할까?
  - 아직 날짜를 선택 안 했을 때 상태를 표현하기 위해서
```ts
null = 선택 안 됨
Date = 선택됨
```


### 4️⃣ 초기값 null의 의미
```ts
useState<Date | null>(null)
```

👉 컴포넌트가 처음 렌더링될 때
```ts
selectedDate === null
```

즉,
- 아직 아무 날짜도 클릭 안 함
- Apply 버튼 비활성화 상태

이 로직이 여기랑 연결됨 👇
```ts
disabled={!selectedDate}
```

