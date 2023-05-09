def solution(my_string):
    strList = my_string.split(' ')

    answer = int(strList[0])

    for i in range(2, len(strList)+1, 2):
        if strList[i-1] == '+':
            answer += int(strList[i])
        else:
            answer -= int(strList[i])
            
    return answer
