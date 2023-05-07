def solution(quiz):
    answer = []
    for i in quiz:
        formula = i.split(' ')
        if formula[1] == '+':
            res = int(formula[0]) + int(formula[2])
        elif formula[1] == '-':
            res = int(formula[0]) - int(formula[2])
            
        if res == int(formula[4]):
            answer.append("O")
        else:
            answer.append("X")
    return answer
