# 최대힙 (array 기반, 인덱스 1부터 사용)
# - 규칙: 부모 ≥ 자식  → 루트(1번 인덱스)가 항상 최대값
# - parent(i) = i // 2, left(i) = 2*i, right(i) = 2*i + 1
# - 삽입(enq): 끝에 넣고 부모보다 크면 위로 올림(sift-up)
# - 삭제(deq): 루트 반환 후, 마지막 값을 루트로 올리고 더 큰 자식과 교환하며 아래로 내림(sift-down)

def enq(n):
    global last, heap
    # 1) 힙의 맨 끝(새로운 마지막 위치)에 값 추가
    last += 1
    heap[last] = n

    # 2) 위로 끌어올리기(sift-up): 부모보다 크면 교환
    c = last                 # c: 현재 노드(자식)의 인덱스
    p = c // 2               # p: 부모 인덱스(1이면 부모는 0 → 없음)
    # p가 0이 아니고, 부모값 < 자식값 이면 최대힙 규칙 위반 → 교환
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]  # 부모/자식 자리 바꿈
        c = p                                 # 한 레벨 위로 올라감
        p = c // 2                            # 새 부모 계산

def deq():
    global last, heap
    # 힙이 비어있다면 예외를 던지는 것이 안전하지만
    # 여기선 호출 측에서 last > 0일 때만 부른다고 가정
    tmp = heap[1]            # 1) 루트(최대값) 백업

    # 2) 마지막 값을 루트로 올리고, 힙 크기 줄이기
    heap[1] = heap[last]
    last -= 1

    # 3) 아래로 내려보내기(sift-down)
    p = 1                    # p: 현재 부모 인덱스
    c = p * 2                # c: 왼쪽 자식 인덱스(먼저 왼쪽부터 확인)
    # 자식이 하나라도 있으면 계속
    while c <= last:
        # 오른쪽 자식이 존재하고, 오른쪽 자식이 더 크면 비교 대상을 오른쪽으로 변경
        if c + 1 <= last and heap[c] < heap[c + 1]:
            c += 1  # 이제 c는 두 자식 중 더 큰 자식

        # 부모가 더 작다면(규칙 위반) 부모/자식 교환 후 한 레벨 아래로
        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = p * 2        # 새 부모의 왼쪽 자식부터 다시 검사
        else:
            # 부모가 더 크거나 같으면 규칙 만족 → 종료
            break

    return tmp               # 처음 백업한 최대값 반환

# ===== 사용 예시 =====
heap = [0] * 100  # 0번 인덱스는 비워두는 용도(계산 편의)
last = 0          # 힙에 저장된 원소 수 (= 마지막 인덱스)

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)

# 최대값부터 하나씩 꺼내 출력 → 7 6 5 4 3 2
while last:
    print(deq())
