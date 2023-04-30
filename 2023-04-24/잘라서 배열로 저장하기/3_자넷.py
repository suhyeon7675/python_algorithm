def solution(my_str, n):
    answer = []
    
    copy_str = my_str
    
    #String 나뉘어야 할 숫자만큼 돌려서
    for i in range(1, (len(my_str)//n) + 1):
        #n수만큼 잘라서 리턴리스트에 추가
        answer.append(copy_str[:n])
        #copy_str에서 리턴리스트 들어간 내용 삭제
        copy_str = copy_str[n:]
        
    #자르고 나머지 있으면 리턴리스트에 추가
    if len(copy_str) != 0:
        answer.append(copy_str)
        
    return answer
