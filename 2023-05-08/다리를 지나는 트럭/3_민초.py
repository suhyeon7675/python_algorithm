def solution(bridge_length, weight, truck_weights):
    b = [0] * bridge_length
    sec = 0
    i = 0
    while (b):
        sec += 1
        i-=b.pop(0)
        if truck_weights:
            if ( i + truck_weights[0] ) <= weight:
                i+=truck_weights[0]
                b.append(truck_weights.pop(0))
            else:
                b.append(0)
    return sec
