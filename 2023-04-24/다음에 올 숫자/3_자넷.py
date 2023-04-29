def solution(common):
    answer = 0
    length = len(common) - 1
    
    first, second, third = common[:3]
    
    if second - first == third - second:
        answer = common[length] + (second - first)
    elif second//first == third//second:
        answer = common[length] * (second//first)
    
    return answer
