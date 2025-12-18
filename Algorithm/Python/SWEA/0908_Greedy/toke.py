# 0시부터 다음날 0시 이전까지 A도크의 사용신청을 확인해 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면
# 최대 몇 대의 화물차가 이용할 수 있는지 알아내 출력하는 프로그램
# 신청서에는 작업 시작 시간과 완료 시간이 매시 정각을 기준으로 표시

# 그리디는 "끝나는 시간이 가장 빠른 작업부터" 고름
# => 앞 작업이 빨리 끝날수록 뒤에 더 많은 작업 배치 가능

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]

    # e를 기준으로 오름차순 정렬 -> 같으면 s가 빠른 순(오름차순)으로 정렬
    arr.sort(lambda x: (x[1], x[0]))  
    cnt = 0
    end = 0  # 이전에 선택한 작업의 종료 시각

    for s, e in arr:
        if s >= end:    # 이전 종료 시각보다 크거나 같으면 +1
            cnt += 1
            end = e     # 마지막으로 끝난 시간을 end로 갱신함!

    print(f'#{test_case} {cnt}')