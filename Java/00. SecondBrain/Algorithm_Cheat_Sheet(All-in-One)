## Java Algorithm Cheat Sheet (All-in-One)


### 0️⃣ 공통 기본 템플릿 (국룰)

```java
import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int[] arr;
    static boolean[] visited;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // 입력
        N = Integer.parseInt(br.readLine());
        arr = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // 알고리즘 호출
    }
}
```


### 1️⃣ DFS (깊이 우선 탐색)

#### 문제 판단
- 연결 요소
- 경로 탐색
- 모든 경우 탐색

#### 핵심
- 재귀 / 스택
- 방문 체크 필수

```java
static ArrayList<Integer>[] graph;
static boolean[] visited;

static void dfs(int v) {
    visited[v] = true;

    for (int next : graph[v]) {
        if (!visited[next]) {
            dfs(next);
        }
    }
}
```


### 2️⃣ BFS (너비 우선 탐색)

#### 문제 판단
- 최단 거리 (가중치 ❌)
- 미로, 레벨 탐색

#### 핵심
- Queue 사용
- 거리 배열 활용

```java
static void bfs(int start) {
    Queue<Integer> q = new LinkedList<>();
    q.add(start);
    visited[start] = true;

    while (!q.isEmpty()) {
        int cur = q.poll();

        for (int next : graph[cur]) {
            if (!visited[next]) {
                visited[next] = true;
                q.add(next);
            }
        }
    }
}
```


### 3️⃣ DP (동적 계획법)

#### 문제 판단
- 최댓값 / 최솟값
- 경우의 수
- 중복 계산 많음

#### 핵심
- 점화식
- dp 배열 정의

```java
int[] dp = new int[n + 1];
dp[0] = 0;
dp[1] = 1;

for (int i = 2; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
}
```


### 4️⃣ 백트래킹

#### 문제 판단
- 모든 경우 시도
- 조건 만족 시만 진행

#### 핵심
- DFS + 되돌리기

```java
static void backtrack(int depth) {
    if (depth == N) return;

    for (int i = 0; i < N; i++) {
        if (!visited[i]) {
            visited[i] = true;
            backtrack(depth + 1);
            visited[i] = false;
        }
    }
}
```


### 5️⃣ Stack

#### 문제 판단
- 괄호 검사
- 이전 상태 추적

```java
Stack<Integer> stack = new Stack<>();
stack.push(1);
stack.pop();
stack.peek();
```


### 6️⃣ 정렬 (Sorting)

#### 문제 판단
- 최댓값 / 최솟값
- 이분 탐색 전처리

```java
Arrays.sort(arr); // 오름차순
```


### 7️⃣ 그래프 최단 비용 (다익스트라)

#### 문제 판단
- 가중치 있음
- 최소 비용

```java
static class Node implements Comparable<Node> {
    int v, cost;
    Node(int v, int cost) {
        this.v = v;
        this.cost = cost;
    }
    public int compareTo(Node o) {
        return this.cost - o.cost;
    }
}

static void dijkstra(int start) {
    PriorityQueue<Node> pq = new PriorityQueue<>();
    Arrays.fill(dist, Integer.MAX_VALUE);

    dist[start] = 0;
    pq.add(new Node(start, 0));

    while (!pq.isEmpty()) {
        Node cur = pq.poll();

        if (dist[cur.v] < cur.cost) continue;

        for (Node next : graph[cur.v]) {
            if (dist[next.v] > cur.cost + next.cost) {
                dist[next.v] = cur.cost + next.cost;
                pq.add(new Node(next.v, dist[next.v]));
            }
        }
    }
}
```


### 8️⃣ 조합 (Combination)

#### 문제 판단
- 순서 ❌
- nCr

```java
static void comb(int idx, int cnt) {
    if (cnt == R) return;
    if (idx == N) return;

    comb(idx + 1, cnt + 1); // 선택
    comb(idx + 1, cnt);     // 미선택
}
```


### 9️⃣ 분할 정복

#### 문제 판단
- 반으로 쪼갬
- 병합정렬 / 거듭제곱

```java
static int divide(int l, int r) {
    if (l == r) return arr[l];
    int mid = (l + r) / 2;
    return divide(l, mid) + divide(mid + 1, r);
}
```


### 🔟 부분집합

#### 문제 판단
- 모든 포함/미포함

```java
static void subset(int idx) {
    if (idx == N) return;

    selected[idx] = true;
    subset(idx + 1);

    selected[idx] = false;
    subset(idx + 1);
}
```


### 1️⃣1️⃣ 이분 탐색

#### 문제 판단
- 정렬됨
- 범위 줄이기

```java
static int binarySearch(int target) {
    int l = 0, r = N - 1;

    while (l <= r) {
        int mid = (l + r) / 2;
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) l = mid + 1;
        else r = mid - 1;
    }
    return -1;
}
```


### 1️⃣2️⃣ 파라메트릭 서치

#### 문제 판단
- “가능한가?”
- 최소 / 최대

```java
static boolean check(int mid) {
    return true; // 조건 판별
}

static int parametric() {
    int l = 0, r = 1000000, ans = 0;

    while (l <= r) {
        int mid = (l + r) / 2;
        if (check(mid)) {
            ans = mid;
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    return ans;
}
```


### 1️⃣3️⃣ 투 포인터 / 슬라이딩 윈도우

```java
int l = 0, sum = 0;
for (int r = 0; r < N; r++) {
    sum += arr[r];

    while (sum > M) {
        sum -= arr[l++];
    }
}
```


### 1️⃣4️⃣ 유니온 파인드

```java
static int[] parent;

static int find(int x) {
    if (parent[x] == x) return x;
    return parent[x] = find(parent[x]);
}

static void union(int a, int b) {
    a = find(a);
    b = find(b);
    if (a != b) parent[b] = a;
}
```


### 1️⃣5️⃣ MST (크루스칼)

```java
Arrays.sort(edges);
for (Edge e : edges) {
    if (find(e.u) != find(e.v)) {
        union(e.u, e.v);
        cost += e.w;
    }
}
```


### 1️⃣6️⃣ 위상 정렬

```java
Queue<Integer> q = new LinkedList<>();
for (int i = 1; i <= N; i++) {
    if (indegree[i] == 0) q.add(i);
}

while (!q.isEmpty()) {
    int cur = q.poll();
    for (int next : graph[cur]) {
        if (--indegree[next] == 0) q.add(next);
    }
}
```


### 1️⃣7️⃣ 비트마스킹

```java
for (int mask = 0; mask < (1 << N); mask++) {
    for (int i = 0; i < N; i++) {
        if ((mask & (1 << i)) != 0) {
            // 선택됨
        }
    }
}
```


---


## 📌 알고리즘 유형 빠른 매핑

| **문제 키워드** | **알고리즘**      |
| ------ | ------------- |
| 최단 거리  | BFS / 다익스트라   |
| 경우의 수  | 백트래킹 / DP     |
| 최소·최대  | 그리디 / 이분 탐색   |
| 연속 구간  | 투 포인터         |
| 순서 관계  | 위상 정렬         |
| 연결 여부  | DFS / 유니온 파인드 |
