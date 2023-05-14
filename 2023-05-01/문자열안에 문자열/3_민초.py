def solution(str1, str2):
    answer = 0
    if str1.find(str2) == -1:
        answer = 2
    else :
        answer = 1
        
    print(str1 in str2)
    return answer
