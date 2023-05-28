def solution(sides):
    return 1 if max(sides) < sorted(sides)[0] + sorted(sides)[1] else 2
