# ---------------------------------------------
# [문제 접근: 메모이제이션(DFS Top-down)]
# - 상태: (숫자판 문자열 state, 남은 교환 횟수 k_left)
# - 값:  해당 상태에서 만들 수 있는 최대 정수값
# - 캐시: memo[(state, k_left)] = 최대값
# ---------------------------------------------

# 1) 입력
# - 테스트케이스 T를 읽는다.
# - 각 케이스마다 숫자판은 문자열 그대로, 교환 횟수 K는 정수로 받는다.
#   예) num_str, K = input().split() ; K = int(K)
# - 문자열 그대로 다루는 이유: 자릿수 교환이 쉽고, 해시 키로 쓰기 편함.

# 2) 보조 함수: swap
# - 인자: 문자열 s, 인덱스 i, j (i<j)
# - 동작: s의 i, j 자리를 맞바꾼 새로운 문자열을 만들어 반환.
# - 구현 팁: list로 바꿔서 교환 후 ''.join
# - 주의: i==j면 그대로 s 반환(불필요한 재귀 방지)

# 3) DFS 함수 설계: dfs(state, k_left)
# - 기저 사례:
#   - k_left == 0 이면 더 못 바꾼다 → int(state) 반환.
# - 캐시 조회:
#   - (state, k_left)가 memo에 있으면 즉시 반환(중복 계산 방지).
# - 전개:
#   - max_val = 0 로 시작.
#   - 길이 L = len(state).
#   - 모든 자리쌍 (i, j) (0 ≤ i < j < L)을 순회하면서:
#       * nxt = swap(state, i, j)
#       * cand = dfs(nxt, k_left - 1)
#       * max_val = max(max_val, cand)
# - 메모/반환:
#   - memo[(state, k_left)] = max_val
#   - return max_val

# 4) 최종 정답
# - memo = {} (딕셔너리) 한 개 생성.
# - ans = dfs(num_str, K)
# - 출력 형식 맞춰서 print

# 5) 주의/가지치기(선택)
# - 숫자판에 중복 자릿수가 있을 경우, 남은 교환을 같은 숫자끼리 소모해도 값이 유지됨.
#   → 별도 처리를 안 해도 DFS가 자동으로 최대값을 찾지만,
#     "이미 memo에 있으면 반환"으로 중복 경로 폭발을 막는 것이 핵심.
# - 선행 0(리딩 제로)을 생성해도 문제 조건상 허용된다면 따로 막지 말 것.
# - 비교는 int로 하는 것이 안전(길이가 같아 문자열 사전순==숫자크기이지만, 혼동 방지 차원).
# - 키는 반드시 (state, k_left) 튜플로!  state만 키로 쓰면 남은 교환 수가 달라 미래가 달라져서 오답.

# 6) 복잡도 감각
# - 자릿수 ≤ 6, K ≤ 10 범위에서는 memo가 실질 탐색 공간을 크게 줄여서 충분히 통과.
# - 같은 state가 여러 경로로 만들어져도, memo가 한 번만 계산하게 해줌.

# 7) 간단 체크 시나리오
# - num_str="94", K=1 → 가능한 교환 1회: "49" → 최대 94 vs 49 중 94? (교환을 반드시 해야 한다면 49)
#   * 문제 정의가 “정확히 K회”라면 마지막 레벨의 값이 정답.
# - num_str="3288", K=2 → 중복 8 덕분에 최대 만든 뒤 동일값 유지하며 남은 교환 소모 가능.
# - num_str가 이미 최대 배치라도 K가 남아 있으면, DFS가 홀짝/중복 이슈까지 포함해 최적값 반환.

# 8) 구현 순서 가이드
# - 입력 파싱 → memo 준비 → swap 구현 → dfs 구현(기저-캐시-전개-메모) → 호출/출력


# SWEA 1244: 최대 상금 (메모이제이션 DFS)

import sys

def solve_case(num_str: str, K: int) -> int:
    L = len(num_str)
    memo = {}

    # 모든 (i, j) 자리쌍 미리 준비
    pairs = [(i, j) for i in range(L) for j in range(i + 1, L)]

    def dfs(state: str, k_left: int) -> int:
        # 더 이상 교환 못 하면 현재 숫자가 결과
        if k_left == 0:
            return int(state)

        key = (state, k_left)
        if key in memo:
            return memo[key]

        max_val = 0

        # 같은 상태로 여러 번 들어가는 걸 줄이기 위한 중복 제거
        seen_next = set()

        s_list = list(state)
        for i, j in pairs:
            t = s_list[:]          # 자리 교환용 복사
            t[i], t[j] = t[j], t[i]
            nxt = ''.join(t)

            # 같은 모양으로 가는 경로는 한 번만 확장
            if nxt in seen_next:
                continue
            seen_next.add(nxt)

            cand = dfs(nxt, k_left - 1)
            if cand > max_val:
                max_val = cand

        memo[key] = max_val
        return max_val

    return dfs(num_str, K)


# ---------- 입출력 ----------
input = sys.stdin.readline
T = int(input().strip())
for tc in range(1, T + 1):
    num_str, K = input().split()
    K = int(K)
    ans = solve_case(num_str, K)
    print(f"#{tc} {ans}")
