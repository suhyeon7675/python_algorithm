# 230517
# [PGS] 한 번만 등장한 문자 / 레벨0 / 14분40초
# https://school.programmers.co.kr/learn/courses/30/lessons/120896

def solution(s):
    # 나의 풀이
    answer = ''

    s = ''.join(sorted(s))
    while s:
        if s[0] not in s[1:]:
            answer += s[0]
        s = s.replace(s[0], '')

    return answer

    # 다른 풀이
    # count() 함수 사용
    # return ''.join(sorted([ch for ch in set(s) if s.count(ch) == 1]))
