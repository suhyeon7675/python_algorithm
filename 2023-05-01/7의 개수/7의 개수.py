def solution(array):
    b = ''
    for a in array:
        b = b + str(a)
    return b.count('7')