def solution(my_string):
    answer = ''
    #my_string 의 알파벳값을 lower ->list 저장    
    str_list = [x for x in my_string.lower()]
    #순서대로 sorting
    str_list.sort()
    
    #string list -> string으로 변환
    answer = ''.join(str(e) for e in str_list)
    
    
    
    return answer
