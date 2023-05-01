# 230430
# [PGS] 종이 자르기 / 레벨0 / 6분 50초
# https://school.programmers.co.kr/learn/courses/30/lessons/120922

def solution(M, N):
    # M이 1이 되기 위해 M-1 번의 가위질 필요. N번 반복
    return (M - 1) * N + (N - 1)    # (M * N) - 1
