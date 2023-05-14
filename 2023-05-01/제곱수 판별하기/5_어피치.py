# 230507
# [PGS] 제곱수 판별하기 / 레벨0 / 3분30초
# https://school.programmers.co.kr/learn/courses/30/lessons/120909

def solution(n):
    from math import sqrt

    x = sqrt(n)
    return 1 if x % int(x) == 0 else 2  # 정수 판별 위해 int(x) 대신 1 사용 가능
    
    # 다른 풀이
    # 0.5 제곱 결과 구한 후, 정수 판별 위해 1로 나눈 나머지 확인
    # return 1 if (n ** 0.5) % 1 == 0 else 2
