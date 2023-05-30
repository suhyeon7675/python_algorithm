def solution(array, n):
    m = 9999
    answer = -1

    array.sort()

    for i in array:
        if m > abs(n-i):
            m = abs(n-i)
            answer = i
    return answer
