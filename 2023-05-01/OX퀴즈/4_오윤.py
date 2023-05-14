#OX 퀴즈
def solution(quiz):
    answer = []
    for i in quiz:
        a = i.split()
        if a[1] == '+' and int(a[0])+int(a[2]) == int(a[4]):
            answer.append("O")
        elif a[1] == '-' and int(a[0])-int(a[2]) == int(a[4]) :
            answer.append("O")
        else : answer.append("X")
    return answer
