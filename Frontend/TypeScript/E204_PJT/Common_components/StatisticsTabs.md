## 전체 코드
```tsx
import { StyleSheet, Text, View, Pressable } from 'react-native'

type ViewType = 'monthly' | 'weekly' | 'subject'

interface StatisticsTabsProps {
  value: ViewType
  onChange: (value: ViewType) => void
}

const StatisticsTabs = ({ value, onChange }: StatisticsTabsProps) => {
  const tabs: { label: string; key: ViewType }[] = [
    { label: '월별 보기', key: 'monthly' },
    { label: '주별 보기', key: 'weekly' },
    { label: '과목별 보기', key: 'subject' },
  ]

  return (
    <View style={styles.container}>
      {tabs.map((tab) => (
        <Pressable
          key={tab.key}
          style={[
            styles.tab,
            value === tab.key && styles.activeTab,
          ]}
          onPress={() => onChange(tab.key)}
        >
          <Text
            style={[
              styles.text,
              value === tab.key && styles.activeText,
            ]}
          >
            {tab.label}
          </Text>
        </Pressable>
      ))}
    </View>
  )
}

export default StatisticsTabs

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    marginTop: 16,
  },
  tab: {
    flex: 1,
    paddingVertical: 12,
    backgroundColor: '#D8CFAF',
    alignItems: 'center',
    borderTopLeftRadius: 12,
    borderTopRightRadius: 12,
    marginHorizontal: 4,
  },
  activeTab: {
    backgroundColor: '#6B4E2E',
  },
  text: {
    fontSize: 16,
    fontWeight: '600',
    color: '#3A2A1A',
  },
  activeText: {
    color: '#FFFFFF',
  },
})
```


---


## 코드 분석
```tsx
type ViewType = 'monthly' | 'weekly' | 'subject'
```

 **📌 ViewType** 
 * 통계 화면에서 어떤 "보기 모드"인지 구분하기 위한 타입
    - monthly : 월별 통계
    - weekly  : 주별 통계
    - subject : 과목별 통계
 
 * 문자열을 그냥 쓰지 않고 타입으로 제한하면
  
   - 오타 방지
   - 자동완성 지원
   - 유지보수 쉬워짐

---

```tsx
/**
 * 📌 StatisticsTabs 컴포넌트가 받을 props 타입 정의
 */
interface StatisticsTabsProps {
  /**
   * 현재 선택된 탭 상태
   * - 부모 컴포넌트에서 관리하는 state 값
   */
  value: ViewType

  /**
   * 탭을 눌렀을 때 실행되는 함수
   * - 어떤 탭을 눌렀는지 value 값으로 부모에게 알려줌
   */
  onChange: (value: ViewType) => void
}
```

---

```tsx
/**
 * 📌 통계 탭 컴포넌트
 * - 월별 / 주별 / 과목별 보기 전환용
 */
const StatisticsTabs = ({ value, onChange }: StatisticsTabsProps) => {

  /**
   * 📌 탭 정보 배열
   * - label : 화면에 보여줄 텍스트
   * - key   : 실제 상태 값 (ViewType)
   * 
   * 이렇게 배열로 관리하면
   * 👉 map으로 반복 렌더링 가능
   * 👉 탭 추가/삭제가 쉬워짐
   */
  const tabs: { label: string; key: ViewType }[] = [
    { label: '월별 보기', key: 'monthly' },
    { label: '주별 보기', key: 'weekly' },
    { label: '과목별 보기', key: 'subject' },
  ]
```

---

```tsx
  return (
    // 탭들을 가로로 배치하는 컨테이너
    <View style={styles.container}>
      {tabs.map((tab) => (
        <Pressable
          key={tab.key} // map 사용 시 반드시 필요한 고유 key
          style={[
            styles.tab,                  // 기본 탭 스타일
            value === tab.key && styles.activeTab, // 선택된 탭이면 활성화 스타일
          ]}
          // 탭을 누르면 부모 컴포넌트의 상태 변경
          onPress={() => onChange(tab.key)}
        >

          <Text
            style={[
              styles.text,                    // 기본 텍스트 스타일
              value === tab.key && styles.activeText, // 선택된 탭이면 글자색 변경
            ]}
          >
            {tab.label}
          </Text>
        </Pressable>
      ))}
    </View>
  )
}

export default StatisticsTabs
```

---

```tsx
const styles = StyleSheet.create({
  // 탭 전체 컨테이너
  container: {
    flexDirection: 'row', // 탭을 가로 방향으로 나열
    marginTop: 16,
  },

  // 기본 탭 스타일
  tab: {
    flex: 1,                  // 탭을 동일한 너비로 분배
    paddingVertical: 12,      // 위아래 여백
    backgroundColor: '#D8CFAF',
    alignItems: 'center',     // 텍스트 가로 중앙 정렬
    borderTopLeftRadius: 12,  // 상단 왼쪽 둥글게
    borderTopRightRadius: 12, // 상단 오른쪽 둥글게
    marginHorizontal: 4,      // 탭 사이 간격
  },

  // 선택된 탭 스타일
  activeTab: {
    backgroundColor: '#6B4E2E',
  },

  // 기본 텍스트 스타일
  text: {
    fontSize: 16,
    fontWeight: '600',
    color: '#3A2A1A',
  },

  // 선택된 탭 텍스트 스타일
  activeText: {
    color: '#FFFFFF',
  },
})
```

