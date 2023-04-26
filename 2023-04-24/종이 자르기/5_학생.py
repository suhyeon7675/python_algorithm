#종이 자르기
def solution(M, N):
    N = (N - 1) * M
    M = M - 1
    answer = N + M
    return answer