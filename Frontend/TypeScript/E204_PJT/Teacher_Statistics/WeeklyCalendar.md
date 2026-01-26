## 이 코드가 하는 일
- 모달로 뜨는 달력
- 월 이동 가능
- 날짜 하나 선택 후
- Apply 누르면 선택한 날짜를 부모에게 전달


---


## 전체 코드
```tsx
import { StyleSheet, Text, View, Pressable, Modal } from 'react-native'
import { useState } from 'react'

interface WeeklyCalendarProps {
  visible: boolean
  onClose: () => void
  onSelectDate: (date: Date) => void
}

const WEEK_DAYS = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']

const WeeklyCalendar = ({
  visible,
  onClose,
  onSelectDate,
}: WeeklyCalendarProps) => {


  const [currentDate, setCurrentDate] = useState(new Date())

  const [selectedDate, setSelectedDate] = useState<Date | null>(null)

  const createCalendarDates = () => {
    const year = currentDate.getFullYear()
    const month = currentDate.getMonth()

    const firstDay = new Date(year, month, 1)
    const lastDay = new Date(year, month + 1, 0)

    const startPadding = firstDay.getDay()
    const totalDays = lastDay.getDate()

    const dates: (Date | null)[] = []

    for (let i = 0; i < startPadding; i++) {
      dates.push(null)
    }

    for (let d = 1; d <= totalDays; d++) {
      dates.push(new Date(year, month, d))
    }

    return dates
  }

  const dates = createCalendarDates()

  /** 월 이동 */
  const changeMonth = (offset: number) => {
    const next = new Date(currentDate)
    next.setMonth(currentDate.getMonth() + offset)
    setCurrentDate(next)
    setSelectedDate(null)
  }

  return (
    <Modal visible={visible} transparent animationType="fade">
      <View style={styles.overlay}>
        <View style={styles.modal}>

          {/* 헤더 (월 이동) */}
          <View style={styles.header}>
            <Pressable onPress={() => changeMonth(-1)}>
              <Text style={styles.arrow}>{'<'}</Text>
            </Pressable>

            <Text style={styles.monthText}>
              {currentDate.getMonth() + 1}월 {currentDate.getFullYear()}
            </Text>

            <Pressable onPress={() => changeMonth(1)}>
              <Text style={styles.arrow}>{'>'}</Text>
            </Pressable>
          </View>

          {/* 요일 */}
          <View style={styles.weekRow}>
            {WEEK_DAYS.map((day) => (
              <Text key={day} style={styles.weekText}>
                {day}
              </Text>
            ))}
          </View>

          {/* 날짜 */}
          <View style={styles.grid}>
            {dates.map((date, index) =>
              date ? (
                <Pressable
                  key={index}
                  onPress={() => setSelectedDate(date)}
                  style={[
                    styles.dayBox,
                    selectedDate?.toDateString() === date.toDateString() &&
                      styles.selectedDay,
                  ]}
                >
                  <Text>{date.getDate()}</Text>
                </Pressable>
              ) : (
                <View key={index} style={styles.emptyBox} />
              )
            )}
          </View>

          {/* 버튼 영역 */}
          <View style={styles.footer}>
            <Pressable onPress={onClose} style={styles.cancelBtn}>
              <Text>Cancel</Text>
            </Pressable>

            <Pressable
              disabled={!selectedDate}
              onPress={() => {
                if (selectedDate) {
                  onSelectDate(selectedDate)
                }
              }}
              style={[
                styles.applyBtn,
                !selectedDate && styles.disabledBtn,
              ]}
            >
              <Text style={styles.applyText}>Apply</Text>
            </Pressable>
          </View>

        </View>
      </View>
    </Modal>
  )
}

export default WeeklyCalendar

const styles = StyleSheet.create({
  overlay: {
    flex: 1,
    backgroundColor: 'rgba(0,0,0,0.4)',
    justifyContent: 'center',
    alignItems: 'center',
  },

  modal: {
    width: 320,
    backgroundColor: '#FFF',
    borderRadius: 16,
    padding: 16,
  },

  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 12,
  },

  arrow: {
    fontSize: 18,
    fontWeight: '700',
  },

  monthText: {
    fontWeight: '700',
  },

  weekRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },

  weekText: {
    width: 40,
    textAlign: 'center',
    fontSize: 12,
    color: '#666',
  },

  grid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    marginTop: 8,
  },

  dayBox: {
    width: 40,
    height: 40,
    margin: 2,
    alignItems: 'center',
    justifyContent: 'center',
    borderRadius: 8,
  },

  selectedDay: {
    backgroundColor: '#4C6EF5',
  },
  
  emptyBox: {
    width: 40,
    height: 40,
    margin: 2,
  },

  footer: {
    flexDirection: 'row',
    justifyContent: 'flex-end',
    marginTop: 16,
    gap: 12,
  },

  cancelBtn: {
    paddingHorizontal: 12,
    paddingVertical: 8,
  },

  applyBtn: {
    paddingHorizontal: 16,
    paddingVertical: 8,
    backgroundColor: '#4C6EF5',
    borderRadius: 8,
  },

  applyText: {
    color: '#FFF',
    fontWeight: '600',
  },
  
  disabledBtn: {
    opacity: 0.4,
  },
})
```


---


## 코드에 주석 달기
### 🔹 import & interface
```ts
import { StyleSheet, Text, View, Pressable, Modal } from 'react-native'
import { useState } from 'react'
```
- `Modal` : 화면 위에 띄우는 팝업
- `Pressable` : 클릭 가능한 버튼


