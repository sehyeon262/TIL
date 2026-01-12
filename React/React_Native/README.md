## React Navtive란?
- React Native란 메타에서 만든 오픈소스 모바일 애플리케이션 프레임워크이다. 
- JavaScript(TS)로 개발이 가능하며 IOS와 Android 모바일 앱을 동시에 개발할 수 있는 크로스 플랫폼이다.


## React vs React Native
| 구분  | React              | React Native              |
| --- | ------------------ | ------------------------- |
| 목적  | **웹(Web)** UI 개발   | **모바일 앱(iOS/Android)** 개발 |
| 결과물 | HTML/CSS/JS → 브라우저 | 네이티브 앱 → 앱스토어             |
| 핵심  | 웹 프론트엔드            | 모바일 앱 프론트엔드               |


## 공통점
- 컴포넌트 기반
- 선언형 UI
- Virtual DOM 개념
- State / Props
- Hooks (`useState`, `useEffect` 등)

``` jsx
function Counter() {
  const [count, setCount] = useState(0);
  return <Text>{count}</Text>;
}
```


## 가장 큰 차이점
### 🧠 React (웹)
```CSS
JSX → React → Virtual DOM → HTML/CSS → 브라우저
```

- `<div>`, `<span>`, `<button>` 사용
- 브라우저가 화면을 그림
- CSS로 스타일링

### 📱 React Native (모바일)
```CSS
JSX → React Native → Native UI → iOS / Android
```
- `<View>`, `<Text>`, `<TouchableOpacity>`
- 실제 네이티브 컴포넌트 사용
- 브라우저 ❌