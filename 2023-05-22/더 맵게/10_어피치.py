# 230524
# [PGS] 더 맵게 / 레벨2 / 18분(효율성 테스트 실패)
# https://school.programmers.co.kr/learn/courses/30/lessons/42626

def solution(scoville, K):
    # 나의 풀이
    # 효율성 테스트 실패
    '''
    answer = 0

    while len(scoville) > 1:
        scoville.sort()

        if scoville[0] < K:
            first, second = scoville.pop(0), scoville.pop(0)
            scoville.append(first + (second * 2))
            answer += 1
        else:
            return answer

    return -1 if scoville[0] < K else answer
    '''

    # 다른 풀이
    # heapq 활용
    # heap[0]에 가장 작은 원소가 있다고 해서, heap[1]에 두번째 작은 원소가 있다는 보장 없음
    # heappop() 함수로 가장 작은 원소 삭제할때마다 이진 트리 재배치를 통해 매번 새로운 최소값을 인덱스 0에 위치시키기 때문
    # 따라서, 두번째로 작은 원소 얻으려면 heap[1]로 접근하면 안된다!!
    from heapq import heapify, heappop, heappush

    answer = 0
    heapify(scoville)   # 기존 리스트를 힙으로 변환

    while scoville[0] < K:
        if len(scoville) == 1:
            return -1

        first = heappop(scoville)
        second = heappop(scoville)
        heappush(scoville, first + (second * 2))
        answer += 1

    return answer