```ts
interface WeeklyCalendarProps {
  visible: boolean
  onClose: () => void
  onSelectDate: (date: Date) => void
}
```
**📌 props 설명 (아주 중요!)**
| 이름             | 역할                            |
| -------------- | ----------------------------- |
| `visible`      | 모달을 열지 말지 결정                  |
| `onClose`      | Cancel 눌렀을 때 실행               |
| `onSelectDate` | 날짜 선택 후 Apply 눌렀을 때 부모로 날짜 전달 |

- 이 컴포넌트는 날짜만 고르고, 실제 처리는 부모가 함


### 🔹 컴포넌트 시작
```ts
const WeeklyCalendar = ({
  visible,
  onClose,
  onSelectDate,
}: WeeklyCalendarProps) => {
```
- props 구조 분해
- `WeeklyCalendarProps` 타입 적용


### 🔹 상태(state) 설명
#### ✔ 기본 전체 구조
```ts
const [
  상태값,
  상태를바꾸는함수
] = useState<상태의타입>(초기값)
```


**✔ 현재 보고 있는 달(month) 기준 날짜**
```ts
const [currentDate, setCurrentDate] = useState(new Date())
```
- 처음엔 오늘 날짜
- `<`, `>` 누르면 여기 값이 바뀜


**✔ 사용자가 클릭한 날짜**
```ts
const [selectedDate, setSelectedDate] = useState<Date | null>(null)
```
- 처음엔 아무것도 선택 안 됨 → `null`
- 날짜 누르면 `Date` 객체 저장


### 🔹 달력 날짜 만드는 함수
```ts
const createCalendarDates = () => {
```
- 이번 달 달력을 만들기 위한 로직

```ts
const year = currentDate.getFullYear()
const month = currentDate.getMonth()
```
- 현재 보고 있는 연 / 월
- `getMonth()`는 0부터 시작 (0 = 1월)

```ts
const firstDay = new Date(year, month, 1)
const lastDay = new Date(year, month + 1, 0)
```
| 코드             | 의미                    |
| -------------- | --------------------- |
| `month, 1`     | 이번 달 1일               |
| `month + 1, 0` | 다음 달의 0일 = 이번 달 마지막 날 |


```ts
const startPadding = firstDay.getDay()
```
- 1일이 무슨 요일인지
- 예: 수요일이면 `3` 
- 그만큼 **빈 칸(null)** 필요


```ts
const totalDays = lastDay.getDate()
```
- 이번 달이 며칠까지 있는지 (28 / 30 / 31)


```ts
const dates: (Date | null)[] = []
```
- 달력에 뿌릴 데이터 배열
- 빈칸은 `null`, 날짜는 `Date`


```ts
for (let i = 0; i < startPadding; i++) {
  dates.push(null)
}
```
- 1일 전까지 빈 칸 채우기


```ts
for (let d = 1; d <= totalDays; d++) {
  dates.push(new Date(year, month, d))
}
```
- 1일 ~ 마지막 날까지 Date 객체 생성


```ts
return dates
```
- 최종 결과: `[null, null, Date(1), Date(2), ...]`



### 🔹 월 이동 함수
```ts
const changeMonth = (offset: number) => {
```
- `-1` → 이전 달
- `+1` → 다음 달

```ts
const next = new Date(currentDate)
next.setMonth(currentDate.getMonth() + offset)
```
- Date 객체는 **복사해서 사용해야 안전**


```ts
setCurrentDate(next)
setSelectedDate(null)
```
- 달 바뀌면 선택 날짜 초기화


### 🔹 JSX 렌더링 구조
#### 1️⃣ Modal
```tsx
<Modal visible={visible} transparent animationType="fade">
```

| 옵션            | 의미       |
| ------------- | -------- |
| `visible`     | 모달 열림/닫힘 |
| `transparent` | 배경 투명    |
| `fade`        | 부드러운 등장  |


#### 2️⃣ 헤더 (월 이동)
```tsx
<Pressable onPress={() => changeMonth(-1)}>
  <Text>{'<'}</Text>
</Pressable>
```
- 이전 달

```tsx
<Text>
  {currentDate.getMonth() + 1}월 {currentDate.getFullYear()}
</Text>
```
- 현재 월 표시

```tsx
<Pressable onPress={() => changeMonth(1)}>
  <Text>{'>'}</Text>
</Pressable>
```
- 다음 달


#### 3️⃣ 요일 표시
```tsx
{WEEK_DAYS.map((day) => (
  <Text key={day}>{day}</Text>
))}
```
- 배열 → 요일 자동 렌더링


####  4️⃣ 날짜 그리드
```tsx
{dates.map((date, index) =>
  date ? (
```
- `date === null` → 빈 칸
- `date 있음` → 날짜 버튼

```tsx
<Pressable
  onPress={() => setSelectedDate(date)}
  style={[
    styles.dayBox,
    selectedDate?.toDateString() === date.toDateString()
      && styles.selectedDay,
  ]}
>
```
**📌 선택된 날짜 스타일 처리 핵심**
- `toDateString()`으로 날짜 비교
- 같으면 파란 배경


#### 5️⃣ 하단 버튼
**Cancel**
```tsx
<Pressable onPress={onClose}>
```
- 그냥 닫기

**Apply**
```tsx
<Pressable
  disabled={!selectedDate}
```
- 날짜 선택 안 하면 비활성화

```tsx
onPress={() => {
  if (selectedDate) {
    onSelectDate(selectedDate)
  }
}}
```
-  부모에게 날짜 전달하는 순간 