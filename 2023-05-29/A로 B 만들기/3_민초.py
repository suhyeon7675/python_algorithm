def solution(before, after):
    for i in before:
        after=after.replace(i,'',1)
    if len(after) ==0:
        return 1
    return 0
