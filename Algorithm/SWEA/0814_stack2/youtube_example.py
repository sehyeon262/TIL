'''
(6+5*(2-8)/2)
6528-*2/+
'''

stack= [0] * 100
top = -1

# 밖에 있을 때의 우선 순위 (클 수록 높음)
icp = {'(' : 3, '*' : 2, '/' : 2, '+' : 1, '-' : 1}
# 스택 안에 있을 때의 우선 순위 (클 수록 높음)
isp = {'(' : 0, '*' : 2, '/' : 2, '+' : 1, '-' : 1}

infix = '(6+5*(2-8)/2)'
postfix = ''

for token in infix:
    # 피연산자면 후위식에 추가
    if token not in '(+-*/)':
        postfix += token
    # 토큰이 닫는 괄호면 여는 괄호를 만날 때까지 pop
    elif token == ')':
        # 스택에 top이 여는 괄호가 아니면 다 꺼내
        while top > -1 and stack[top] != '(':
            top -= 1
            postfix = stack[top + 1]
        # 전체 수식이 괄호로 둘러 쌓이지 않은 경우 대비
        if top != -1:
            # '(' 여는 괄호 버림...
            top -= 1

    # 연산자인 경우 (우선순위 따짐)
    else:
        # 비어있거나 더 높으면 집어넣어
        if top == -1 or isp[stack[top]] < icp[token]:
            top += 1
            stack[top] = token
        # 토큰과 같거나 더 높으면
        elif isp[stack[top]] >= icp[token]:
            while top > -1 and isp[stack[top]] >= icp[token]:
                postfix += stack[top]
                top -= 1
            # push
            top += 1
            stack[top] = token
    print(postfix, stack)

