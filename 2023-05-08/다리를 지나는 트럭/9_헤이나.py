from collections import deque # 양쪽 끝에서의 삽입/삭제 o(1)

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    q = deque()
    bridge_weight = 0
    time_list = []
    time = 0
    
    while True:
        time += 1 
        if time_list and time_list[0] + bridge_length == time:  # 트럭이 다리를 다 지났는지 확인
            bridge_weight -= q.popleft() # 다 지났으면 다리위 트럭무게만큼 제외
            print(bridge_weight)
            time_list.pop(0)
            
        if truck_weights:  #남은 트럭 확인
            if bridge_weight + truck_weights[0] <= weight: #트럭을 추가해도 되는지 확인
                bridge_weight += truck_weights[0]
                q.append(truck_weights.pop(0))  # 지난 트럭은 q로
                time_list.append(time)  # 트럭이 진입한 시간을 저장해서 시간 관리
                
        if not truck_weights and not q:
            break
            
    return time
    