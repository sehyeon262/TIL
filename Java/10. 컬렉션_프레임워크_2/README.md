# 📚 목차
### 컬렉션 프레임워크2
- Map 계열
- Stack
- Queue
- Deque
- 정렬


---


# 🎯 학습 목표
✔ 컬렉션 프레임워크의 구조와 핵심 인터페이스를 이해하고, 자료구조 선택 기준을 설명할 수 있다.

✔ Map 계열의 키-값 저장 구조와 탐색·삽입·정렬 특성을 파악하여 요구사항에 적합한 구현체를 선택할 수 있다.

✔ Stack·Queue·Deque 의 동작 원리를 이해하고 활용할 수 있다.

✔ Comparator·Comparable 인터페이스를 구현하여 사용자 정의 객체를 정렬할 수 있다.


---


# ✅ Map 계열


## ◾ Map 계열 컬렉션
- 키(Key)와 값(Value)의 쌍으로 데이터를 저장하는 구조
- 키를 기준으로 값에 접근하며 키는 중복을 허용하지 않음 (값은 허용)
- 키를 활용하여 빠른 검색 가능
- 키 또는 값에 null 허용 (일부 TreeMap 에서는 허용하지 않음)
- 구현 클래스
    - HashMap
    - LinkedHashMap
    - TreeMap

https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html


## ◾ HashMap
- 데이터의 저장 순서를 유지하지 않음
- 내부적으로 Hash Table을 사용하여 데이터 저장 및 검색
- null 키를 하나 허용하며, 여러 개의 null 값을 허용
- 빠른 검색, 삽입, 삭제를 지원

> 💡 서로 다른 키가 동일한 Hash 값을 가질 경우, 충돌이 발생하면 체이닝을 사용하여 연결리스트로 관리


## ◾ LinkedHashMap
- 데이터의 저장 순서를 유지
- 내부적으로 Hash Table + 이중 연결 리스트를 사용하여 데이터 저장 및 검색
- null 키를 하나 허용하며, 여러 개의 null 값을 허용
- 빠른 검색, 삽입, 삭제를 지원
- 해시 충돌 시 HashMap과 동일하게 처리


## ◾ TreeMap
- 키를 기준으로 정렬된 상태로 데이터를 유지 (기본 오름차순)
- 사용자 정의 정렬이 필요한 경우 Comparator를 사용
- 내부적으로 레드-블랙 트리 기반으로 구현
- null 키는 허용하지 않음


## ◾ Map 주요 메서드
| 메서드                         | 내용                         |
| --------------------------- | -------------------------- |
| put(K key, V value)         | 키-값 쌍을 추가 (이미 키가 존재하면 덮어씀) |
| get(Object key)             | 키에 해당하는 값을 반환              |
| remove(Object key)          | 키의 값을 지우고 반환               |
| containsKey(Object key)     | 특정 키가 있는지 확인               |
| containsValue(Object value) | 특정 값이 있는지 확인               |
| keySet()                    | 모든 키를 반환 (Set 형태)          |
| values()                    | 모든 값을 반환 (Collection 형태)   |
| isEmpty()                   | Map이 비어 있는지 확인             |
| size()                      | Map에 저장된 키-값 쌍의 개수를 반환     |


---


# ✅ Stack


## ◾ Stack 이란?
- **후입선출(Last-In First-Out, LIFO) 구조**
- Vector 기반으로 동작

| 메서드          | 내용                          |
| ------------ | --------------------------- |
| push(E item) | 스택의 맨 위에 데이터를 추가            |
| pop()        | 스택의 맨 위에 있는 데이터를 제거하고 반환    |
| peek()       | 스택의 맨 위에 있는 데이터를 제거하지 않고 반환 |
| isEmpty()    | 스택이 비어 있는지 확인               |
| size()       | 스택에 저장된 요소의 개수를 반환          |


---


# ✅ Queue

## ◾ Queue 란?
- **선입선출(First-In First-Out, FIFO) 구조**
- 다양한 구현체 (LinkedList, ArrayDeque)가 있음

