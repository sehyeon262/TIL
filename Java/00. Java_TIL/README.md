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

