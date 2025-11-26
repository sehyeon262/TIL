# i번 째 버스 노선은 번호가 Ai이상, Bi이하인 모든 정류장만을 다님
T = int(input())

# 정류장마다 몇 개의 노선이 지나는지 미리 리스트 만들어놓고, 노선 구간마다 count 올려줌

for test_case in range(1, T+1):
    N = int(input())  # 버스 노선 수
    stop_count = [0] * 5001  # 정류장 번호 1 ~ 5000

    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            stop_count[i] += 1

    P = int(input())  # 조회할 정류장 수
    result = []

    # 조회할 정류장 번호에 대해 값 수집
    for _ in range(P):
        C = int(input())
        result.append(stop_count[C])

    # 리스트를 언패킹하여 출력
    print(f'#{test_case}', *result)