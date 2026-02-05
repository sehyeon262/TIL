# 상근이의 동기는 모두 N명
# 이 학생들의 학번은 모두 1부터 N까지이다. 상근이의 학번은 1이다.
# 리스트를 바탕으로 결혼식에 초대할 사람의 수를 구하는 프로그램을 작성
# 친구의 친구까지만 초대

from collections import deque

n = int(input())  # 상근이 동기 수
m = int(input())  # 리스트 길이

graph = [[] for _ in range(n + 1)]

for _ in range(m):
  i, j = map(int, input().split())
  graph[i].append(j)
  graph[j].append(i)

visited = [0] * (n + 1)
visited[1] = 1


q = deque()
q.append((1, 0))
cnt = 0

while q:
  cur, dist = q.popleft()

  if dist >= 2:
    continue

  for nxt in graph[cur]:
    if not visited[nxt]:
      visited[nxt] = 1
      cnt += 1
      q.append((nxt, dist + 1))

print(cnt)