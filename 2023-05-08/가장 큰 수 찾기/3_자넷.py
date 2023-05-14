def solution(array):
    answer = []
    print(len(array))
    for i in range(1, len(array)+1):
        if array[i-1] > array[i-2]:
            answer = [array[i-1], i-1]
    return answer
