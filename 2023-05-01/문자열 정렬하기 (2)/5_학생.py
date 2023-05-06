def solution(my_string):
    answer =''
    for i in my_string:
        if('A' <= i and i <= 'Z'):
            answer += chr(ord(i)+32)
        else: answer += i
    answer = sorted(answer)
    return ''.join(answer)