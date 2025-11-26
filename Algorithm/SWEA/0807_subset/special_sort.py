T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    for i in range(N):
        idx = i  # 기준 인덱스
        # 인덱스가 짝수면 남은 리스트들 중 최대값 대입
        if i % 2 == 0:
            max_num = arr[i]  # 현재 자리가 최대값이라 가정
            for j in range(i, N):
                if max_num < arr[j]:
                    max_num = arr[j]
                    idx = j  # 최대값의 인덱스 저장
            arr[i], arr[idx] = arr[idx], arr[i]  # 현재 자리와 최대값 자리 교환
        # 인덱스가 홀수면 남은 리스트들 중 최소값 대입
        else:
            min_num = arr[i] # 현재 자리가 최소값이라 가정
            for j in range(i, N):
                if min_num > arr[j]:
                    min_num = arr[j]
                    idx = j  # 최소값의 인덱스 저장
            arr[i], arr[idx] = arr[idx], arr[i]  # 현재 자리와 최소값 자리 교환

    print(f'#{tc}', *arr[:10])

