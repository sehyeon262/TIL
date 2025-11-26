'''
- 길이가 N인 물웅덩이
- 개구리가 점프할 수 있는 거리는 최대 K
- 뛸 수 있는 나뭇잎이 없더라도, 개구리는 무조건 K만큼 점프를 하고 물에 빠지게 된다
- 물웅덩이의 가장 왼쪽에는 항상 나뭇잎이 떠있다 -> 가장 왼쪽에서 점프 시작
- 나뭇잎이 있는 곳은 1, 없는 곳은 0
- 개구리가 최대로 이동한 거리가 얼마인가?
'''

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    frog = 1  # 개구리 현재 위치

    while frog < N:
        next = min(frog + K, N)

        # 가장 먼 1 찾기
        for i in range(next, frog, -1):
            if arr[i] == 1:
                frog = i
                break
        else:
            # 구간에서 나뭇잎이 없으면 다음 최대로 갈 수 있는데 까지 가고 종료!
            frog = next
            break
    print(f'#{test_case} {frog}')



