
## 전체 코드
```tsx
import { StyleSheet, Text, View, Pressable } from 'react-native'

interface MonthlyStatisticsProps {
  year: number
  month: number
  onSelectDate: (date: string) => void
}

// 임시 더미 데이터 (나중에 교체해야 됨!)
const mockConcentration: Record<number, number> = {
  1: 85,
  2: 40,
  3: 90,
  4: 70,
  5: 95,
  6: 60,
  7: 80,
  8: 30,
  9: 88,
  10: 76,
}

const getColorByScore = (score?: number) => {
  if (score === undefined) return '#E0E0E0'

  if (score > 70) return '#2B482C'

  if (score > 30) return '#87A066'

  return '#E6C85C'
}

const MonthlyStatistics = ({ year, month, onSelectDate }: MonthlyStatisticsProps) => {

  const daysInMonth = new Date(year, month, 0).getDate()
  const firstDayOfWeek = new Date(year, month - 1, 1).getDay()
  const weekDays = ['일', '월', '화', '수', '목', '금', '토']


  return (
    <View style={styles.container}>

      <View style={styles.calendarContainer}>
        {/* 요일 헤더 */}
        <View style={styles.weekRow}>
          {weekDays.map((day) => (
            <Text key={day} style={styles.weekText}>
              {day}
            </Text>
          ))}
        </View>

        {/* 날짜 그리드 */}
        <View style={styles.grid}>
          {Array.from({ length: firstDayOfWeek + daysInMonth }, (_, index) => {
            // 🔹 앞쪽 빈 칸
            if (index < firstDayOfWeek) {
              return (
                <View key={`empty-${index}`} style={styles.dayCell}>
                  <View style={[styles.dayBox, styles.emptyBox]} />
                </View>
              )
            }

            // 🔹 실제 날짜
            const date = index - firstDayOfWeek + 1
            const score = mockConcentration[date]
            const bgColor = getColorByScore(score)

            return (
              <View key={date} style={styles.dayCell}>
                <Pressable
                  style={[styles.dayBox, { backgroundColor: bgColor }]}

                  onPress={() =>
                    onSelectDate(
                      `${year}-${String(month).padStart(2, '0')}-${String(date).padStart(2, '0')}`
                    )
                  }
                >

                  <Text
                    style={[
                      styles.dayText,
                      score > 70 && styles.highScoreText,]}>
                    {date}
                  </Text>
                </Pressable>
              </View>
            )
          })}
        </View>

        {/* 범례 */}
        <View style={styles.legend}>
          <Text style={styles.legendText}>낮음</Text>

          <View
            style={[
              styles.legendColor,
              { backgroundColor: '#E6C85C' },
            ]}
          />
          <View
            style={[
              styles.legendColor,
              { backgroundColor: '#9DB27C' },
            ]}
          />
          <View
            style={[
              styles.legendColor,
              { backgroundColor: '#4F6F3A' },
            ]}
          />

          <Text style={styles.legendText}>높음</Text>
        </View>
      </View>

    </View>
  )
}

export default MonthlyStatistics

const styles = StyleSheet.create({
  container: {
    marginTop: 8,
  },

  calendarContainer: {
    borderWidth: 2,
    borderColor: '#3A2E1F',
    borderRadius: 16,
    padding: 16,
    backgroundColor: '#F7F3E6',
    marginTop: 12,
  },

  weekRow: {
    flexDirection: 'row',
  },

  weekText: {
    width: '14.28%',
    textAlign: 'center',
    fontWeight: '600',
  },

  grid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    paddingHorizontal: 8,
  },

  dayCell: {
    flexBasis: '14.28%',
    paddingHorizontal: 6,
    marginVertical: 8,
  },

  dayBox: {
    width: '100%',
    aspectRatio: 1,
    borderRadius: 12,
    justifyContent: 'center',
    alignItems: 'center',
  },

  emptyBox: {
    backgroundColor: 'transparent',
  },

  dayText: {
    fontWeight: '700',
    color: '#1F2A1F',
  },

  highScoreText: {
    color: '#FFFFFF',
  },

  legend: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 6,
    marginTop: 12,
  },

  legendColor: {
    width: 60,
    height: 10,
    borderRadius: 5,
  },

  legendText: {
    fontSize: 15,
    fontWeight: 600,
    color: '#555',
  },
})
```


---


