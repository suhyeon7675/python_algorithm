def solution(my_string, num1, num2):
    temp_list = list(my_string)
    temp = my_string[num1]
    temp_list[num1] = temp_list[num2]
    temp_list[num2] = temp
    return ''.join(temp_list)
