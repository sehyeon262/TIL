# 버튼 => 0 ~ 9, +, -
#  현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다.
# 채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.
# 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.
# 수빈이가 지금 보고있는 채널은 100번

N = int(input())    # 수빈이가 이동하려는 채널
M = int(input())    # 고장난 버튼 개수

no_btn = set()      # 평균적으로 O(1)
if M > 0:
    no_btn = set(map(int, input().split()))

# +, - 만 사용함
min_cnt = abs(N - 100)

for ch in range(1000001):
    str_ch = str(ch)

    # 고장난 버튼이 있나 확인
    can_press = True
    for digit in str_ch:
        if int(digit) in no_btn:
            can_press = False
            break

    if can_press:
        press_cnt = len(str_ch) + abs(ch - N)
        min_cnt = min(min_cnt, press_cnt)

print(min_cnt)

 