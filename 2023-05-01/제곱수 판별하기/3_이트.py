from math import sqrt

def solution(n):
    if int(sqrt(n)) == sqrt(n):
        answer = 1
    else:
        answer = 2
    return answer