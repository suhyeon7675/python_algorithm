# 230507
# [PGS] OX퀴즈 / 레벨0 / 9분
# https://school.programmers.co.kr/learn/courses/30/lessons/120907

def solution(quiz):
    answer = []
    for e in quiz:
        e_split = e.split()

        if e_split[1] == '-':
            correct = int(e_split[0]) - int(e_split[2])
            if correct == int(e_split[-1]):
                answer.append('O')
            else:
                answer.append('X')
        else:
            correct = int(e_split[0]) + int(e_split[2])
            if correct == int(e_split[-1]):
                answer.append('O')
            else:
                answer.append('X')
    return answer
