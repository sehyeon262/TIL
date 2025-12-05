import sys
sys.stdin = open("sample_input.txt", "r")

# 핵심: 남은 풍선의 집합(상태)만 알면 됨!!
# - mask라는 비트마스크(정수)로 표현함
# - 인덱스 i 풍선이 터졌으면 mask의 i번쨰 비트를 1, 아직 살아있으면 0
# ex) N = 5 --> mask = 0b01010 (인덱스 1, 3이 터졌고(1), 0, 2, 4는 살아 있음(0))

def solve(balls):
    """
    balls[i] : i번째(0-based) 풍선에 적힌 숫자
    규칙
      - 양옆 살아있으면: 왼값 * 오른값
      - 한쪽만 살아있으면: 그쪽 값
      - 양옆 다 없으면(혼자 남음): 자기 값
    목표
      - 모든 풍선을 터뜨릴 때까지 점수를 더했을 때의 '최댓값'
    아이디어
      - 상태를 '어떤 풍선들이 이미 터졌는지'로 정의 → 비트마스크 mask
      - dp(mask) = '현재 mask(=터진 집합) 상태에서 앞으로 얻을 수 있는 최대 점수'
      - 아직 안 터진 i를 하나 골라 터뜨림 → 이득(gain) + dp(다음 mask) 의 최댓값
    """

    N = len(balls)
    # 모든 풍선이 터진 상태
    full = (1 << N) - 1

    # memo[mask] = dp(mask) 값 저장, -1이면 아직 계산 안 함
    memo = [-1] * (1 << N)

    def dp(mask: int):
        '''
        mask의 i번째 비트가 1이면 'i번 풍선은 이미 터졌다'는 뜻.
        예) mask = 0b01010 이면 1번, 3번이 터진 상태.
        반환값: 이 상태에서 최대로 얻을 수 있는 점수
        '''
        # 모두 터진 상태면 더 얻을 점수가 없음 -> 0
        if mask == full:
            return 0
        
        # 이미 계산한 상태면 재사용(메모이제이션)
        if memo[mask] != -1:
            return memo[mask]
        
        best = 0    # 이상태에서 가능한 선택들 중 최댓값을 저장

        # 아직 안 터진 풍선 i를 하나 선택해서 터트려 본다
        for i in range(N):
            # i번쨰 비트 터졌는지 확인 (1이면 터진 거, 0이면 안 터진 거)
            # ex) i = 3을 검사하고 싶을 때
            # mask = 01011 --> (mask >> 3) = 00001 => 오른쪽으로 3칸 이동
            if (mask >> i) & 1:
                # i가 이미 터졌으면 스킵!
                continue

            # ------- i의 이웃 찾기 -------
            # 왼쪽 이웃 중에서 아직 안 터진 첫 번째
            left = i - 1
            while left >= 0 and ((mask >> left) & 1):
                # left가 터졌으면 더 왼쪽으로 이동
                left -= 1
            
            right = i + 1
            while right < N and ((mask >> right) & 1):
                # right가 터졌으면 더 오른쪽으로 이동
                right += 1
            
            # ------ 점수 적용 하자 -------
            if left >= 0 and right < N:     # 양쪽 모두 존재
                score = balls[left] * balls[right]
            elif left >= 0:                 # 왼쪽만 존재
                score += balls[left]
            elif right < N:                 # 오른쪽만 존재
                score = balls[right]    
            else:                           # 양쪽 다 없음 (혼자 남음)
                score = balls[i]

            # i를 터트린 후 새 상태로 진행함 
            # => i번째 비트를 1로 설정해서 i번 풍선을 터트렸다고 업데이트하는 연산임
            # or(|)은 1이 하나라도 있으면 1로 바꿔주기 때문!
            next_mask = mask | (1 << i)

            # 현재 선택(i)을 했을 때 얻는 총 점수 = 이번 이득 + 다음 상태의 최댓값
            candidate = score + dp(next_mask)

            # 여러 선택 중 최대값 갱신
            if candidate > best:
                best = candidate
        
        # 계산 끈 => 메모에 저장 후 반환
        memo[mask] = best
        return best

    # 아직 아무 풍선도 안 터진 상태(mask = 0)에서의 최댓값이 정답
    return dp(0)


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    balls = list(map(int, input().split()))
    print(f'#{test_case} {solve(balls)}')

