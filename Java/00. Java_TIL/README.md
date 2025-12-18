## 📌 Scanner 입력 메서드 핵심 3종 정리
| 메서드          | 자료형      | 입력 예시         | 읽는 범위  | 특징 / 주의점            |
| ------------ | -------- | ------------- | ------ | ------------------- |
| `nextInt()`  | `int`    | `10`          | 숫자만    | 👉 **엔터(`\n`)를 남김** |
| `next()`     | `String` | `hello`       | 공백 전까지 | 👉 한 단어만 읽음         |
| `nextLine()` | `String` | `hello world` | 한 줄 전체 | 👉 공백 포함, 엔터까지 읽음   |

---

## 📌 실제 코드 예시 비교

### 1️⃣ nextInt() 예시
```java
int a = sc.nextInt();
System.out.println(a);
```

- 입력
```
10
```

- 출력
```
10
```

#### ✔ 정수만 입력
#### ❗ 엔터는 처리 안 함

---

### 2️⃣ next() 예시
```java
String s = sc.next();
System.out.println(s);
```

- 입력
```
hello world
```

- 출력
```
hello
```
#### ✔ 공백 전까지만 읽음
#### ❌ "world"는 다음 입력으로 남음

---

### 3️⃣ nextLine() 예시
```java
String s = sc.nextLine();
System.out.println(s);
```

- 입력
```
hello world
```

- 출력
```
hello world
```

#### ✔ 공백 포함 한 줄 전체
#### ✔ 문장 입력에 사용


---


# 배열 (Array)

## 1️⃣ 배열이란?
- 같은 자료형의 여러 값을 하나로 묶어서 저장하는 자료구조
```java
int[] arr = {1, 2, 3, 4};
```
- int형 데이터 여러 개를 하나의 이름(arr)으로 관리
- 인덱스(index)는 0부터 시작


## 2️⃣ 배열 선언 방법 (⭐중요)
### 1. 선언만 하기
```java
int[] arr;
```

### 2. 선언 + 생성
```java
int[] arr = new int[5];
```
- 크기 5
- 초기값 자동 설정됨

### 3. 선언 + 초기화
```java
int[] arr = {1, 2, 3, 4, 5};
```

### 4. new + 초기화
```java
int[] arr = new int[]{1, 2, 3};
```


## 3️⃣ 배열의 초기값

| 자료형     | 초기값                |
| ------- | ------------------ |
| int     | 0                  |
| double  | 0.0                |
| char    | '\u0000' (공백처럼 보임) |
| boolean | false              |
| String  | null               |

```java
int[] a = new int[3];
System.out.println(a[0]); // 0
```


## 4️⃣ 배열 접근 방법 (index)
```java
int[] arr = {10, 20, 30};

System.out.println(arr[0]); // 10
System.out.println(arr[1]); // 20
System.out.println(arr[2]); // 30
```
### ❌ 주의
```java
System.out.println(arr[3]); // 오류 (IndexOutOfBounds)
```


## 5️⃣ 배열 길이 (length)
```java
int[] arr = new int[5];
System.out.println(arr.length); // 5
```


## 6️⃣ 배열과 반복문 (필수)

### 기본 for문
```java
for (int i = 0; i < arr.length; i++) {
    System.out.println(arr[i]);
}
```

### 향상된 for문 (for-each)
```java
for (int x : arr) {
    System.out.println(x);
}
```

### 📌 차이점
- **for** → 인덱스 필요할 때

- **for-each** → 값만 필요할 때


## 7️⃣ 배열 입력받기 (Scanner)
```java
Scanner sc = new Scanner(System.in);

int n = sc.nextInt();
int[] arr = new int[n];

for (int i = 0; i < n; i++) {
    arr[i] = sc.nextInt();
}
```


## 8️⃣ 배열 출력하기 (주의)

### ❌ 이렇게 하면 주소값 나옴
```java
System.out.println(arr);
```

### ✅ 방법 1) 반복문
```java
for (int x : arr) {
    System.out.print(x + " ");
}
```

### ✅ 방법 2) Arrays.toString
```java
import java.util.Arrays;
System.out.println(Arrays.toString(arr));
```


## 9️⃣ 배열 복사

### 1. for문
```java
int[] copy = new int[arr.length];
for (int i = 0; i < arr.length; i++) {
    copy[i] = arr[i];
}
```

