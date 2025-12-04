# 📘 목차 - 클래스와 객체
1. 함수

2. 클래스

3. 생성자

4. 객체지향 프로그래밍


---


# ✅ 함수 


## 🔵 함수(Function)
- 특정 작업을 수행하는 코드 블록
- 반복적으로 사용되는 코드를 재사용 가능하게 만들어 가독성과 유지 보수성을 향상시킴
- ex) 1 ~ 5 까지 더해줘, 6 ~ 10 까지 더해줘 등


## 🔵 함수(Function) 정리
- 특정 작업을 수행하는 코드 블록에 이름을 붙인 것
- 실행 가능한 단위
- 함수의 구성 요소: 반환타입(또는 void), 함수이름, 매개변수, 함수 내용
- return 구문은 반환 타입이 void 인 경우 생략이 가능
```java
int add(int a, int b) {
    return a + b;
}
```
```java
void printHelloWorld() {
    System.out.println("Hello, World!");
}
```


---


# ✅ 클래스 


## 🔵 사람의 정보를 관리하자. (배열 도입)
![alt text](image.png)

```java
String[] names = new String[2];
names[0] = "Yang";
names[1] = "Hong";

int[] ages = new int[2];
ages[0] = 45;
ages[1] = 25;

String[] hobbies = new String[2];
hobbies[0] = "YouTube";
hobbies[1] = "Golf";
```


## 🔵 사람의 정보를 관리하자.

![alt text](image-1.png)

```java
public class Person {
    String name;
    int age;
    String hobby;
}
```


## 🔵 사람의 정보를 출력하자.
```
나의 이름은 Yang 입니다.
나이는 45세, 취미는 YouTube 입니다.

나의 이름은 Hong 입니다.
나이는 25세, 취미는 Golf 입니다.
```
⬇️ ⬇️ ⬇️
```java
info(name, age, hobby){
    나의 이름은 name 입니다.
    나이는 age세, 취미는 hobby 입니다.
}
```


## 🔵 사람의 정보를 관리하자.
![alt text](image-2.png)

```java
public class Person {
    String name;
    int age;
    String hobby;

    public void info() {
        System.out.println("나의 이름은 " + name + "입니다.");
        System.out.println("나이는 " + age + "세, 취미는 " + hobby + " 입니다.");
    }
}
```


## 🔵 클래스(Class)
- 관련 있는 변수(필드)와 함수(메서드)를 묶어서 만든 사용자 정의 자료형(데이터 타입)
- 객체를 생성하기 위한 설계도(Blueprint)
- 클래스를 통해 생성된 객체 → 인스턴스(Instance)
```
붕어빵 틀 → 클래스
붕어빵 → 인스턴스
```


## 🔵 클래스 구성 요소
### 필드(Field)
- 클래스에 선언된 변수 (멤버 변수, 멤버 필드)
- 클래스의 속성을 정의 → 각 인스턴스는 필드에 고유한 값을 가질 수 있음

### 메서드(Method)
- 특정 동작을 수행하는 코드 블록 (객체의 행동을 정의)
- 입력(매개변수)을 이용하여 처리하고 결과(반환 값)를 반환
- 오버로딩 가능

### 생성자(Constructor)
- 객체 생성 시 호출되는 특별한 메서드 (필드 초기화 또는 생성 시 필요한 작업 수행)
- 클래스 이름과 같고, 반환타입이 없음


## 🔵 클래스 선언
```scss
[제한자(Modifier)] class 클래스이름 {

    // 멤버 변수, 필드 (속성 정의)
    [제한자(Modifier)] 데이터타입 변수이름 [=초깃값];

    // 생성자
    [제한자(Modifier)] 클래스이름([매개변수들]) {
        생성자 본문
    }

    // 메서드 (기능 정의)
    [제한자(Modifier)] 반환타입!void 메서드이름([매개변수들]) {
        메서드 본문
    }
}
```


## 🔵 객체(인스턴스) 생성
```cpp
클래스이름 객체이름 = new 클래스이름([생성자 매개변수들]);
```


## 🔵 객체 멤버 접근
- . (dot) 연산자를 활용
- 필드 값 접근 → `객체이름.멤버변수이름`
- 메서드 호출 → `객체이름.멤버메서드이름([매개변수들]);`


