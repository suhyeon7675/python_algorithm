#다음에 올 숫자
def solution(common):
    minus = common[2] - common[1]
    if minus == (common[1] - common[0]):
        return common[-1] + minus
    else:
        return common[-1] * (common[1] / common[0])
