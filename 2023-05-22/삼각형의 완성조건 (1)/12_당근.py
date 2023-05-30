def solution(sides):
    answer = 0
    m = max(sides)
    n = sum(sides) - m
    if m < n :
        return 1
    else :
        return 2
