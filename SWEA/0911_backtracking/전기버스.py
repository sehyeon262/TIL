# 충전지를 교환하는 방식의 전기버스를 운행
# 정류장에는 교체용 충전지가 있는 교환기가 있고, 충전지마다 최대로 운행할 수 있는 정류장 수가 정해져 있다.
# 충전지가 방전되기 전에 교체하며 운행해야 하는데 교체하는 시간을 줄이려면 최소한의 교체 횟수로 목적지에 도착

def change(i, cnt):    # i: 지금 배터리를 교체하는 정류장, cnt: 현재 교환 횟수
    global min_v

    # 기저 조건
    if i >= N - 1:
        min_v = min(min_v, cnt)
        return
    # 가지치기 => 현재 교환 횟수가 최소교환보다 크거나 같으면 종료!
    if cnt >= min_v:
        return

    # i에서 새 배터리를 장착하면, i+1 ~ i+size[i] 중 아무 곳이나 다음 교체 지점으로 설정 가능
    # 멀리부터 탐색하면 더 빨리 답을 만나서 가지치기가 많이 됨
    for k in range(size[i], 0, -1):
        change(i + k, cnt + 1)


T = int(input())
for test_case in range(1, T+1):
    # N: 정류장 수, size: 정류장 별 배터리 용량
    N, *size = map(int, input().split())    # size 길이는 N - 1임
    min_v = float('inf')   # 최소한의 교환 횟수

    change(0, 0)    # 1번 정류장에서 시작 (i = 0)
    print(f'#{test_case} {min_v - 1}')  # 처음 장착은 제외함
