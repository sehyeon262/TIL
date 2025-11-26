# T = int(input())
# for test_case in range(1, T+1):
#     # N: 물웅덩이 길이, K: 개구리 최대 점프 칸 수
#     N, K = map(int, input().split())
#     pond = [0] + list(map(int, input().split()))
#
#     frog = 1    # 개구리 현재 위치
#
#     while frog < N:
#         # 다음에 점프 할 위치
#         next = frog
#
#         # 개구리가 점프 가능한 범위 1 ~ K
#         for i in range(1, K+1):
#             # i만큼 점프한 위치가 물웅덩이를 벗어나면 물웅덩이 길이가 최대 이동거리
#             if frog + i > N:
#
#
#             # 다음에 i만큼 점프한 위치에 나뭇잎이 있다면 점프 가능
#             if pond[frog + i] == 1:
#                 next = frog + i
#                 break
#         else:
#             # 반복문이 중단된 적 없으면 점프할 곳 못 찾음
#             # 현재 위치 +K가 마지막 점프 위치가 되고 점프 종료
#             frog = frog + K
#             break
#         # 다음 위치를 현재위치로 최신화
#         frog = next
#
#     print(f'#{test_case} {frog}')

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    lips = list(map(int, input().split()))

    pos = 0
    while pos < N - 1:
        next_pos = min(pos + K, N - 1)

        # pos ~ next_pos 구간에서 가장 먼 나뭇잎 찾기
        for i in range(next_pos, pos, -1):
            if lips[i] == 1:
                pos = i
                break
        else:
            # 나뭇잎이 없으면 그냥 next_pos까지 가고 종료
            pos = next_pos
            break

    print(f"#{tc} {pos + 1}")