## `index.tsx` 전체 코드
```tsx
import { StyleSheet, Text, View } from 'react-native'
import LeftSidebar from 'app/components/menu/LeftSidebar'
import StudentGrid from './StudentGrid'

const index = () => {
  return (
    <View style={styles.container}>
      <LeftSidebar />
      <StudentGrid />
    </View>
  )
}

export default index

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: "row",
  },
})
```