from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    qu = deque(truck_weights)
    cross = deque([0]*bridge_length)
    sum_weight = 0

    while cross:
        time += 1
        sum_weight -= cross[0]
        cross.popleft()

        if qu:
            if ( sum_weight + qu[0] ) <= weight:
                sum_weight += qu[0]
                cross.append(qu.popleft())
            else:
                cross.append(0)

    return time