# 230525
# [PGS] 369게임 / 레벨0 / 4분
# https://school.programmers.co.kr/learn/courses/30/lessons/120891

def solution(order):
    answer = 0
    order = str(order)

    for e in ['3', '6', '9']:
        answer += order.count(e)

    return answer
