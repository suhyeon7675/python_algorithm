def solution(quiz):
    answer = []
    test = []
    for i in quiz:
        i = i.split(' = ') #공백 제거
        if '+' in i[0]:
            j = i[0].split(" + ")
            if ((int)(j[0]) + (int)(j[1]) == (int)(i[1])):
                answer.append("O")
            else: answer.append("X")
        else:
            j = i[0].split(" - ")
            if ((int)(j[0]) - (int)(j[1]) == (int)(i[1])):
                answer.append("O")
            else: answer.append("X")
    return answer