T = 10

for test_case in range(1, T + 1):
    N = int(input())  # 덤프 횟수
    boxes = list(map(int, input().split()))  # 박스들의 높이

    # 평탄화 작업 N번 반복
    for _ in range(N):
        # 최고/최저 높이 위치 찾기
        max_idx = min_idx = 0  # 0번 위치가 가장 높,낮다고 가정

        for i in range(100):
            if boxes[i] > boxes[max_idx]:
                max_idx = i
            if boxes[i] < boxes[min_idx]:
                min_idx = i

        # 반복문을 다 돌고 난 후, 최고/최저 위치 구했으니 덤프
        boxes[max_idx] -= 1
        boxes[min_idx] += 1

        # 주어진 덤프 횟수 이내에 평탄화가 완료 조건
        # 최고점, 최저점 높이 차가 1 이내 => break
        if boxes[max_idx] - boxes[min_idx] <= 1:
            break

    # 평탄화가 끝나고 나서 한 번 더 최고/최저 위치 찾기
    max_idx = min_idx = 0

    for i in range(100):
        if boxes[i] > boxes[max_idx]:
            max_idx = i
        if boxes[i] < boxes[min_idx]:
            min_idx = i
    print(f'#{test_case} {boxes[max_idx] - boxes[min_idx]}')
