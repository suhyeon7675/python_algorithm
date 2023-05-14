def solution(quiz):
    answer = []
    
    for i in quiz:
        quizsplit = i.split(' ')
        if quizsplit[1] == '+':
            if int(quizsplit[0]) + int(quizsplit[2]) == int(quizsplit[4]):
                answer.append('O')
            else:
                answer.append('X')
        elif quizsplit[1] == '-':
            if int(quizsplit[0]) - int(quizsplit[2]) == int(quizsplit[4]):
                answer.append('O')
            else:
                answer.append('X')
    return answer
