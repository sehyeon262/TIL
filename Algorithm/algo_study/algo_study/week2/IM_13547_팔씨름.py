T = int(input())

for test_case in range(1, T+1):
    s = list(input())

    # 'o' 횟수
    cnt = 0
    # 'o'의 개수를 셈
    for i in range(len(s)):
        if s[i] == 'o':
            cnt += 1
    # 'o'의 개수를 센 후 8개 이상이면 이미 면제임 => YES
    if cnt >= 8:
        result = 'YES'
    # 'o'의 개수가 8개 미만인 경우
    else:
        # 남은 팔씨름 경기가 8번 이기기까지 남은 횟수보다 많으면 면제 확률 있음!!
        if 15 - len(s) >= 8 - cnt:
            result = 'YES'
        else:
            result = 'NO'

    print(f'#{test_case} {result}')
    