## `StatisticsSummary.tsx` 란?
**하단 요약 바 (공통 UI, 내용만 다름)**


---


## 전체 코드
```tsx
import { StyleSheet, Text, View } from 'react-native'

interface SummaryItem {
  label: string
  value: string
}

interface StatisticsSummaryProps {
  left: SummaryItem
  right: SummaryItem
}

const StatisticsSummary = ({ left, right }: StatisticsSummaryProps) => {
  return (
    <View style={styles.container}>
      <View style={styles.box}>
        <Text style={styles.label}>{left.label}</Text>
        <Text style={styles.value}>{left.value}</Text>
      </View>

      <View style={styles.box}>
        <Text style={styles.label}>{right.label}</Text>
        <Text style={styles.value}>{right.value}</Text>
      </View>
    </View>
  )
}

export default StatisticsSummary

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    gap: 16,
    marginTop: 24,
  },
  box: {
    flex: 1,
    paddingVertical: 16,
    borderRadius: 16,
    backgroundColor: '#F6F3DC',
    alignItems: 'center',
  },
  label: {
    fontSize: 14,
    color: '#555',
  },
  value: {
    fontSize: 20,
    fontWeight: '700',
    marginTop: 6,
  },
})
```


---


## 코드 분석
```tsx
/**
 * SummaryItem 인터페이스
 * - 하나의 요약 박스에 들어갈 데이터 구조
 * - label : 항목 이름 (예: "평균 집중 시간")
 * - value : 값 (예: "32분")
 */
interface SummaryItem {
  label: string
  value: string
}
```

---

```tsx
/**
 * StatisticsSummary 컴포넌트가 받을 props 타입
 * - left  : 왼쪽 요약 박스 데이터
 * - right : 오른쪽 요약 박스 데이터
 */
interface StatisticsSummaryProps {
  left: SummaryItem
  right: SummaryItem
}
```

---

```tsx
/**
 * 통계 요약 컴포넌트
 * - 좌 / 우 두 개의 요약 박스를 가로로 보여줌
 */
const StatisticsSummary = ({ left, right }: StatisticsSummaryProps) => {
  return (
    // 전체 컨테이너 (가로 정렬)
    <View style={styles.container}>

      {/* 왼쪽 요약 박스 */}
      <View style={styles.box}>
        {/* 항목 이름 */}
        <Text style={styles.label}>{left.label}</Text>
        {/* 항목 값 */}
        <Text style={styles.value}>{left.value}</Text>
      </View>

      {/* 오른쪽 요약 박스 */}
      <View style={styles.box}>
        <Text style={styles.label}>{right.label}</Text>
        <Text style={styles.value}>{right.value}</Text>
      </View>

    </View>
  )
}

// 다른 파일에서 사용할 수 있도록 export
export default StatisticsSummary
```

---

```tsx
const styles = StyleSheet.create({
  // 두 박스를 감싸는 부모 컨테이너
  container: {
    flexDirection: 'row', // 자식 요소들을 가로로 배치
    gap: 16,              // 박스 사이 간격
    marginTop: 24,        // 위쪽 여백
  },

  // 각각의 요약 박스
  box: {
    flex: 1,              // 좌우 박스 너비를 동일하게
    paddingVertical: 16,  // 위아래 내부 여백
    borderRadius: 16,     // 둥근 모서리
    backgroundColor: '#F6F3DC', // 배경색
    alignItems: 'center', // 텍스트를 가로 중앙 정렬
  },

  // 항목 이름 텍스트
  label: {
    fontSize: 14,
    color: '#555',        // 연한 회색
  },

  // 값 텍스트
  value: {
    fontSize: 20,
    fontWeight: '700',    // 굵은 글씨
    marginTop: 6,         // label과의 간격
  },
})
```


---


## 코드 자세한 설명
### ✅ 이 컴포넌트가 하는 역할 (한 줄 요약)

-  “좌우 2개의 통계 요약 박스를 공통 컴포넌트로 만든 것”


### ✅ interface 설명 (진짜 중요)
#### 1️⃣ SummaryItem
```ts
interface SummaryItem {
  label: string
  value: string
}
```

👉 “요약 박스 하나의 설계도”

- 예)
```ts
{
  label: "평균 집중 시간",
  value: "32분"
}
```
- 이 구조 무조건 지켜야 함
- ❌ 숫자, ❌ 빠진 값 → 에러


#### 2️⃣ StatisticsSummaryProps
```ts
interface StatisticsSummaryProps {
  left: SummaryItem
  right: SummaryItem
}
```

👉 이 컴포넌트는 props로 2개를 반드시 받는다
- `left` 👉 왼쪽 박스 데이터
- `right` 👉 오른쪽 박스 데이터
- 둘 다 `SummaryItem` 형태여야 함


### ✅ props 구조 분해 설명
```ts
const StatisticsSummary = ({ left, right }: StatisticsSummaryProps)
```

- 이건 사실 아래랑 같다 👇
```ts
const StatisticsSummary = (props: StatisticsSummaryProps) => {
  const left = props.left
  const right = props.right
}
```
-  그냥 짧게 쓴 문법일 뿐
-  리액트에서 제일 많이 쓰는 패턴


### ✅ 실제 사용 예시 (이렇게 씀!)
```tsx
<StatisticsSummary
  left={{ label: '평균 집중 시간', value: '32분' }}
  right={{ label: '집중 성공 횟수', value: '12회' }}
/>
```
-  이 구조가 틀리면 TypeScript가 바로 잡아줌