## Garbage Collection (가비지 컬렉션)
- **더 이상 사용되지 않는 메모리를 자동으로 회수하는 기능**
- 주로 Java, Python, JavaScript 같은 관리형 언어에서 사용됨.


### 왜 필요한가?
- 프로그램이 실행되면서 객체를 계속 생성하면 사용이 끝난 객체도 메모리에 남아 있게 됨.
- 이걸 정리하지 않으면 메모리 누수(Memory Leak) 발생
- 결국 OutOfMemoryError 발생 가능

- Garbage Collector(GC)는 참조되지 않는 객체를 찾아 자동으로 제거함.


### 동작 원리
1. Mark & Sweep 방식
1-1. Mark (표시 단계)
- 루트 객체에서 시작해 참조되는 객체를 표시

1-2. Sweep (정리 단계)
- 표시되는 않는 객체를 메모리에서 제거


### Java 기준 메모리 구조
- Young Generation (새 객체)
- Old Generation (오래 살아남은 객체)
- GC는 이 영역을 나눠 관리

=> 객체가 오래 살아남으면 Old 영역으로 이동
=> Old 영역 GC는 비용이 큼 (Full GC 발생 시 성능 저하)


### 면접에서 자주 나오는 질문
- GC가 동작하는 시점은?
- Stop-The-World란?
- Minor GC와 Full GC 차이?
- 메모리 누수는 GC가 있어도 발생할 수 있는가?


### 면접 한 줄 정리
- Garbage Collection은 더 이상 참조되지 않는 객체를 자동으로 정리하여 메모리 누수를 방지하는 메모리 관리 기법이다.