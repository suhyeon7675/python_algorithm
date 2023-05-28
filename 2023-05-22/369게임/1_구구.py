def solution(order):
    answer = 0
    find = ['3', '6', '9']
    for num in find:
        answer += str(order).count(num)
    return answer
