def solution(my_string):
    op_list = my_string.split(" ")
    answer = int(op_list[0])
    idx = 1
    while idx < len(op_list):
        answer += int(op_list[idx + 1]) if op_list[idx] == "+" else int(op_list[idx + 1]) * -1
        idx += 2
    return answer
