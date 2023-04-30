# 230430
# [PGS] 다음에 올 숫자 / 레벨0 / 12분10초
# https://school.programmers.co.kr/learn/courses/30/lessons/120924

def solution(common):

    # 나의 풀이
    # x == 0 조건문 따로 뺄 필요 없음
    last = common[-1]
    llast = common[-2]
    x = last - llast

    if x == 0:
        answer = last
    elif x == (common[1] - common[0]):  # 등차수열
        answer = last + x
    else:                               # 등비수열
        answer = last * (last // llast)

    return answer
