from itertools import combinations
T = int(input())

def cal_score(N, K, wrong_idx):
    # 튜플 -> 집합으로 바꿔 시간복잡도 O(1)로 바꿔줌
    wrong = set(wrong_idx)
    # 점수, 카운터
    score, cnt = 0, 0

    for i in range(N):
        # 틀린 문제라면
        if i in wrong:  # O(1)
            cnt = 0
        # 정답이면
        else:
            # 카운터 +1 하는데
            cnt += 1
            # 연속으로 맞춘 문제가 K보다 작으면
            if cnt < K:
                # 점수 +1
                score += 1
            # cnt == K
            else:
                # 점수 +1 후 2배, 카운터는 0   
                score += 1
                score *= 2
                cnt = 0
    return score



for test_case in range(1, T+1):
    N, M, K = map(int, input().split())

    # 최소값을 무한대로 가정
    min_score = float('inf')
    for wrong_idx in combinations(range(N), N-M):
        min_v = cal_score(N, K, wrong_idx) 
        
        if min_v < min_score:
            min_score = min_v
    
    print(f'#{test_case} {min_score}')










'''
def min_score_fast(N, M, K):
    # 틀린 문제 수
    W = N - M
    # 더블 없이 담을 수 있는 최대 정답 수
    # cap = (덩어리 수) * (덩어리당 최대 길이) = (W+1) * (K-1)
    cap = (W + 1) * (K - 1)
    # 더블이 전혀 없다 => 점수합은 정답 개수랑 같음 (연속 K를 한 번도 만들지 않으니..)
    if M <= cap:
        return M
    # 더블 없이 최대로 정답을 담은 후 넘치는 정답 spill
    spill = M - cap
    # ceil(spill / K)의 정수 연산 버전
    D = (spill + K - 1) // K   
    # (M - D*K) => 더블 이후 남은 정답들의 +1 합
    # 2*K*((1 << D) - 1) => 초반에 더블 D번을 몰아서 만든 누적 합
    return (M - D*K) + 2*K*((1 << D) - 1)
'''
