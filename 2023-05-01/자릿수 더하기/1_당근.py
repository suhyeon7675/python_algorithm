def solution(n):
    n_list = list(map(int, str(n)))
    n_list = sorted(n_list)
    
    answer = sum(n_list)
    return answer
