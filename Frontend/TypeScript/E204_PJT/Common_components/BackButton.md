## `BackButton` 전체 코드

```tsx
import { Pressable, Image, StyleSheet } from 'react-native'
import { router } from 'expo-router'

interface BackButtonProps {
  onPress?: () => void   // 필요하면 커스텀 동작
  size?: number
}

const BackButton = ({ onPress, size = 24 }: BackButtonProps) => {
  const handlePress = () => {
    if (onPress) {
      onPress()
    } else {
      router.back() // 기본 동작: 뒤로가기
    }
  }

  return (
    <Pressable onPress={handlePress} style={styles.container}>
      <Image
        source={require('../../assets/icons/back.png')}
        style={{ width: size, height: size }}
        resizeMode="contain"
      />
    </Pressable>
  )
}

export default BackButton

const styles = StyleSheet.create({
  container: {
    padding: 8,   // 터치 영역 확보 (중요)
  },
})
```


## 코드 해석

### 