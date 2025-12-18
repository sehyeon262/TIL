T = int(input())

for tc in range(T):

    N = int(input())

    arr = list(map(int, input().strip()))

    max_count = 0
    count = 0

    for i in range(N):
        if arr[i] == 1:
            count += 1

            if i == N - 1:
                if max_count < count:
                    max_count = count

        else:
            if max_count < count:
                max_count = count
            count = 0

    print(f'#{tc + 1} {max_count}')