## 코드 주석
```tsx
import { StyleSheet, Text, View, Pressable } from 'react-native'

/**
 * 📌 MonthlyStatistics 컴포넌트가 받을 props 타입
 * - year: 선택된 연도
 * - month: 선택된 월
 * - onSelectDate: 날짜를 눌렀을 때 실행할 함수
 */
interface MonthlyStatisticsProps {
  year: number
  month: number
  onSelectDate: (date: string) => void
}

/**
 * 📌 임시 더미 데이터
 * key   : 날짜 (1일, 2일, ...)
 * value : 집중도 점수 (0 ~ 100)
 *
 * 👉 실제 API 붙이면 이 객체는 없어질 예정
 */
const mockConcentration: Record<number, number> = {
  1: 85,
  2: 40,
  3: 90,
  4: 70,
  5: 95,
  6: 60,
  7: 80,
  8: 30,
  9: 88,
  10: 76,
}

/**
 * 📌 점수에 따라 배경색을 결정하는 함수
 * - score가 없으면(데이터 없음) → 회색
 * - 70 초과 → 진한 초록
 * - 30 초과 → 연한 초록
 * - 그 외 → 노랑
 */
const getColorByScore = (score?: number) => {
  if (score === undefined) return '#E0E0E0'
  if (score > 70) return '#2B482C'
  if (score > 30) return '#87A066'
  return '#E6C85C'
}

/**
 * 📌 월별 통계 달력 컴포넌트
 */
const MonthlyStatistics = ({ year, month, onSelectDate }: MonthlyStatisticsProps) => {

  /**
   * 📅 해당 월의 총 일수
   * 예) 2025년 11월 → 30
   */
  const daysInMonth = new Date(year, month, 0).getDate()

  /**
   * 📅 해당 월 1일이 무슨 요일인지
   * 0: 일요일 ~ 6: 토요일
   */
  const firstDayOfWeek = new Date(year, month - 1, 1).getDay()

  /** 요일 텍스트 배열 */
  const weekDays = ['일', '월', '화', '수', '목', '금', '토']

  return (
    <View style={styles.container}>

      {/* 📦 달력 전체를 감싸는 카드 영역 */}
      <View style={styles.calendarContainer}>

        {/* 🗓 요일 헤더 */}
        <View style={styles.weekRow}>
          {weekDays.map((day) => (
            <Text key={day} style={styles.weekText}>
              {day}
            </Text>
          ))}
        </View>

        {/* 📅 날짜 그리드 */}
        <View style={styles.grid}>
          {Array.from({ length: firstDayOfWeek + daysInMonth }, (_, index) => {

            /**
             * 🔹 1일 이전의 빈 칸 처리
             * 예) 1일이 수요일이면 일/월/화는 빈 칸
             */
            if (index < firstDayOfWeek) {
              return (
                <View key={`empty-${index}`} style={styles.dayCell}>
                  <View style={[styles.dayBox, styles.emptyBox]} />
                </View>
              )
            }

            /**
             * 🔹 실제 날짜 계산
             * index - firstDayOfWeek + 1
             */
            const date = index - firstDayOfWeek + 1

            /** 해당 날짜의 집중도 점수 */
            const score = mockConcentration[date]

            /** 점수에 따른 배경색 */
            const bgColor = getColorByScore(score)

            return (
              <View key={date} style={styles.dayCell}>
                <Pressable
                  style={[styles.dayBox, { backgroundColor: bgColor }]}
                  onPress={() =>
                    onSelectDate(
                      `${year}-${String(month).padStart(2, '0')}-${String(date).padStart(2, '0')}`
                    )
                  }
                >
                  {/* 날짜 텍스트 */}
                  <Text
                    style={[
                      styles.dayText,
                      score > 70 && styles.highScoreText,
                    ]}
                  >
                    {date}
                  </Text>
                </Pressable>
              </View>
            )
          })}
        </View>

        {/* 📊 범례 */}
        <View style={styles.legend}>
          <Text style={styles.legendText}>낮음</Text>

          <View style={[styles.legendColor, { backgroundColor: '#E6C85C' }]} />
          <View style={[styles.legendColor, { backgroundColor: '#9DB27C' }]} />
          <View style={[styles.legendColor, { backgroundColor: '#4F6F3A' }]} />

          <Text style={styles.legendText}>높음</Text>
        </View>
      </View>
    </View>
  )
}

export default MonthlyStatistics
```


---


## 컴포넌트 구조 설명
### 🧠 전체 역할

**“한 달짜리 달력을 그리고, 날짜별 집중도를 색으로 보여주는 컴포넌트”**


### 1️⃣ 날짜 계산 로직 (핵심)
```ts
daysInMonth       // 이 달이 며칠까지 있는지
firstDayOfWeek    // 1일이 무슨 요일인지
```
- 이 두 개 덕분에
  - 달력 앞에 빈 칸이 자동으로 생기고
  - 달마다 시작 요일이 달라져도 깨지지 않음


### 2️⃣ grid + flexWrap 구조
```ts
grid: {
  flexDirection: 'row',
  flexWrap: 'wrap',
}
```
- 가로 7칸
- 줄 자동 개행
- 태블릿 / 해상도 바뀌어도 안전

👉 태블릿 가로에 최적화된 달력 구조


### 3️⃣ dayCell / dayBox 분리 이유
```ts
dayCell  // 간격, 위치 담당
dayBox   // 실제 색깔 박스
```
- 이렇게 나눴기 때문에:
  - 좌우 여백 조절 쉬움
  - 박스 크기 균일
  - 디자인 수정 편함

👉 UI 설계 제대로 한 구조야 👍


### 4️⃣ 색상 + 글자색 분기
```ts
score > 70 && styles.highScoreText
```
- 진한 초록일 때만 흰 글자
- 회색 / 연한 색은 검정 글자 유지

👉 가독성 최고


### 5️⃣ onSelectDate 책임 분리
```ts
onSelectDate(...)
```
- 이 컴포넌트는 **“보여주기만”**
- 실제 이동 / 모달 / API는 **부모가 담당**

👉 유지보수 + 팀플에 완벽한 구조
