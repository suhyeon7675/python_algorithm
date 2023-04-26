def solution(my_str, n):
    answer = []
    LEN = len(my_str) // n
    for i in range(LEN+1):
        answer.append(my_str[i*n:(i+1)*n])
    if "" in answer:
        answer.remove("")
    return answer