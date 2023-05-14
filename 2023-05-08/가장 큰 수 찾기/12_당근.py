def solution(array):
    
    answer = []
    m = max(array)
    i = array.index(max(array))
    answer.append(m)
    answer.append(i)
    
    return answer
