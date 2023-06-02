def solution(before, after):
    answer = 1
    before = list(before)
    for str in after:
        if str not in before:
            return 0
        else:
            before.remove(str)
    return answer
