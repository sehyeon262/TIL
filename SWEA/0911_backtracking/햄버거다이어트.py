# 민기의 햄버거 재료에 대한 점수와 가게에서 제공하는 재료에 대한 칼로리가 주어졌을 때,
# 민기가 좋아하는 햄버거를 먹으면서도 다이어트에 성공할 수 있도록 정해진 칼로리 이하의 조합 중에서
# 민기가 가장 선호하는 햄버거를 조합해주는 프로그램을 만들어보자.
# (단 여러 재료를 조합하였을 햄버거의 선호도는 조합된 재료들의 맛에 대한 점수의 합으로 결정되고,
#  같은 재료를 여러 번 사용할 수 없으며, 햄버거의 조합의 제한은 칼로리를 제외하고는 없다.)

# 주어진 제한 칼로리 이하의 조합중에서 가장 맛에 대한 점수가 높은 햄버거의 점수 출력

# cnt: 개수, calorie: 칼로리 합, total: 점수의 합
def recur(cnt, calorie, total):
    global max_v

    # 가지치기
    if calorie > L:
        return
    
    # 모든 재료 다 봤으면 최대점수 갱신
    if cnt == N:
        max_v = max(total, max_v)
        return
    
    recur(cnt + 1, calorie + flavor[cnt][1], total + flavor[cnt][0])
    recur(cnt + 1, calorie, total) 

T = int(input())
for test_case in range(1, T+1):
    # N: 재료의 수, L: 제한 칼로리
    N, L = map(int, input().split())
    # 0열: 점수, 1열: 칼로리 
    flavor = [list(map(int, input().split())) for _ in range(N)]
    flavor.sort()   # 가지치기로 빠른 실행을 위해 높은 점수부터 계간
    max_v = 0
    recur(0, 0, 0)

    print(f'#{test_case} {max_v}')
