# 230430
# [PGS] 문자열 밀기 / 레벨0 / 17분40초
# https://school.programmers.co.kr/learn/courses/30/lessons/120921

def solution(A, B):
    # 나의 풀이
    answer = 0

    if A == B:
        return answer

    for i in range(len(A) - 1, -1, -1):
        answer += 1
        tmp = A[i:] + A[:i]
        if tmp == B:
            return answer

    return -1
