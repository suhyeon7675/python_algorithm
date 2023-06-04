def solution(i, j, k):
    answer = 0
    
    for a in range(i, j+1 ,1):
        for b in str(a):
            
            if str(k) in str(b):
                answer +=1
            # print(b, answer)
    return answer