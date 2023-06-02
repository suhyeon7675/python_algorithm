def solution(before, after):
    
    list_b = sorted(before)
    list_a = sorted(after)
    
    if list_b == list_a :
        return 1
    else:
        return 0
    
    #숫자(int) 정렬과 문자열(str) 정렬은 다르다는 점!
