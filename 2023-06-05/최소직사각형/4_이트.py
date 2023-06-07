def solution(sizes):
    L, S = 0, 0
    for 가로, 세로 in sizes:
        if 가로 >= 세로:
            L, S = max(L, 가로), max(S, 세로)
        else:
            L, S = max(L, 세로), max(S, 가로)
    return L * S