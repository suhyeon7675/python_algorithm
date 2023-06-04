def solution(my_string):
    my_string = list(my_string)
    for i in range(len(my_string)):
        if ('A' <= my_string[i] and my_string[i] <= 'Z'):
            my_string[i] = chr(ord(my_string[i]) + 32)
        else:
            my_string[i] = chr(ord(my_string[i]) - 32)     
    return ''.join(map(str, my_string))