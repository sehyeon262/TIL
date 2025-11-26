from collections import deque

T = 10

for test_case in range(1, T+1):
    tc = int(input())
    data = list(map(int, input().split()))
    q = deque(data)  # 길이 8
    # 뺄 숫자를 저장할 변수, 초기값은 1입니다.
    minus = 1

    # 암호 생성 과정이 끝날 때까지 무한 반복함
    while True:
        # 큐의 맨 앞에서 숫자 꺼내서 minus 만큼 뺌
        x = q.popleft() - minus
        # 계산 결과가 0보다 작거나 같으면
        if x <= 0:
            # 큐의 맨 뒤에 0을 추가하고 종료!
            q.append(0)
            break
        # 계산 결과가 0 보다 크면, 그 값을 큐의 맨 뒤에 추가함
        q.append(x)
        # minus를 5로 나눈 나머지에 1을 더하면 1~5 사이의 숫자가 순환함
        minus = 1 + (minus % 5)

    print(f'#{tc}', *q)

