def solution(babbling):
    answer = 0
    check = ["aya","ye","woo","ma"]    
    for i in babbling:               
        for a in check:                
            i = i.replace(a,'!',1)   
        if i.replace('!','') == '':   
            answer += 1               
    return answer
