# 230507
# [PGS] n의 배수 고르기 / 레벨0 / 2분30초
# https://school.programmers.co.kr/learn/courses/30/lessons/120905

def solution(n, numlist):
    answer = []

    for num in numlist:
        if num % n == 0:
            answer.append(num)

    return answer
  
    # list comprehension 사용한 풀이
    # return [num for num in numlist if (num % n) == 0]
