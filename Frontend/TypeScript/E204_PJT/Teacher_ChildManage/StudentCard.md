## `StudentCard.tsx` 전체 코드
```tsx
import { StyleSheet, Text, View, Image, Pressable } from 'react-native'

interface StudentCardProps {
  name: string
  number: number
  onPress?: () => void
}

const StudentCard = ({ name, number, onPress }: StudentCardProps) => {
  return (
    <Pressable style={styles.card} onPress={onPress}>
      <Image
        source={require('../../assets/seed.png')}
        style={styles.image}
        resizeMode="contain"
      />
      <Text style={styles.text}>
        {number}번 {name}
      </Text>
    </Pressable>
  )
}

export default StudentCard
```


## 1️⃣ import 부분
```tsx
import { StyleSheet, Text, View, Image, Pressable } from 'react-native'
```
- StyleSheet -> RN에서 스타일을 객체로 관리하는 도구 (CSS 역할)
- Text -> RN에서 글자를 표시할 때 쓰는 컴포넌트
- View -> div 같은 컨테이너 역할
- Image -> 이미지 표시
- Pressable -> “눌 수 있는 영역” (버튼, 카드 등) 



## 2️⃣ props 타입 정의
```tsx
interface StudentCardProps {
  name: string
  number: number
  onPress?: () => void
}
```
**StudentCard 컴포넌트는 반드시 이 정보들을 받아야 한다**

- `name: string` -> 학생 이름 (필수)
- `number: number` -> 학생 번호 (필수)
- `onPress?: () => void` -> 카드 클릭 시 실행할 함수 (선택)

#### 📌 ?의 의미
- 있어도 되고 없어도 됨
- 나중에 “학생 상세 페이지 이동” 같은 거 연결할 때 사용


## 3️⃣ 컴포넌트 선언부

```tsx
const StudentCard = ({ name, number, onPress }: StudentCardProps) => {
```
