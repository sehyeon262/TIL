T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))

    # 현재 가장 큰 나무 높이로 맞춤
    max_h = max(trees)

    # 각 나무가 얼마나 모자라는지 리스트
    diff = [max_h - h for h in trees]

    # 키워야 할 나무들의 총 합
    s = sum(diff)
    # 홀수 차이(= 홀수 날에 꼭 필요한 +1)의 개수
    ones = sum(d % 2 for d in diff)

    days = 0
    while True:
        # D일 동안 홀수날 짝수날 개수
        # 홀수날 => 5일 => (5+1) // 2 = 3개
        odd_days = (days + 1) // 2  
        # 짝수날 => 3일 => 3 // 2 = 1개
        even_days = days // 2       
        # D일 동안 가능한 총 성장량 = 홀수 날 개수 + 짝수 날 개수 * 2
        capacity = odd_days + (even_days * 2)

        # 홀수 날은 최소 ones개 필요
        # 총 성장량은 최소 s이상 필요
        if odd_days >= ones and capacity >= s:
            break
        # 위 조건 만족 못하면 날짜 하루 늘임
        days += 1

    print(f'#{test_case} {days}')