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
