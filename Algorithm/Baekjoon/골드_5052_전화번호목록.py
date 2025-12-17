# 전화번호 목록이 주어진다. 이때, 이 목록이 일관성이 있는지 없는지를 구하는 프로그램을 작성하시오.
# 전화번호 목록이 일관성을 유지하려면, 한 번호가 다른 번호의 접두어인 경우가 없어야 한다.
# 일관성 있는 목록인 경우에는 YES, 아닌 경우에는 NO를 출력한다.

T = int(input())

for _ in range(T):
    lst = []
    N = int(input())
    for _ in range(N):
        lst.append(input())

    lst.sort()
    
    # 일관성 있다고 가정
    res = True 
    for i in range(N-1):
        a = lst[i]      # 앞
        b = lst[i + 1]  # 뒤

        # 뒤 전화번호의 앞부분이 앞 전화번호와 같음 => 접두어 존재!
        if b[:len(a)] == a:
            res = False 
            break
    
    print("YES" if res else "NO")