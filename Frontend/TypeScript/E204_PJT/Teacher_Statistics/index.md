## 전체 코드
```tsx
import { StyleSheet, Text, View } from 'react-native'
import React from 'react'
import LeftSidebar from '../../components/menu/LeftSidebar'
import BackButton from 'app/components/menu/BackButton'
import StatisticsHeader from '../../components/menu/StatisticsHeader'
import { useLocalSearchParams } from 'expo-router'

const index = () => {

  const { name, number } = useLocalSearchParams<{
    name: string
    number: string
  }>()

  return (
    <View style={styles.container}>
      <LeftSidebar />

      <View style={styles.content}>
        <StatisticsHeader
          name={name}
          number={Number(number)}
        />
      </View>
    </View>
  )
}

export default index

const styles = StyleSheet.create({

  container: {
    flexDirection: "row",
    backgroundColor: "#F3EED4",
    flex: 1,
  },

  content: {
    flex: 1,
    padding: 16,
  },
})
```
