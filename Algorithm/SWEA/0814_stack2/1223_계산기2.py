# 후위 표기 변환
def infix_to_postfix(expr):
    stack = []
    result = ''
    icp = {'(':3, '*':2, '/':2, '+':1, '-':1}
    isp = {'(':0, '*':2, '/':2, '+':1, '-':1}

    for x in expr:
        if x.isdigit():  # 피연산자
            result += x
        elif x == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()  # '(' 제거
        else:  # 연산자 or '('
            while stack and isp[stack[-1]] >= icp.get(x, 0):
                result += stack.pop()
            stack.append(x)
    while stack:
        result += stack.pop()
    return result

# 후위 표기 계산
def eval_postfix(s):
    stack = []
    for x in s:
        if x.isdigit():
            stack.append(int(x))
        else:
            b = stack.pop()
            a = stack.pop()
            if x == '+':
                stack.append(a + b)
            elif x == '-':
                stack.append(a - b)
            elif x == '*':
                stack.append(a * b)
            elif x == '/':
                stack.append(a // b)  # 정수 나눗셈
    return stack[0]

# 입력 처리
T = int(input())  # 테스트 케이스 수
for tc in range(1, T + 1):
    s = input()
    postfix_expr = infix_to_postfix(s)
    result = eval_postfix(postfix_expr)
    print(f'#{tc} {result}')