### 2. System.arraycopy
```java
System.arraycopy(arr, 0, copy, 0, arr.length);
```

### 3. Arrays.copyOf ⭐
```java
int[] copy = Arrays.copyOf(arr, arr.length);
```


## 🔟 배열 정렬
```java
Arrays.sort(arr);
```
- 오름차순 정렬
- 문자열도 가능


## 1️⃣1️⃣ 2차원 배열 (행렬)

### 선언
```java
int[][] arr = new int[2][3];
```

### 초기화
```java
int[][] arr = {
    {1, 2, 3},
    {4, 5, 6}
};
```

### 접근
```java
System.out.println(arr[0][1]); // 2
```

### 반복문
```java
for (int i = 0; i < arr.length; i++) {
    for (int j = 0; j < arr[i].length; j++) {
        System.out.print(arr[i][j] + " ");
    }
    System.out.println();
}
```


---


# 문자열

## 1️⃣ 문자열이란?

### ◾ 정의 및 특징
- 문자열은 문자들의 집합으로, `String` 이란 이름으로 사용됨
- 문자열은 큰 따옴표 (`" "`)를 사용하여 생성
- 한 번 생성되면 그 내용 직접 변경할 수 없는 **불변(immutable)** 자료형
- JAVA는 다양한 문자열 메소드와 연산자를 제공하여 문자열을 쉽게 다룰 수 있도록 지원
---
### ◾ 기본 구조
- 문자열은 큰따옴표 `" "`로 감싸서 정의
- 여러 줄의 문자열은 줄바꿈 문자 `\n` 를 사용
```java
String a = "Hello, World!";   // 한 줄 문자열
String b = "Java is fun";   // 큰따옴표 사용
String c = "해당 변수는\n여러 줄로\n작성된 문자열입니다.";   // 줄바꿈 문자 사용
String d = "";   // 빈 문자열
```
---
### ◾ 문자열 생성과 초기화

- #### 직접 값 할당
```java
String message = "안녕하세요!";
```

- #### 빈 문자열 생성
```java
String empty = "";
```
---
### ◾ 문자열, 수 변환
- 문자열을 정수나 실수로 변환할 수 있음
- `Integer.parseInt()` -> 정수로 변환
- `Double.parseDouble()` -> 실수로 변환
```java
String g = "20";    // 문자열 "20"
String h = "15.5";  // 문자열 "15.5"
System.out.println(Integer.parseInt(g) + 5);      // 출력: 25
System.out.println(Double.parseDouble(h) + 4.5);  // 출력: 20.0
```

- 다른 수 자료형을 문자로 변경할 때 -> `String.valueOf()` 메소드 사용
```java
int number = 123;
String text = String.valueOf(number);
System.out.println(text);  // 출력: "123"
```

- 다음과 같이 간단하게 변환하는 방법도 있음
```java
int number = 123;
String text = "" + number;
System.out.println(text);  // 출력: "123"
```
---
### 🚨 주의 사항
- 문자열이 수로 변환 가능한 형태여야 함
- `"123"`은 변환 가능
- `"abc"`는 불가능 => 변환시 `NumberFormatException` 에러 발생!
```java
int i = Integer.parseInt("abc");  // NumberFormatException 발생
```

---

## 2️⃣ 문자열의 인덱싱


### ◾ 인덱싱: 특정 문자 접근
- 문자열의 특정 문자에 접근하려면 `charAt(index)` 메소드를 사용
- 인덱스는 0부터 시작
```java
String text = "Java";
System.out.println(text.charAt(0));  // 출력: J
System.out.println(text.charAt(3));  // 출력: a
```

- 마지막 문자에 접근하려면 `text.charAt(text.length() - 1)` 사용
```java
System.out.println(text.charAt(text.length() - 1));  // 출력: a
```

- 인덱스가 문자열 번위를 초과하면 `StringIndexOutOfBoundsException` 에러 발생!
```java
System.out.println(text.charAt(10));  // 에러 발생
```

---

## 3️⃣ 메소드란?


### ◾ 메소드 정의
- 메소드는 특정 작업을 수행하기 위해 독립적으로 작성된 코드 블록임.
---
### ◾ 메소드 특징
- 재사용 가능, 동일한 작업을 여러 번 호출 가능
- 매개변수를 통해 외부 데이터 받아 처리하고, 결과 반환할 수 있음
- 클래스 내에서 정의되며, 객체 지향 프로그래밍의 중요한 구성 요소임.
---
### ◾ 문자열의 주요 메소드

