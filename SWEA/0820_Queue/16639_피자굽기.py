from collections import deque
T = int(input())

# 맨 앞 피자 꺼내서 치즈를 반으로 줄임 → 남았으면 맨 뒤로 보내고, 0이면 빼고 다음 피자 투입

for test_case in range(1, T+1):
    # N: 동시에 넣을 수 있는 피자 개수, M: 피자 개수
    N, M = map(int, input().split())
    # 각 피자의 치즈의 양
    cheese = list(map(int, input().split()))

    # 큐에 (피자번호, 치즈량) 저장함
    q = deque()
    # 다음에 넣을 피자의 인덱스
    next_idx = N

    for i in range(N):
        q.append((i+1, cheese[i]))

    while len(q) > 1:
        # 맨 앞 피자를 꺼냄
        p_num, c = q.popleft()
        c //= 2

        # 피자 치즈가 다 녹았고,
        if c == 0:
            # 남은 피자가 있으면 그 자리에 새로 투입
            if next_idx < M:
                q.append((next_idx + 1, cheese[next_idx]))
                next_idx += 1
            # 없으면 그냥 빈자리로 두고, 큐 길이만 줄어듦
        else:
            # 치즈가 남았으면 뒤로 보냄(회전)
            q.append((p_num, c))

    # 마지막 남은 피자의 번호 출력
    last_piz = q[0][0]
    print(f'#{test_case} {last_piz}')
