import heapq

def solution(operations):
    answer = []
    
    heap = []
    
    #print(operations)
    
    for op in operations:
        
        if 'I' in op:
            heapq.heappush(heap, int(op.split()[1]))
            
        elif 'D 1' in op:
            if len(heap)!=0:
                heap.pop(len(heap)-1)
            
        elif 'D -1' in op:
            if len(heap)!=0:
                 heapq.heappop(heap)
    
    if len(heap) == 0:
        return [0,0]
    else:
        
        answer.append(max(heap))
        answer.append(min(heap))
    
    
    return answer