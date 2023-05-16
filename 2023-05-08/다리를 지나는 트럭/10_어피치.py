# 230514
# [PGS] 다리를 지나는 트럭 / 레벨2 / 1시간20분(검색 도움 받음)
# https://school.programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):

    # 테스트 5 시간 초과
    answer = 0
    bridge = [0] * bridge_length

    while True:
        if (not truck_weights) and sum(bridge) == 0:
            break

        answer += 1
        bridge.pop(0)
        next_num = 0

        if truck_weights:
            if sum(bridge)+truck_weights[0] <= weight:
                next_num = truck_weights.pop(0)
        bridge.append(next_num)

    return answer
