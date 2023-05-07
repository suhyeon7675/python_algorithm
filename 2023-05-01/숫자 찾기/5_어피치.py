# 230507
# [PGS] 숫자 찾기 / 레벨0 / 3분55초
# https://school.programmers.co.kr/learn/courses/30/lessons/120904

def solution(num, k):
    i = str(num).find(str(k))
    return i + 1 if i >= 0 else i
