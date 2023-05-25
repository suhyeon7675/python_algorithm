def solution(operations):
    answer = []
    
    n = 0
    q = []
    while n < len(operations):
        if operations[n][0] == "I":
            q.append(int(operations[n][2:]))
        elif operations[n] == "D 1":
            try:
                q.remove(max(q))
            except:
                pass
        else:
            try:
                q.remove(min(q))
            except:
                pass
        n += 1
        
    if len(q) == 0:
        answer = [0,0]
    else:
        answer = [max(q),min(q)]
    return answer