## 🔵 변수의 종류
| 변수 종류                       | 선언                                | 생성 시기              | 특징               |
| --------------------------- | --------------------------------- | ------------------ | ---------------- |
| 클래스 변수 (Class Variable)     | 클래스에서 멤버 필드 선언 시 static 키워드를 사용 O | 클래스가 메모리에 로드될 때 생성 | 모든 인스턴스가 공유하는 변수 |
| 인스턴스 변수 (Instance Variable) | 클래스에서 멤버 필드 선언 시 static 키워드를 사용 X | 인스턴스가 생성될 때 생성     | 각 인스턴스마다 별도로 생성  |
| 지역 변수 (Local Variable)      | 메서드, 생성자 또는 초기화 블록 내에서 선언         | 선언된 블록이 실행될 때 생성   | 블록이 끝나면 소멸       |


## 🔵 메서드(Method)
- 객체가 할 수 있는 행동을 정의
- 어떤 작업을 수행하는 명령문의 집합에 이름을 붙여 놓은 것
- 메서드의 이름은 소문자로 시작하는 것이 관례
- 자바에서는 독립적으로 정의된 함수가 없어 함수 == 메서드


## 🔵 메서드 선언
- 선언 시 {} 안에 메서드가 해야 할 일을 정의


## 🔵 메서드 호출
- 객체를 생성한 후 객체의 멤버 메서드를 호출한다.
- 클래스 객체.메서드 이름으로 호출

```java
Person p = new Person();
p.info();
```

- static 이 붙어 있으면 클래스이름.메서드이름() 으로 호출
```java
Person.hello();
```

```java
public class Person {
    public void info() {
        // 메서드 내용 정의
    }
    public static void hello() {
        // 메서드 내용 정의
    }
}
```


## 🔵 매개 변수 (Parameter)
- 메서드에 입력 데이터를 전달하는 역할 (생략 가능)
- 메서드 선언 시 타입과 이름을 지정
- 호출할 때는 인자(Argument)라고도 함
- 매개 변수는 묵시적 형변환을 이용하여 전달 됨

```java
public void study(int time) {
    //int time = ?
    //파라미터는 해당 위치에 선언한 지역변수
    System.out.println(time + "시간 공부.");
}

Person p = new Person();
p.study(10);
```
```java
p.study((byte) 10);   // O
p.study((short) 10);  // O
p.study(10);          // O
p.study(10L);         // X
p.study(10.0f);       // X
p.study(10.0);        // X
p.study(10, 10);      // X
```


## 🔵 가변인자 (Variable Arguments)
- 메서드에서 매개변수 개수를 가변적으로 받을 수 있음. (0개 ~)
- 배열처럼 처리되지만 호출 시 배열을 명시적으로 생성할 필요가 없음
- 가변 인자는 항상 마지막 위치해야 함
- 여러 개의 가변 인자 불가

```
리턴타입 메서드이름(타입... 변수명) {
    // 내부적으로 변수명은 배열처럼 사용 가능
}
```
```java
public class VarArgsExample {
    public static void printNumbers(int... numbers) {
        for (int n : numbers) {
            System.out.println(n);
        }
    }
}

public static void main(String[] args) {
    printNumbers(1, 2, 3);
    printNumbers(10);
    printNumbers();   // 0개도 가능
}
```


## 🔵 반환 타입(Return Type)
- 메서드가 수행한 결과를 반환
- 메서드 선언 시 타입을 지정, 없다면 void 작성 (생략 불가능)
- 반환 타입이 void가 아니라면 반드시 해당 타입의 값을 return 해야함
- 반환 타입은 메서드 당 하나만 작성 가능
- 결과를 받을 때 묵시적 형 변환 적용
```java
public int getAge() {
    return age;
}

Person p = new Person();
p.name = "Yang";
p.age = 45;
p.hobby = "유튜브";

int age = p.getAge();
```


## 🔵 메서드 오버로딩 (Overloading)
  • 이름이 같고 매개변수가 다른 메서드를 여러 개 정의하는 것
  • 중복 코드에 대한 효율적 관리 가능
  • 파라미터의 개수 또는 순서, 타입이 달라야 할 것 (파라미터 이름만 다른 것은 X)
  • 리턴 타입이 다른 것은 의미 X


---


