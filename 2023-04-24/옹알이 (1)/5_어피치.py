# 230430
# [PGS] 옹알이 (1) / 레벨0 / 15분
# https://school.programmers.co.kr/learn/courses/30/lessons/120956

def solution(babbling):
    # 각 babbling 요소마다 앞에서부터 문자열 비교한 후 slicing하여 다시 비교
    answer = 0
    l = ["aya", "ye", "woo", "ma"]

    for b in babbling:
        while b:
            if b[:2] in l:
                b = b[2:]
            elif b[:3] in l:
                b = b[3:]
            else:
                break

            if not b:
                answer += 1

    return answer
