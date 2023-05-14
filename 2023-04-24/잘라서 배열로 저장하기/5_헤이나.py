def solution(my_str, n):
    answer = []
    
    num = len(my_str)//n
    
    for i in range(num+1):
        answer.append(my_str[n*i : n*(i+1)])
    
        
    if answer[-1] == '':
        answer.pop()
    
    return answer