# ✅ 생성자


## 🔵 생성자?
- 객체 생성 시 호출되는 특별한 메서드 (필드 초기화 또는 생성시 필요한 작업 수행)
- 클래스 이름과 같고, 반환타입이 없음 **(void 작성 X)**
- **new** 키워드와 함께 호출하여 객체 생성
- 객체 생성 시 반드시 호출 되어야 함
- 기본 생성자(매개 변수가 없음)를 자동으로 제공 **(생성자 미 작성 시)**
- 매개변수의 개수가 다르거나, 자료형이 다른 여러 개의 생성자가 있을 수 있음 (생성자 오버로딩)
- 생성자의 첫번째 라인으로 this() 생성자를 사용하여 또 다른 생성자를 하나 호출 가능


## 🔵 기본 생성자
- 매개 변수가 없는 생성자
- 개발자가 따로 정의하지 않으면 컴파일러가 자동으로 추가
- 생성자가 하나라도 정의 되어 있으면 컴파일러는 기본 생성자를 추가하지 않음

```java
public class Dog {
    public Dog() { }
}

public class Main {
    public static void main(String[] args) {
        // 객체 생성
        Dog d = new Dog();
    }
}
```


## 🔵 매개변수 생성자
- 매개 변수를 받아 객체를 초기화 하는 생성자
- 생성자 호출 시 인자를 넘겨주어야 함
- 작성 시 컴파일러는 기본 생성자를 작성하지 않음
```java
public class Dog {
    String name;
    int age;

    public Dog(String n, int a){
        name = n;
        age = a;
    }
}
```
```java
public class Main {
    public static void main(String [] args) {
        Dog d1 = new Dog( );
        d1.name = "마루";
        d1.age = 5;

        Dog d2 = new Dog("마리", 5);
    }
}
```


## 🔵 생성자 오버로딩
- 같은 이름의 생성자를 매개 변수의 개수나 타입이 다르게 여러 개 정의
- 매개 변수의 타입, 개수, 순서 등이 달라야 함

```java
public class Dog {
    1 : Dog( ) { }
    2 : Dog(String name) { }
    3 : Dog(int age) { }
    4 : Dog(String name, int age) { }
    5 : Dog(String name, String type) { }
    6 : Dog(String type, int age) { }
    7 : Dog(String type, String name) { }
    8 : Dog(String name, String type, int age) { }
    9 : Dog(String name, int age, String type) { }
}
```
### [메모 박스]
- 각 번호의 생성자가 동작하지 안 할지 생각해보자


## 🔵 this.
- 매개변수 이름과 필드 이름이 같을 때, 필드를 구분하기 위해서 사용 (다르면 생략 가능)
- 참조 변수로써 현재 인스턴스 자기 자신을 가리킴
- static 영역에서 사용 불가능

```java
public class Dog {
    String name;
    int age;

    Dog(String name, int age) {
        this.name = name; // 필드와 매개변수를 구분
        this.age = age;
    }
}
```


## 🔵 this()
- 해당 키워드를 통해 같은 클래스의 다른 생성자를 호출
- 같은 클래스 내에서만 호출 가능
- 반드시 생성자의 첫번째 줄에 위치
- 중복 코드를 제거하거나, 생성자 체인을 통해 간결하고 유지보수하기 쉬운 코드 작성에 도움

```java
public class Dog {
    String name;
    int age;

    Dog(int age){
        this("익명", 2);
    }

    Dog(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
```


---


# ✅ 객체지향 프로그래밍


## 🔵 객체지향 프로그래밍 (OOP, Object Oriented Programming)
- 객체 : 의사나 행위가 미치는 대상, 작용의 대상 / 세상의 모든 사물, 개념(유·무형) 등
- 객체(Object): 데이터와 관련된 알고리즘(메서드)를 하나의 단위로 묶어 놓은 것
- 객체 모델링 : 현실세계의 객체를 SW 객체로 설계하는 것
    
    ![alt text](image-3.png)


## 🔵 객체지향 프로그래밍 특징 ( A PIE )
- Abstraction (추상화)
- Polymorphism (다형성)
- Inheritance (상속)
- Encapsulation (캡슐화)


## 🔵 객체지향 프로그래밍 장점
- 모듈화 된 프로그래밍
- 재사용성이 높다
