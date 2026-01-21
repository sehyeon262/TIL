## 📌 목차
- [Layout](#layout)
- [Position (위치)](#position-위치)
- [Size (크기)](#size-크기)
- [Spacing (여백)](#spacing-여백)
  - [Margin](#margin)
  - [Padding](#padding)
- [Border (테두리)](#border-테두리)
- [Background / Opacity](#background--opacity)
- [Text 전용 (TextStyle)](#text-전용-textstyle)
- [Shadow (그림자)](#shadow-그림자)
  - [iOS](#ios)
  - [Android](#android)
- [Image 전용 (ImageStyle)](#image-전용-imagestyle)
- [Overflow / Display](#overflow--display)
- [Transform](#transform)



## 📱 React Native Style 속성 총정리 (TypeScript 기준)
**`StyleSheet.create({})` 안에서 사용하는 것들** 
- 웹 CSS랑 다르고 일부만 비슷



## Layout
| 속성               | 설명       | 가능한 값                                                                                           |
| ---------------- | -------- | ----------------------------------------------------------------------------------------------- |
| `flex`           | 남은 공간 비율 | `number`                                                                                        |
| `flexDirection`  | 주축 방향    | `"row"`, `"column"`, `"row-reverse"`, `"column-reverse"`                                        |
| `justifyContent` | 주축 정렬    | `"flex-start"`, `"flex-end"`, `"center"`, `"space-between"`, `"space-around"`, `"space-evenly"` |
| `alignItems`     | 교차축 정렬   | `"flex-start"`, `"flex-end"`, `"center"`, `"stretch"`, `"baseline"`                             |
| `alignSelf`      | 자기 자신 정렬 | `"auto"`, `"flex-start"`, `"flex-end"`, `"center"`, `"stretch"`, `"baseline"`                   |
| `flexWrap`       | 줄바꿈      | `"nowrap"`, `"wrap"`, `"wrap-reverse"`                                                          |
| `gap`            | 아이템 간격   | `number`                                                                                        |


## Position (위치)
| 속성         | 설명     | 가능한 값                      |
| ---------- | ------ | -------------------------- |
| `position` | 위치 기준  | `"relative"`, `"absolute"` |
| `top`      | 위쪽 거리  | `number`                   |
| `bottom`   | 아래쪽 거리 | `number`                   |
| `left`     | 왼쪽 거리  | `number`                   |
| `right`    | 오른쪽 거리 | `number`                   |
| `zIndex`   | 쌓임 순서  | `number`                   |


## Size (크기)
| 속성          | 설명    | 가능한 값                     |
| ----------- | ----- | ------------------------- |
| `width`     | 너비    | `number`, `"auto"`, `"%"` |
| `height`    | 높이    | `number`, `"auto"`, `"%"` |
| `minWidth`  | 최소 너비 | `number`                  |
| `maxWidth`  | 최대 너비 | `number`                  |
| `minHeight` | 최소 높이 | `number`                  |
| `maxHeight` | 최대 높이 | `number`                  |


## Spacing (여백)

### Margin
| 속성                 | 설명       | 값        |
| ------------------ | -------- | -------- |
| `margin`           | 전체 바깥 여백 | `number` |
| `marginTop`        | 위 여백     | `number` |
| `marginBottom`     | 아래 여백    | `number` |
| `marginLeft`       | 왼쪽 여백    | `number` |
| `marginRight`      | 오른쪽 여백   | `number` |
| `marginVertical`   | 상하 여백    | `number` |
| `marginHorizontal` | 좌우 여백    | `number` |


### Padding
| 속성                  | 설명        | 값        |
| ------------------- | --------- | -------- |
| `padding`           | 전체 안쪽 여백  | `number` |
| `paddingTop`        | 위 안쪽 여백   | `number` |
| `paddingBottom`     | 아래 안쪽 여백  | `number` |
| `paddingLeft`       | 왼쪽 안쪽 여백  | `number` |
| `paddingRight`      | 오른쪽 안쪽 여백 | `number` |
| `paddingVertical`   | 상하 안쪽 여백  | `number` |
| `paddingHorizontal` | 좌우 안쪽 여백  | `number` |


## Border (테두리)
| 속성                        | 설명      | 가능한 값    |
| ------------------------- | ------- | -------- |
| `borderWidth`             | 테두리 두께  | `number` |
| `borderColor`             | 테두리 색   | `string` |
| `borderRadius`            | 둥글기     | `number` |
| `borderTopLeftRadius`     | 좌상단 둥글기 | `number` |
| `borderTopRightRadius`    | 우상단 둥글기 | `number` |
| `borderBottomLeftRadius`  | 좌하단 둥글기 | `number` |
| `borderBottomRightRadius` | 우하단 둥글기 | `number` |


## Background / Opacity
| 속성                | 설명  | 가능한 값                                              |
| ----------------- | --- | -------------------------------------------------- |
| `backgroundColor` | 배경색 | `"#FFF"`, `"#FFFFFF"`, `"rgba()"`, `"transparent"` |
| `opacity`         | 투명도 | `0 ~ 1`                                            |


## Text 전용 (TextStyle)
| 속성              | 설명     | 가능한 값                                                  |
| --------------- | ------ | ------------------------------------------------------ |
| `color`         | 글자 색   | `string`                                               |
| `fontSize`      | 글자 크기  | `number`                                               |
| `fontWeight`    | 글자 굵기  | `"normal"`, `"bold"`, `"100" ~ "900"`                  |
| `fontStyle`     | 글자 스타일 | `"normal"`, `"italic"`                                 |
| `textAlign`     | 글자 정렬  | `"auto"`, `"left"`, `"right"`, `"center"`, `"justify"` |
| `lineHeight`    | 줄 간격   | `number`                                               |
| `letterSpacing` | 자간     | `number`                                               |


## Shadow (그림자)
### iOS
| 속성              | 설명      | 값                                   |
| --------------- | ------- | ----------------------------------- |
| `shadowColor`   | 그림자 색   | `string`                            |
| `shadowOffset`  | 그림자 위치  | `{ width: number; height: number }` |
| `shadowOpacity` | 그림자 투명도 | `0 ~ 1`                             |
| `shadowRadius`  | 퍼짐 정도   | `number`                            |


### Android
| 속성          | 설명     | 값        |
| ----------- | ------ | -------- |
| `elevation` | 그림자 깊이 | `number` |


## Image 전용 (ImageStyle)
| 속성             | 설명     | 가능한 값                                                       |
| -------------- | ------ | ----------------------------------------------------------- |
| `resizeMode`   | 이미지 맞춤 | `"cover"`, `"contain"`, `"stretch"`, `"repeat"`, `"center"` |
| `tintColor`    | 색상 덮기  | `string`                                                    |
| `borderRadius` | 둥글기    | `number`                                                    |


## Overflow / Display
| 속성         | 설명    | 가능한 값                               |
| ---------- | ----- | ----------------------------------- |
| `overflow` | 넘침 처리 | `"visible"`, `"hidden"`, `"scroll"` |
| `display`  | 표시 여부 | `"flex"`, `"none"`                  |


## Transform 
| 속성          | 설명 | 가능한 값                                                                                          |
| ----------- | -- | ---------------------------------------------------------------------------------------------- |
| `transform` | 변형 | `{ scale }`, `{ translateX }`, `{ translateY }`, `{ rotate: "deg" }`, `{ skewX }`, `{ skewY }` |