| 메서드        | 내용                               |
| ---------- | -------------------------------- |
| offer(E e) | 큐의 맨 뒤에 요소를 추가 (공간 부족 시 실패 반환)   |
| add(E e)   | 큐의 맨 뒤에 요소를 추가 (공간 부족 시 예외 발생)   |
| poll()     | 큐의 맨 앞 요소 제거 후 반환 (비어 있으면 null)  |
| remove()   | 큐의 맨 앞 요소 제거 후 반환 (비어 있으면 예외 발생) |
| peek()     | 큐의 맨 앞 요소 반환 (비어 있으면 null 반환)    |
| element()  | 큐의 맨 앞 요소 반환 (비어 있으면 예외 발생)      |
| isEmpty()  | 큐가 비어 있는지 확인                     |
| size()     | 큐에 저장된 요소의 개수를 반환                |


# ✅ Deque

## ◾ Deque 이란?
- **양방향 큐 (양쪽에서 삽입과 삭제 가능)**
- ArrayDeque (배열 기반), LinkedList (연결리스트 기반) 사용 가능

| 메서드           | 내용                              |
| ------------- | ------------------------------- |
| addFirst(E e) | 덱 맨 앞에 요소를 추가 (공간 부족 시 예외 발생)   |
| addLast(E e)  | 덱 맨 뒤에 요소를 추가 (공간 부족 시 예외 발생)   |
| removeFirst() | 덱 맨 앞 요소 제거 후 반환 (비어 있으면 예외 발생) |
| removeLast()  | 덱 맨 뒤 요소 제거 후 반환 (비어 있으면 예외 발생) |
| getFirst()    | 덱 맨 앞 요소 반환 (비어 있으면 예외 발생)      |
| getLast()     | 덱 맨 뒤 요소 반환 (비어 있으면 예외 발생)      |
| isEmpty()     | 덱이 비어 있는지 확인                    |
| size()        | 덱에 저장된 요소의 개수를 반환               |


# ✅ 정렬

## ◾ 정렬(Sort)
- 요소들을 특정 기준에 맞추어 오름차순 또는 내림차순으로 배치 하는 것
- **순서를 가지는 Collection들만 정렬 가능**
- 자바 제공 클래스 → Collections의 sort()를 이용하여 정렬
    
    → 배열은 Arrays의 sort()를 이용하여 정렬


## ◾ Comparable 인터페이스
- 객체의 기본 정렬 기준을 정의
- 클래스에 직접 구현
- compareTo(T o) 메서드를 구현하여 정렬 기준을 정의
    
    ex) 이름 순 정렬, 나이 순 정렬 등
```java
public interface Comparable<T> {
    public int compareTo(T o);
}
```

| 반환 값 | 의미                   |
| ---- | -------------------- |
| 0    | 현재 객체와 비교 대상 객체가 같음  |
| 양수   | 현재 객체가 비교 대상 객체보다 큼  |
| 음수   | 현재 객체가 비교 대상 객체보다 작음 |


## ◾ Comparator 인터페이스
- 별도의 정렬 기준을 정의
- 정렬 기준이 여러 개 필요한 경우 유용
- 클래스 외부에서 정렬 기준을 정의하며, 특정 필드나 사용자 정의 기준으로 정렬할 수 있음
- compare(T o1, T o2) 메서드를 구현하여 정렬 기준을 정의
```java
public interface Comparator<T> {
    int compare(T o1, T o2);
}
```
| 반환 값 | 의미                    |
| ---- | --------------------- |
| 0    | 두 객체가 같음              |
| 양수   | 첫 번째 객체가 두 번째 객체보다 큼  |
| 음수   | 첫 번째 객체가 두 번째 객체보다 작음 |


## ◾ omparator 인터페이스
- 1회성 객체 사용 시 anonymous inner class 사용
- 클래스 정의, 객체 생성을 한번에 처리

```java
// before
Collections.sort(names, new StringLengthComparator());

// after
Collections.sort(names, new Comparator<String>() {
    @Override
    public int compare(String o1, String o2) {
        return Integer.compare(o1.length(), o2.length());
    }
});
```
---
#### 📌 Lambda 식
- 함수적 프로그래밍의 형태로 재사용 가능한 코드 블록
- 기존의 anonymous inn class를 이용한 처리 방식을 간결하게 처리

- Lambda 표현식 사용
```java
Collections.sort(names, (o1, o2)->{
    return Integer.compare(o1.length(), o2.length());
});
```