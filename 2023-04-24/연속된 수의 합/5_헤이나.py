def sum(num):    
    result = 0
    for i in range(num):
        result += i

    return result


def solution(num, total):
    answer = []    
    a = 0
    
    a = (total - sum(num))//num
    
    for i in range(num):
        answer.append(a+i)
    
    
    return answer