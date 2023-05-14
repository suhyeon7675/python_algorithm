# 230507
# [PGS] 배열의 유사도 / 레벨0 / 2분
# https://school.programmers.co.kr/learn/courses/30/lessons/120903

def solution(s1, s2):
    answer = 0

    for element in s1:
        if element in s2:
            answer += 1

    return answer
