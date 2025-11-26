# N개의 컨테이너를 M대의 트럭으로, A->B로 운반
# 트럭 당 한 개 운반
# 트럭의 적재용량 초과하는 컨테이너는 운반할 수 없음!
# A->B로 최대 M대의 트럭이 편도로 한 번만 운행
# 화물의 총 중량이 최대가 되도록 옮길 때, 전체 무게가 얼마인지?
# 한 개도 옮길 수 없는 경우 '0' 출력!!


def drive(i, j, weight, truck):
    global max_v

    # 종료 조건
    if i == M or j == N:
        return max_v

    # 화물 실을 수 있을 때
    if truck[i] >= weight[j]:
        max_v += weight[j]
        i += 1
        j += 1
        drive(i, j, weight, truck)
    # 화물 실을 수 없을 때
    else:
        j += 1
        drive(i, j, weight, truck)


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # N: 컨테이너 수, M: 트럭 수
    weight = list(map(int, input().split()))  # N개의 컨테이너 무게
    truck = list(map(int, input().split()))  # 트럭의 적재 용량

    # 내림차순 정렬함 => 최대 중량 구하니깐 무거운 것부터 보기!
    weight.sort(reverse=True)
    truck.sort(reverse=True)

    max_v = 0

    drive(0, 0, weight, truck)
    print(f"#{test_case} {max_v}")


# ----------- 더 간단한 코드 ------------
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # N: 컨테이너 수, M: 트럭 수
    weights = list(map(int, input().split()))  # 컨테이너 무게들
    trucks = list(map(int, input().split()))  # 트럭 적재 용량들

    # 무거운 컨테이너 , 큰 트럭부터 보자
    weights.sort(reverse=True)
    trucks.sort(reverse=True)

    i = j = 0   # i: 컨테이너 인덱스, j: 트럭 인덱스
    ans = 0

    while i < N and j < M:
        if weights[i] <= trucks[j]:
            # 화물 실을 수 있으면
            ans += weights[i]
            i += 1
            j += 1
        else:
            # 화물 실을 수 없을 때 -> 더 가벼운 다음 컨테이너로
            i += 1
    print(f'#{test_case} {ans}')