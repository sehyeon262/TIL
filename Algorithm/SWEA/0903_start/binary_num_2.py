# 0보다 크고 1미만인 십진수 N을 이진수로 바꾸려고 한다.
# N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력
# 13자리 이상이 필요한 경우에는 ‘overflow’를 출력
# 10진수 -> 2진수

T = int(input())

for test_case in range(1, T+1):
    decimal = float(input())

    result = []
    # 2로 계속 곱하다가 남는 소수가 0이면 종료
    # 10으로 나눴을때의 몫을 결과값에 더함
    for _ in range(12):
        decimal *= 2
        # 소수부가 0이 되어 없으면 종료!
        if decimal == 0:
            break

        if decimal >= 1:
            result .append('1')
            decimal -= 1
        else:
            result.append('0')

    # 12자리 다 써도 소수부가 남아있으면 overflow!
    if decimal != 0:
        print(f'#{test_case}', "overflow")
    else:
        print(f'#{test_case} {"".join(result)}')
