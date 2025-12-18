T = 10

for test_case in range(1, T+1):
    # 정점 개수
    N = int(input())
    val = [0] * (N + 1)
    # 부모 노드를 인덱스로 하는 왼쪽 자식 정점 번호 저장
    left = [0] * (N + 1)
    # 부모 노드를 인덱스로 하는 오른쪽 자식 정점 번호 저장
    right = [0] * (N + 1)

    for _ in range(N):
        lst = input().split()
        i = int(lst[0])
        x = lst[1]

        # 정점이 연산자인 경우
        if x in '+-*/':
            val[i] = x  # 연산자는 문자열로 저장함
            left[i] = int(lst[2])   # 왼쪽 자식 번호 저장함
            right[i] = int(lst[3])  # 오른쪽 자식 번호 저장함
        # 정점이 숫자인 경우 => 리프노드임
        else:
            val[i] = float(x)

    # 후위 순위 (L -> R -> T)
    def calculate(i: int):
        # 정점이 int거나 float이면 그대로 반환
        if isinstance(val[i], (int,float)):
            return float(val[i])

        # 연산자면 자식들 먼저 계산하고 연산자를 밑에 if문을 통해 계산해줌
        a = calculate(left[i])
        b = calculate(right[i])
        op = val[i]

        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return a / b

    # 루트 1부터 계산해야함
    # int를 하는 이유 => 소수점이 생기면 버리기 위해서임!
    result = int(calculate(1))
    print(f'#{test_case} {result}')