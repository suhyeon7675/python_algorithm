def solution(quiz):
    answer = []

    for q in quiz:
        formula, result = q.split('= ')

        if int(result) == int(eval(formula)):
            answer.append("O")
        else:
            answer.append("X")

    return answer