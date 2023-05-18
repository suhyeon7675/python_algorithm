def solution(bridge_length, weight, truck_weights):
    hour = 0
    bridge = [0] * bridge_length
    
    #다리의 길이만큼 iteration 돌면서
    while bridge:
        #1초가 지나감에 따라
        hour += 1
        #다리 길이에서 맨 왼쪽의 값을 삭제처리 (=맨 마지막 값은 빈 값)
        bridge.pop(0)
        #지나갈 트럭이 남아있는 경우
        if truck_weights:
            #다리 위에 있는 트럭 + 새로 들어올 트럭 더한 값이 최대 무게보다 작으면
            if sum(bridge) + truck_weights[0] <= weight:
                #다리 위에 다른 트럭 하나 들어오고, 해당 트럭은 대기트럭에서 삭제처리
                bridge.append(truck_weights.pop(0))
            #다리 위에 있는 트럭 + 새로 들어올 트럭이 최대 무게를 넘으면
            else:
                #아직 신규 트럭 못건넘 = 건너는 트럭 마지막 값에 0 추가
                bridge.append(0)
            
    return hour
