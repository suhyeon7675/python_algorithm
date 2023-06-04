import heapq

def solution(jobs):
    answer = 0
    now_time = 0
    size_job = len(jobs)
    
    sorted_heap = sorted(jobs, key=lambda x:x[0])
    heap =[]
    
    while sorted_heap or heap:
        
        while sorted_heap and sorted_heap[0][0]<= now_time:
            start, duration = sorted_heap.pop(0)
            heapq.heappush(heap, (duration, start))
        
        if heap:
            duration, start = heapq.heappop(heap)
            now_time = max(now_time, start) + duration
            answer += now_time - start
        else:
            now_time +=1

    
    answer //= size_job
    
    
    return answer