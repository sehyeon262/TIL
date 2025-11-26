# 스택 밖에 있을 때 우선순위
icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
# 스택 안 에 있을 때 우선순위
isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

# 중위 표기식을 후위 표기식으로 바꾸기
# infix: 중위 표기식 / N : 식의 길이(토큰 개수)
def get_postfix(infix, N):
    # 결과를 출력할 후위 표기식
    postfix = ''

    stack = []

    # 중위 표기식에서 글자(토큰) 하나씩 떼어 와서 후위 표기식 만듦
    for token in infix:
        # 토큰이 피연산자인 경우
        if token not in '(+-/*)':
            # 후위표기식에 그대로 피연산자를 쓴다.(출력한다.)
            postfix += token
        # 토큰이 연산자인 경우
        else:
            # 먼저 봐야하는 연산자 => ')'
            # 토큰이 ')' 라면
            if token == ')':
                # '(...)' 안에 있는 모든 연산자가 먼저 계산이 되어야 한다.
                # 스택 안에 '('를 만날 때까지 모든 연산자를 꺼내 쓴다.
                while stack:
                    # 연산자를 하나 꺼내보기
                    operator = stack.pop()
                    # 꺼낸게 '(' 라면 연산자 꺼내기 중단
                    if operator == '(':
                        break
                    # 여는 괄호가 아니면 계속 식에 출력
                    postfix += operator

        # 토큰이 닫는 괄호가 아닌 다른 연산자였다면
            else:
                # 스택 꼭대기에 있는 연산자의 우선순위와 => isp[stack[-1]]
                # 현재 토큰의 우선순위를 비교 => icp[token]
                # 누가 더 우선순위가 높은지 확인
                # 우선순위가 높은 친구는 먼저 계산이 되어야 하니깐 출력하기

                # 스택 안에 현재 token보다 우선순위가 같거나 높은 연산자는 다 꺼내쓴다
                while stack and icp[token] <= isp[stack[-1]]:
                    # 꺼내서 결과에 이어붙이기
                    postfix += stack.pop()

                # 토큰의 우선순위가 스택의 꼭대기에 있는 연산자의 우선순위보다 높았다면
                # 또는 스택이 비어있다면
                stack.append(token)

    # 모든 토큰을 확인 한 후에 스택에 남아있는 연산자는 그대로 차례대로 출력
    while stack:
        postfix += stack.pop()

    return postfix








