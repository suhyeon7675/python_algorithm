def solution(quiz):
    answer = []
    for q in quiz:
        a = q.split(' ')
        if a[1] == '+':
            answer.append('O' if int(a[0]) + int(a[2]) == int(a[4]) else 'X')
        else:
            answer.append('O' if int(a[0]) - int(a[2]) == int(a[4]) else 'X')
    return answer
