def solution(array, commands):
    answer = []
    
    for command in commands:
        # print(command)
        temp = array[command[0]-1:command[1]]
        temp.sort()
        # print(temp)
        answer.append(temp[command[2]-1])
    
    
    
    return answer