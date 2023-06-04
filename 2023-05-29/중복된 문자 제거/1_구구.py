def solution(my_string):
    answer = ''
    for str in list(my_string):
        if answer.count(str) == 0:
            answer += str
    return answer
