def solution(common):
    answer = 0
    if common[2] - common[1] == common[1] - common[0]:
        d = common[2] - common[1]
        answer = common[-1] + d
    else:
        r = common[2] / common[1]
        answer = common[-1] * r
    return answer