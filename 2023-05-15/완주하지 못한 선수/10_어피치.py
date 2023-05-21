# 230521
# [PGS] 완주하지 못한 선수 / 레벨1 / 10분
# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    from collections import Counter

    p = Counter(participant)
    c = Counter(completion)

    for k in p.keys():
        if p[k] != c[k]:
            return k

    # 다른 풀이
    # Counter 객체 간 뺄셈 가능
    '''
    p = Counter(participant)
    c = Counter(completion)

    return list(p-c)[0]
    '''
