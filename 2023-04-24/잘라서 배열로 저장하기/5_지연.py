def solution(my_str, n):
    my_len = len(my_str) // n if len(my_str) // n == len(my_str)/n else int(len(my_str)/n+1)
    answer = [my_str[n*idx:n*(idx+1)] for idx in range(my_len)]
    return answer
