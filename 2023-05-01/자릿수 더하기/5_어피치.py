# 230507
# [PGS] 자릿수 더하기 / 레벨0 / 2분30초
# https://school.programmers.co.kr/learn/courses/30/lessons/120906

def solution(n):
    answer = 0

    for e in str(n):
        answer += int(e)

    return answer
  
    # sum() 함수 사용한 풀이
    # return sum(int(e) for e in str(n))
