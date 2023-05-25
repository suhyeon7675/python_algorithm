def solution(sides):
    long = max(sides)
    sides.remove(long)
    if long < sum(sides):
        return 1
    else:
        return 2