T = int(input())

# 짝을 미리 딕셔너리로 만듦
pair = {')':'(', '}':'{', ']':'[' }

for test_case in range(1, T+1):
    s = list(input())
    # 스택의 가장 상단 위치 가리키는 변수
    top = -1
    stack = [0] * 100

    result = 1
    # 문자열 하나씩 가져옴
    for x in s:
        # 여는 괄호가 존재하면 push
        if x in ['(', '{', '[']:
            top += 1
            # 해당 위치에 여는 괄호 저장
            stack[top] = x

        # 닫는 괄호인 경우
        elif x in [')', '}', ']']:
            # 스택이 비었는데 닫는 괄호가 나옴(여는 괄호가 없음) => 짝이 안 맞음
            if top == -1:
                result = 0  # 기록 중단
                break
            # 스택의 가장 위에 있는 여는 괄호가 현재 닫는 괄호와 짝이 맞으면
            if stack[top] == pair[x]:
                # 짝이 맞으면 스택에서 pop
                top -= 1
            # 짝이 맞지 않으면
            else:
                result = 0

    # 여는 괄호가 남아있으면 => 비정상임
    if top != -1:
        result = 0

    print(f'#{test_case} {result}')