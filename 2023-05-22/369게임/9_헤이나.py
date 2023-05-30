def solution(order):
    answer = 0
    
    for _ in range(7): # 1,000,000이 최대
        if order//10 <1:
            if order%3==0:
                answer+=1
            break
        else:
            if (order%10)%3==0 and (order%10)!=0:
                answer+=1
            order = order//10
            
    
    return answer