#### `length()` : 문자열의 길이 알아내기
- `length()` : 문자열의 길이를 변환함
    - 길이에는 **공백, 줄바꿈, 특수문자** 모두 포함!
    - 줄바꿈(`\n`)은 하나의 문자로 취급됨
    
    ```java
    String text = "CodeTree";
    String text2 = "Java Programming\n";

    System.out.println(text.length());    // 출력: 8
    System.out.println(text2.length());   // 출력: 17
    ```

#### `substring()` : 문자열 자르기
- 메소드는 문자열의 일부분을 추출하여 새로운 문자열로 반환
    - `substring(start)` :  문자열의 `start` 인덱스부터 끝 인덱스까지의 부분 문자열 반환
    - `substring(start, end)` : 문자열의 `start` 인덱스부터 `end-1` 인덱스까지의 부분 문자열 반환

    ``` java
    String text = "Hello, Java!";
    String sub1 = text.substring(7);      // "Java!" 추출 (인덱스 7부터 끝까지)
    String sub2 = text.substring(7, 11);    // "Java" 추출 (인덱스 7부터 10까지)
    System.out.println(sub1);  // 출력: Java!
    System.out.println(sub2);  // 출력: Java
    ```


#### `substring()` 예제: 문자열의 변경
- String 은 불변(immutable) 자료형이므로, 개별 문자를 직접 변경할 수 없음
- 문자열을 변경하려면 `substring()` 을 통해 새로운 문자열을 생성하는 방법을 고려해볼 수 있음

```java
String text = "Java";
// text.charAt(0) = 'K'; // 에러 발생
String newText = "K" + text.substring(1); // "Kava" 생성
System.out.println(newText);  // 출력: Kava
```

#### `toUpperCase()`, `toLowerCase()` : 대소문자 변환
- `toUpperCase()` : 모든 문자열을 대문자로 변환
- `toLowerCase()` : 모든 문자열을 소문자로 변환

```java
String text = "Java Programming";
System.out.println(text.toUpperCase());  // 출력: "JAVA PROGRAMMING"
System.out.println(text.toLowerCase());  // 출력: "java programming"
```

#### `trim()` : 양쪽 공백 제거
- 문자열 양쪽에 있는 공백 및 기타 공백 문자를 제거함

```java
String text = "   Hello, World!   ";
System.out.println(text.trim());  // 출력: "Hello, World!"
```

#### `replace()` : 특정 문자열 대체
- 문자열 내에서 특정 부분을 다른 문자열로 대체함
```java
String text = "Hello, World!";
String newText = text.replace("World", "Java");
System.out.println(newText);  // 출력: "Hello, Java!"
```

#### `indexOf()`, `lastIndexOf()` : 문자열 찾기
- `indexOf()` 메소드 : 문자열 내에서 특정 문자열의 시작 인덱스를 반환하며, 찾지 못하면 -1 을 반환.
- 찾으려는 문자열이 여러 번 있을 경우 **가장 처음 등장한 위치의 시작 인덱스를 반환**
```java
String text = "Hello, World!";
System.out.println(text.indexOf("World"));  // 출력: 7
System.out.println(text.indexOf("Java"));   // 출력: -1
```

- `lastIndexOf()` : 특정 문자열이 마지막으로 등장하는 인덱스를 반환.
- 찾으려는 문자열이 여러 번 쓰인 경우에는 마지막으로 등장한 위치의 시작 인덱스를 반환함.
```java
String text2 = "banana";
System.out.println(text2.lastIndexOf("na"));  // 출력: 4
```
---
## 4️⃣ 특수 문자

### ◾ 정의 및 사용법
- 특수 문자는 문자열 내에서 특정 동작을 수행하거나 특수한 문자를 표현하기 위해 사용됩니다.
- 이들은 백슬래시(\)로 시작하는 이스케이프 문자입니다.

- 대표적인 특수 문자로는 \n (새 줄), \t (탭), \\ (백슬래시), \' (작은따옴표), \" (큰따옴표) 등이 있습니다.
---
### ◾ 주요 특수 문자와 예시

#### 1. `\n` : 줄 바꿈 (Newline)
```java
String multilineStr = "안녕하세요.\nJava를 배워봅시다.";
System.out.println(multilineStr);
```

