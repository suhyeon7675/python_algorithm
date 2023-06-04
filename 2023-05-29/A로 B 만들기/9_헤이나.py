def solution(before, after):
    answer = 0
    
    
    for b in before:
        if b in after:
            after = after.replace(b,'',1)
    
    if after =='':
        return 1
    
    return answer