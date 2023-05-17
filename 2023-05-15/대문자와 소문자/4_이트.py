def solution(my_string):
    lower = my_string.lower()
    answer = ''
    for i in range(len(my_string)):
        if my_string[i] == lower[i]:
            answer += my_string[i].upper()
        else:
            answer += my_string[i].lower()
    return answer