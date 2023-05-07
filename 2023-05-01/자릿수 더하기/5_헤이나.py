def solution(n):
    answer = 0
    
    temp = n
    while True:
        if temp//10 >0:
            answer += temp%10
            temp = temp//10
        else:
            answer += temp
            break
            

    return answer