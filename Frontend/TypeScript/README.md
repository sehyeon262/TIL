## TypeScript란?
**TypeScript = JavaScript + 타입(Type)**


---


## React 최소 개념 (이거 모르면 RN 이해 안 됨)
### 1️⃣ 꼭 알아야 할 4개
#### ① 함수형 컴포넌트
```ts
function App(){
    return <Text>Hello</Text>;
}
```
👉 RN도 전부 함수


#### ② JSX
```tsx
<View>
    <Text>안녕</Text>
</View>
```

👉 HTML ❌

👉 RN 전용 태그(View, Text)


#### ③ props
```ts
function Box({ title }: { title: string }) {
    return <Text>{title}</Text>;
}
```


#### ④ state (useState)
```ts
const [count, setCount] = useState(0);
```

---

### 2️⃣ React Native 구조 이해 (진짜 중요)
#### 🔹 RN 기본 태그 (외우자!!)

| 역할     | 태그                              |
| ------ | ------------------------------- |
| 컨테이너   | `View`                          |
| 글자     | `Text`                          |
| 버튼     | `Pressable`, `TouchableOpacity` |
| 입력     | `TextInput`                     |
| 화면 스크롤 | `ScrollView`                    |


#### 🔹 스타일 방식 (CSS ❌)
```ts
const styles = StyleSheet.create({
  box: {
    backgroundColor: "#fff",
    padding: 16,
  },
});
```


#### 🔹 Flexbox (RN 필수)
```ts
flexDirection: "row";
justifyContent: "space-between";
alignItems: "center";
```

#### ➕ (추가) Flexbox 3개만 알면 RN 레이아웃 80% 해결
1. flexDirection (방향)
```ts
flexDirection: "row" | "column";
```
- column (기본): 세로
- row: 가로

2. justifyContent (주축 정렬)
```ts
justifyContent: "center";
justifyContent: "space-between";
```
- 위/아래 또는 좌/우 배치 담당

3.  alignItems (교차축 정렬)
```ts
alignItems: "center";
```
- 가운데 정렬 담당

---

### 3️⃣ TypeScript – RN에서 필요한 것만
**❗ 지금 당장 필요한 TS 5개**

1. Props 타입
```ts
interface Props {
  title: string;
}

function Card({ title }: Props) {
  return <Text>{title}</Text>;
}
```

2. useState 타입
```ts
const [visible, setVisible] = useState<boolean>(false);
```

3. 배열 렌더링
```ts
interface Student (
    id: number;
    name: string;
)

const list: Student[] = [];
```

4. 이벤트
```ts
<Pressable onPress={() => setCount(count + 1)} />
```
👉 RN 이벤트는 onPress 하나면 끝

5. Optional
```ts
interface Props {
  subtitle?: string;
}
```

---

### 4️⃣ 무조건 만들어야 하는 패턴
#### 🔹 버튼 → 상태 변경
```tsx
const [on, setOn] = useState(false);

<Pressable onPress={() => setOn(!on)}>
  <Text>{on ? "ON" : "OFF"}</Text>
</Pressable>
```

#### 🔹 Props 전달
```tsx
<Card title="수업 시작" />
```

#### 🔹 조건부 렌더링
```tsx
{on && <Text>보임</Text>}
```

#### 🔹 FlatList (RN 핵심)
```tsx
<FlatList
  data={students}
  keyExtractor={(item) => item.id.toString()}
  renderItem={({ item }) => <Text>{item.name}</Text>}
/>
```

---

### 5️⃣ Navigation 

❗ **RN Navigation 필수**
```bash
npm install @react-navigation/native
```

#### 🔹 타입 정의 (진짜 중요)
```ts
type RootStackParamList = {
  Home: undefined;
  Detail: { id: number };
};
```

#### 🔹 이동
```ts
navigation.navigate("Detail", { id: 1 });
```

---


## React(TypeScript) vs React Native(TypeScript)

### 1️⃣ 같은 점 (핵심 개념은 90% 동일)
✔️ **타입스크립트 문법**
- `interface`, `type`
- `props`, `state` 타입 지정
- `useState`, `useEffect` 제네릭
- `union`, `enum`, `generic`

```ts
interface Props {
  title: string;
  count: number;
}
```
---
✔️ **React Hooks 타입 지정**
```ts
const [count, setCount] = useState<number>(0);
```
---
✔️ **컴포넌트 구조**
```ts
function MyComponent({ title }: Props) {
  return ...
}
```

---


### 2️⃣ 다른 점
- 가장 큰 차이: DOM vs Native 컴포넌트

| **구분**     | **React (Web)**   | **React Native**   |
| ------ | ------------- | -------------- |
| UI 기반  | DOM           | Native View    |
| 기본 태그  | `div`, `span` | `View`, `Text` |
| 이벤트 타입 | MouseEvent    | GestureEvent   |
| 스타일    | CSS           | StyleSheet     |


---


### 3️⃣ 타입 차이 실제 예제

#### 🔹 React (웹)
```ts
const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {
  console.log(e.target);
};
```

#### 🔹 React Native
```ts
const handlePress = (e: GestureResponderEvent) => {
  console.log(e.nativeEvent);
};
```
👉 이벤트 타입이 다름


---

### 4️⃣ Props 타입 차이
#### 🔹 React Web
```ts
interface Props {
  onClick: () => void;
  children: React.ReactNode;
}
```

#### 🔹 React Native
```ts
interface Props {
  onPress: () => void;
  children: React.ReactNode;
}
```
📌 onClick ❌ → onPress ⭕


---


### 5️⃣ 스타일 타입 차이 (중요)
#### 🔹 React (CSS)
```ts
const style: React.CSSProperties = {
  backgroundColor: "red",
};
```

#### 🔹 React Native
```ts
import { StyleSheet } from "react-native";

const styles = StyleSheet.create({
  box: {
    backgroundColor: "red",
    flex: 1,
  },
});
```

👉 RN은 CSS 타입이 아예 없음


---


### 6️⃣ useRef 타입 차이 (자주 터짐)
#### 🔹 React Web
```ts
const inputRef = useRef<HTMLInputElement>(null);
```

#### 🔹 React Native
```ts
const inputRef = useRef<TextInput>(null);
```


---


### 7️⃣ Navigation 타입 (RN에서만 있음)
- React Native는 **라우팅이 라이브러리 기반**
```ts
type RootStackParamList = {
  Home: undefined;
  Detail: { id: number };
};
```
```ts
const navigation = useNavigation<NativeStackNavigationProp<RootStackParamList>>();
```

👉 웹 React에는 거의 없음