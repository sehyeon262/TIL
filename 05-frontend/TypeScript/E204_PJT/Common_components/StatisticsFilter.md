## `StatisticsFilter.tsx` 란?
**월별/ 주별에서 쓰는 "필터 영역"**


---


## 전체 코드
```tsx
import { StyleSheet, Text, View, Pressable } from 'react-native'

interface StatisticsFilterProps {
  year: number
  month: number
  onPressYear?: () => void
  onPressMonth?: () => void
}

const StatisticsFilter = ({
  year,
  month,
  onPressYear,
  onPressMonth,
}: StatisticsFilterProps) => {
  return (
    <View style={styles.container}>
      <Pressable style={styles.box} onPress={onPressYear}>
        <Text style={styles.text}>{year}년</Text>
      </Pressable>

      <Pressable style={styles.box} onPress={onPressMonth}>
        <Text style={styles.text}>{month}월</Text>
      </Pressable>
    </View>
  )
}

export default StatisticsFilter

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    gap: 12,
    marginVertical: 16,
  },
  box: {
    paddingVertical: 8,
    paddingHorizontal: 16,
    borderRadius: 12,
    backgroundColor: '#E8DFC1',
  },
  text: {
    fontSize: 16,
    fontWeight: '600',
  },
})
```

---

## 코드 분석
```tsx
/*
StatisticsFilter 컴포넌트가 받을 props의 타입 정의

📌 interface란?
- "이 컴포넌트는 이런 데이터들을 받아야 해!" 라고 약속하는 설계도
- TypeScript에서 props 구조를 미리 정해주는 역할

📌 이 컴포넌트가 받는 값들:
- year: 숫자 (ex: 2026)
- month: 숫자 (ex: 1)
- onPressYear: 연도 버튼 눌렀을 때 실행할 함수 (선택)
- onPressMonth: 월 버튼 눌렀을 때 실행할 함수 (선택)
*/
interface StatisticsFilterProps {
  year: number              // 필터에 표시할 연도
  month: number             // 필터에 표시할 월
  onPressYear?: () => void  // 연도 버튼 클릭 시 실행 (있어도 되고 없어도 됨)
  onPressMonth?: () => void // 월 버튼 클릭 시 실행 (있어도 되고 없어도 됨)
}
```

---

```tsx
/*
StatisticsFilter 컴포넌트 정의

📌 구조 분해 할당
- props.year → year
- props.month → month
- props.onPressYear → onPressYear
- props.onPressMonth → onPressMonth
*/
const StatisticsFilter = ({
  year,
  month,
  onPressYear,
  onPressMonth,
}: StatisticsFilterProps) => {

  return (
    /*
    전체 필터 영역
    - 가로(row)로 연/월 버튼을 나란히 배치
    */
    <View style={styles.container}>

      {/*
      연도 버튼
      - Pressable: 클릭 가능한 영역
      - onPressYear가 있으면 눌렀을 때 실행
      */}
      <Pressable style={styles.box} onPress={onPressYear}>
        <Text style={styles.text}>
          {year}년
        </Text>
      </Pressable>

      {/*
      월 버튼
      - onPressMonth가 있으면 눌렀을 때 실행
      */}
      <Pressable style={styles.box} onPress={onPressMonth}>
        <Text style={styles.text}>
          {month}월
        </Text>
      </Pressable>

    </View>
  )
}

// 다른 파일에서 import 해서 쓸 수 있도록 export
export default StatisticsFilter
```

---

```tsx
/*
스타일 정의 영역
📌 StyleSheet.create를 쓰는 이유
- 성능 최적화
- 스타일 자동 타입 체크
*/
const styles = StyleSheet.create({

  // 연도 / 월 버튼을 감싸는 컨테이너
  container: {
    flexDirection: 'row', // 가로 방향 정렬
    gap: 12,              // 버튼 사이 간격
    marginVertical: 16,   // 위아래 여백
  },

  // 연도 / 월 버튼 공통 스타일
  box: {
    paddingVertical: 8,    // 위아래 패딩
    paddingHorizontal: 16, // 좌우 패딩
    borderRadius: 12,      // 둥근 모서리
    backgroundColor: '#E8DFC1',
  },

  // 버튼 안 텍스트 스타일
  text: {
    fontSize: 16,
    fontWeight: '600',
  },
})
```