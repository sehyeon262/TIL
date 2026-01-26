## 전체 코드

```tsx
import { View, StyleSheet, Pressable, Text } from 'react-native'
import { ReactNode } from 'react'

interface StatisticsCardProps {
  children: ReactNode
}

const StatisticsCard = ({ children }: StatisticsCardProps) => {
  return (
    <View style={styles.wrapper}>
      <View style={styles.content}>
        {children}
      </View>
    </View >
  )
}

export default StatisticsCard

const styles = StyleSheet.create({
  wrapper: {
    backgroundColor: '#E3DDB5',
  },

  content: {
    borderWidth: 2,
    borderColor: '#3A2E1F',
    backgroundColor: '#E3DDB5',
    borderRadius: 5,
    padding: 16,
  },
})
```


---


## 전체 코드 주석
```tsx
import { View, StyleSheet, Pressable, Text } from 'react-native'
import { ReactNode } from 'react'

/**
 * StatisticsCard 컴포넌트가 받을 props 타입 정의
 */
interface StatisticsCardProps {
  /**
   * children
   * - 이 컴포넌트 안에 들어갈 모든 JSX 내용
   * - <StatisticsCard>여기 들어가는 내용</StatisticsCard>
   */
  children: ReactNode
}

/**
 * 통계 카드 공통 컴포넌트
 * - 내부 내용은 children으로 받아서 자유롭게 구성
 */
const StatisticsCard = ({ children }: StatisticsCardProps) => {
  return (
    // 카드의 바깥 배경 영역
    <View style={styles.wrapper}>
      {/* 실제 카드 내용 영역 */}
      <View style={styles.content}>
        {children}
      </View>
    </View>
  )
}

export default StatisticsCard

/**
 * 스타일 정의
 */
const styles = StyleSheet.create({
  // 카드 전체를 감싸는 바깥 영역
  wrapper: {
    backgroundColor: '#E3DDB5',
  },

  // 카드 안쪽 실제 콘텐츠 영역
  content: {
    borderWidth: 2,              // 테두리 두께
    borderColor: '#3A2E1F',      // 테두리 색
    backgroundColor: '#E3DDB5',  // 카드 배경색
    borderRadius: 5,             // 모서리 둥글게
    padding: 16,                 // 내부 여백
  },
})
```


---


## 핵심 개념 설명
### 1️⃣ children: ReactNode 이게 뭐야?
```tsx
interface StatisticsCardProps {
  children: ReactNode
}
```

👉 children은 “컴포넌트 안에 들어가는 내용” 전체를 의미

- 예를 들면 👇
```tsx
<StatisticsCard>
  <Text>주 평균 점수</Text>
  <Text>85점</Text>
</StatisticsCard>
```

이 안에 있는
```tsx
<Text>주 평균 점수</Text>
<Text>85점</Text>
```

- 이게 전부 children 이고
-  StatisticsCard에서는 그걸 그냥 받아서 보여주기만 해


### 2️⃣ 왜 ReactNode를 쓰는 거야?
**`ReactNode`는 이런 것들을 전부 포함하는 타입이다**

- `<Text />`
- `<View />`
- 여러 개 JSX
- 조건부 렌더링 결과
- 다른 컴포넌트

즉,
```tsx
children: ReactNode
```
-  “리액트에서 화면에 그릴 수 있는 건 다 들어올 수 있다”
- 그래서 공통 카드 컴포넌트에 딱 적합함


### 3️⃣ 이 컴포넌트의 역할 정리

- 이 컴포넌트는 **“내용을 정하지 않는다”**

**❌ 이건 안 함**
- 텍스트 내용 고정
- 레이아웃 강제

**⭕ 이걸 함**
- 카드 테두리
- 배경색
- 패딩
- 공통 UI 스타일

👉 그래서 월별 / 주별 / 과목별 통계 전부 재사용 가능


###4️⃣ wrapper 와 content를 나눈 이유
```tsx
<View style={styles.wrapper}>
  <View style={styles.content}>
    {children}
  </View>
</View>
```

이 구조의 장점 👇
- 그림자
- 카드 간 간격
- 배경 레이어
- 애니메이션

을 wrapper에만 추가 가능

👉 확장성 진짜 좋음 (팀 프로젝트에서 최고)


### 5️⃣ 실제 사용 예시 (이렇게 쓰면 됨)
```tsx
<StatisticsCard>
  <Text style={{ fontSize: 14 }}>주 평균 집중도</Text>
  <Text style={{ fontSize: 24, fontWeight: 'bold' }}>87%</Text>
</StatisticsCard>
```

또는 
```tsx
<StatisticsCard>
  <WeeklyStatistics />
</StatisticsCard>
```
- 내부 내용이 뭐든 상관 없음
- 카드 틀만 제공하는 컴포넌트