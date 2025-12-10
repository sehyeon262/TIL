# 1차원 좌표계 위에 선분 N개가 있다. 
# 선분이 최대로 겹쳐있는 부분의 겹친 선분의 개수를 구해보자. 
# 선분의 끝 점에서 겹치는 것은 겹치는 것으로 세지 않는다.


# N 너무 크면 시간초과 이슈 => 빠른 입력 사용
import sys
input = sys.stdin.readline

N = int(input())
lines = []

for _ in range(N):
    s, e = map(int, input().split())
    lines.append((s, 1)) # 시작점 -> cnt += 1
    lines.append((e, -1)) # 끝점 -> cnt -= 1

lines.sort()
res = 0
cnt = 0

for _, point in lines:
    cnt += point
    res = max(res, cnt)

print(res)