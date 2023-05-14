from collections import deque

def solution(bridge_length, weight, truck_weights):
    cross = deque()
    time = 0
    for idx, truck in enumerate(truck_weights):
        cross.append(truck)
        time += 1
        if idx != len(truck_weights)-1:
            if (sum(cross) + truck_weights[idx + 1] > weight):
                time += bridge_length - len(cross)
                while sum(cross) + truck_weights[idx + 1] > weight:
                    cross.popleft()
                    time += 1
                time -= 1
        else:
            time += bridge_length
    return time
