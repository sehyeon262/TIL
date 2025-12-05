T = int(input())

for test_case in range(1, T+1):
    # N명의 사람, M초의 시간, K개의 붕어빵
    N, M, K = map(int, input().split())
    arrive = list(map(int, input().split()))

    # 온 순서대로 확인하기 위해 정렬함 
    arrive.sort()

    possible = True

    for i in range(N):  
        t = arrive[i] 
        # t초까지 만들어진 붕어빵 총 개수 
        # 완성된 판 수 * 판당 개수         
        bread = (t // M) * K  
        # 지금까지 온 손님 수 == 붕어빵이 총 몇 개 필요한가?   
        customer = i + 1  

        # 손님 수보다 붕어빵이 부족하면 불가능함           
        if bread < customer:        
            possible = False
            break

    if possible:
        print(f"#{test_case} Possible")
    else:
        print(f"#{test_case} Impossible")

'''
[다른 방법]

T = int(input())

for test_case in range(1, T+1):
    # N명의 사람, M초의 시간, K개의 붕어빵
    N, M, K = map(int, input().split())
    arrive = list(map(int, input().split()))
    
    # 가장 늦게 도착하는 손님 시간 구함
    max_t = max(arrive)

    # t초에 도착하는 손님 수를 lst[t]에 저장함
    lst = [0] * (max_t + 1)
    for c in arrive:
        lst[c] += 1

    # 현재 붕어빵 재고
    bread = 0
    possible = True

    # 0초부터 가장 늦게 오는 손님시간까지 반복함
    for t in range(max_t + 1):
        # t가 M의 배수일 때 붕어빵 K개 생산함
        if t != 0 and t % M == 0:
            bread += K
        
        # t초에 손님이 오면 붕어빵 소비함
        bread -= lst[t]

        # 만약 재고가 부족하면 불가능ㅜ
        if bread < 0:
            possible = False
            # 더이상 확인할 필요 없으므로 끝냄
            break
    
    if possible:
        print(f'#{test_case} Possible')
    else:
        print(f'#{test_case} Impossible')
'''