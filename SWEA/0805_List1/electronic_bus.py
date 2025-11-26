T = int(input())

for test_case in range(1,T+1):
    # K: 한 번 충전으로 최대한 이동할 수 있는 정류장 수
    # N: 종점 정류장
    # M: 충전기가 설치된 정류장
    K,N,M = map(int, input().split())
    M_num = list(map(int, input().split()))  # 충전소가 설치된 위치 리스트
    lst = [0] * N

    # 조건
    # 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력
    # 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0 출력

    current = 0  # 현재 위치
    count = 0  # 충전 횟수
    while current + K < N:
        # K 이내에서 가장 먼 곳부터 충전소 찾음
        # 최소 충전 횟수를 찾으므로 최대한 K만큼 간 후 충전소가 존재하는 것이 좋음!!
        for i in range(current+K , current, -1):
            # K 이내에 정류장이 존재한다면 정류장으로 이동
            if i in M_num:
                current = i
                count += 1
                break
        # 없으면 반복문 빠져나와 0 출력
        else:
            count = 0
            break

    print(f'#{test_case} {count}')
