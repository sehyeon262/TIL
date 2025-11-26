T = int(input())

# 15번 팔씨름을 하여 8번 이상 이기는 사람이 점심 값 면제
# s[i]가 o면 소정이가 i번째 경기에서 승리, x면 패배
# 점심값 면제 받을 가능성 있으면 YES, 없으면 NO
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