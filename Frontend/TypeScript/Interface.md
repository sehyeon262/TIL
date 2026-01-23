## ◼️ Interface 란?
**interface = 이 컴포넌트 사용 설명서**


---


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


---


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


---


## ◼️ interface가 없으면 생기는 문제
- size에 문자열을 넣어도 에러가 안 남
- onPress를 숫자로 넣어도 모름
- 팀원이 잘못 써도 막을 방법 없음


---


## ◼️ interface의 핵심 역할 3가지
### 1. 타입 안전성
```tsx
<BackButton size="크게" />
```

### 2. 자동 완성
VSCode에서 `<BackButton` 입력 시 `onPress`, `size` 자동으로 뜸

### 3. 협업용 설명서
- "이 컴포넌트 이렇게 쓰세요" 라고 말 안 해도 됨


---


## 📑 한 문장 요약
** interface는 컴포넌트가 받을 props의 타입과 구조를 미리 정의하는 설계도이다.**