- 출력
```
안녕하세요.
Java를 배워봅시다.
```

#### 2. `\t` : 탭 (Tab)
```java
String tabStr = "이름\t나이\t직업";
System.out.println(tabStr);
```

- 출력:
```
이름    나이    직업
```

#### 3. `\\` : 백슬래시 (Backslash)
```java
String path = "C:\\Users\\Teddy\\Documents";
System.out.println(path);
```

- 출력:
```
C:\Users\Teddy\Documents
```

#### 4. `\'` : 작은따옴표 (Single Quote)
```java
String quote = "그는 말했다, \'안녕하세요\'";
System.out.println(quote);
```

- 출력:
```
그는 말했다, '안녕하세요'
```

#### 5. `\"` : 큰따옴표 (Double Quote)
```java
String quote2 = "그녀는 말했다, \"Java는 재미있어요\"";
System.out.println(quote2);
```

- 출력:
```
그녀는 말했다, "Java는 재미있어요"
```

---

## 📚 정리
- 문자열은 문자들의 집합으로, 큰따옴표(`""`)로 표현되며, JAVA에서는 String 클래스로 구현됩니다.

- 문자열은 **불변(immutable)** 자료형으로, 한 번 생성되면 직접 수정할 수 없습니다.

- 메소드는 특정 작업을 수행하는 코드 블록으로, 여러 반복되는 작업에서 자주 사용됩니다.

- 다양한 문자열 메소드(`toUpperCase()`, `toLowerCase()`, `trim()`, `replace()`, `split()`, `indexOf()`, `lastIndexOf()` 등)와 반복문을 통한 직접 구현을 활용하여 문자열을 효율적으로 다룰 수 있습니다.

- **인덱싱**은 `charAt()` 메소드를 사용하여 수행하며, 문자열의 길이는 `length()` 메소드를 사용합니다.

- **특수 문자**(이스케이프 문자)를 사용하여 줄 바꿈, 탭, 백슬래시, 따옴표 등을 문자열에 포함시킬 수 있습니다.


---


# charAt() 메서드

## 1️⃣ `charAt()`이란?

- #### 문자열(String)에서 특정 위치의 문자 하나를 꺼내는 메서드야.
```java
문자열.charAt(인덱스)
```
- 반환값 타입: char
- 문자열은 0번부터 시작 (중요 ⚠️)


## 2️⃣ 기본 예제

```java
String str = "Java";

char c = str.charAt(0);
System.out.println(c);
```

#### 실행 결과
```
J
```


## 3️⃣ 반복문과 함께 사용 (자주 나옴!)

### 문자열 한 글자씩 출력
```JAVA
String s = "Hello";

for (int i = 0; i < s.length(); i++) {
    System.out.println(s.charAt(i));
}
```

- 출력
```
H
e
l
l
o
```
#### 📌 length()는 문자열 길이
#### 📌 charAt(i)는 i번째 문자


## 4️⃣ charAt + 조건문 예제
### 예: 문자열에 'a'가 있는지 확인
```java
String s = "banana";

for (int i = 0; i < s.length(); i++) {
    if (s.charAt(i) == 'a') {
        System.out.println("a 발견!");
    }
}
```

#### 📌 비교할 때는 작은따옴표 'a' 사용
- (문자(char)는 ' ' / 문자열(String)은 " ")



## 5️⃣ Scanner 입력 + charAt
```java
Scanner sc = new Scanner(System.in);
String s = sc.next();

System.out.println(s.charAt(0)); // 첫 글자
```

#### 📌 문자열 입력받은 뒤
- 첫 글자
- 마지막 글자   
    => 이런 문제에서 charAt 필수



## 6️⃣ 마지막 문자 꺼내기 ⭐
```java
String s = "Hello";

char last = s.charAt(s.length() - 1);
System.out.println(last);
```

#### 📌 길이가 5 → 마지막 인덱스는 4


## 7️⃣ 자주 하는 실수 

### ❌ 1. 문자열에 바로 인덱싱하려고 하기
```java
s[0]; // ❌ Java에서는 안 됨
```

#### ✅ 올바른 방법
```java
s.charAt(0);
```

### ❌ 2. char 비교에 큰따옴표 사용
```java
if (s.charAt(i) == "a") // ❌
```

#### ✅ 올바른 방법
```java
if (s.charAt(i) == 'a') // ⭕
```