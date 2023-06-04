# 230525
# [PGS] 가까운 수 / 레벨0 / 30분
# https://school.programmers.co.kr/learn/courses/30/lessons/120890

def solution(array, n):
    array.sort()
    answer, prev_gap = 0, 10000

    for num in array:
        curr_gap = abs(n - num)
        if prev_gap > curr_gap:
            answer, prev_gap = num, curr_gap
        else:
            pass

    return answer
  
    # 다른 풀이
    # n과의 차이가 적은 순으로 정렬 -> 가장 가까운 수 여러 개일 경우 더 작은 수대로 정렬
    '''
    array.sort(key=lambda x: (abs(x-n), x-n))
    return array[0]
    '''
