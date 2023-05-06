def solution(n):
    answer = 0
    
    for i in [int(x) for x in str(n)]:
        answer += i
        
    return answer
