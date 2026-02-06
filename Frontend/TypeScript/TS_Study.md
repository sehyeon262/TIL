## 📌 목차
- [Props](#Props)
- [Interface](#Interface)
- [State(상태)](#State(상태))


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


---


# Date 사용방법

## Date 객체 생성
- 아래와 같이 여러 방법으로 Date 객체를 생성함
- 객체의 메소드를 이용해 날짜 정보를 관리할 수 있음
```ts
const date1: Date = new Date(1919, 2, 1) // 1919-03-01 00:00:00
const date2: Date = new Date(1919, 2, 1, 19, 24, 51); // 1919-03-01 19:24:51
const date3: Date = new Date('1919-03-01 19:24:51')
```

## 현재 시간 반환 (get)
```ts
// Thu Jan 05 2023 23:10:06 GMT+0900 (대한민국 표준시)
console.log(Date());

const today = new Date();
// Thu Jan 05 2023 23:10:06 GMT+0900 (대한민국 표준시)
console.log(today.toString());
```
- 위 처럼 함수를 호출하여 현재 날짜를 반환할 수도 있고 
- 객체를 생성하여 반환할 수도 있으며 
- 위 두 방법으로 모두 현재 날짜를 얻을 수 있음


## Date의 인스턴스 메소드

### 년, 월, 일
```ts
const today: Date = new Date();
const year: number = today.getFullYear();
const month: number = today.getMonth() + 1;
const date: number = today.getDate();
console.log(`${year}-${month}-${date}`)
```
- month만 1을 더해줌 => `getMonth()` 함수가 0-11의 값을 반환하기 때문
- get 뒤에 UTC를 붙이면 현지 시간이 아닌 국제시간을 기준으로 시간을 반환하여 사용할 수 있음


### 응용: 00-31 두자리 날짜형식 표시, 0 넣기 (javascript, typescript)

- 위 코드를 실행해보면 뭔가 예쁘게 나오지 않습니다. 2023-1-5 이런식으로 나오기 때문입니다. 그래서 이를 예쁘게 두자리로 맞춰봄

```ts
function getFullDate(delimiter: string, year: number, month: number, date: number): string {
    return `${year}${delimiter}${month.toString().padStart(2, '0')}${delimiter}${date.toString().padStart(2, '0')}`
}

// 2023-01-05
console.log(getFullDate("-", year, month, date));
```
- padStart 라는 메소드를 이용해서 두자리 날짜형식으로 맞추되 빈 부분은 0으로 채워넣도록 함.


### 요일
- 요일 정보를 얻어서 사용해야할 때도 있음
```ts
enum DAY {
    SUNDAY,
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY
};

const day: number = today.getDay();
if (day === DAY.SUNDAY || day === DAY.SATURDAY) {
    console.log("쉬는 날");
} else {
    console.log("출근 하는 날 ㅠㅠ")
}
```
- `getDay()` 함수를 이용해서 요일을 반환 후 (0-6 반환하며 0이 일요일) 위와 같은 방식으로 enum을 정의해서 사용할 수 있음

