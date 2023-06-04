def solution(array, n):
    answer = 0
    min = 100
    for a in array:
        if abs(n-a) <min:
            min= abs(n-a)
            answer = a
        elif abs(n-a) == min:
            if answer>a:
                answer = a
            
    
    return answer