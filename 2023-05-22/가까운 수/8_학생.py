def solution(array, n): 
    answer = 9999
    for i in sorted(array):
        if (answer > abs((i-n)/2)):
            answer = abs((i-n)/2)
            j = i
    return j
