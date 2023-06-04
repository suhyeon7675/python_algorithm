def solution(array, n):
    min = 100

    for num in sorted(array, reverse=True):
        if abs(min - n) >= abs(num - n):
            min = num
    return min
                
