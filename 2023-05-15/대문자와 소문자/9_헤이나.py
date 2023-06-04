def solution(my_string):
    answer = ''
    
    for ch in my_string:
        c = ''
        if ch.isupper():
            c = ch.lower()
        else:
            c = ch.upper()
        
        answer += c
    
    return answer