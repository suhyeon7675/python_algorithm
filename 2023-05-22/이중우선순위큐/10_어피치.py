# 230527
# [PGS] 이중우선순위큐 / 레벨3 / 23분
# https://school.programmers.co.kr/learn/courses/30/lessons/42628

def solution(operations):
    l = []

    for op in operations:
        if op == 'D 1':
            if l:
                l.pop()
        elif op == 'D -1':
            if l:
                l.pop(0)
        else:
            l.append(int(op[2:]))
        l.sort()

    if l:
        return [l[-1], l[0]]
    else:
        return [0, 0]
