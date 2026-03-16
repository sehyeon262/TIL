## Context Switching

### 개념
- Context Switching은 CPU가 한 프로세스(또는 스레드)에서 다른 프로세스로 작업을 전환할 때 **현재 상태(Context)를 저장하고 새로운 작업의 상태를 불러오는 과정**이다.
- 즉, CPU가 여러 작업을 번갈아 수행하기 위해 작업을 전환하는 과정이다.

---

### 왜 필요한가?
- CPU는 한 번에 하나의 작업만 실행할 수 있다.
- 하지만 여러 프로그램이 동시에 실행되는 것처럼 보이기 위해 빠르게 작업을 전환한다.

**예시**
```
프로세스 A 실행
↓
Context Switching
↓
프로세스 B 실행
↓
Context Switching
↓
프로세스 C 실행
```
이렇게 빠르게 전환되기 때문에 멀티태스킹이 가능하다.

---

### Context에 포함되는 정보
Context에는 다음과 같은 정보가 포함된다.
- Program Counter (다음 실행 명령 위치)
- CPU Register 값
- Process State
- Memory 정보
- Stack 정보

이 정보들을 저장하고 복원하면서 작업을 전환한다.

---


### 단점
Context Switching은 **오버헤드가 발생한다.**

**이유**
- CPU 레지스터 저장
- 메모리 상태 저장
- 새 프로세스 상태 복원

그래서 너무 많이 발생하면 성능이 떨어질 수 있다.

---

### 언제 많이 발생할까?
- 멀티 프로세스 환경
- 멀티 스레드 환경
- CPU Scheduling

---

### 면접에서 이어지는 질문
- Context Switching이 발생하는 이유
- 멀티 프로세스 vs 멀티 스레드 차이
- CPU Scheduling 알고리즘
- Thread가 Process보다 빠른 이유

---

### 한 줄 정리
> Context Switching은 CPU가 여러 프로세스를 실행하기 위해 현재 작업의 상태를 저장하고 다른 작업으로 전환하는 과정이다.