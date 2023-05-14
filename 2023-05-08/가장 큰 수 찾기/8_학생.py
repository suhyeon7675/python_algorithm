def solution(array):
    answer = []
    num, j = 0, 0
    for i in range(len(array)):
        if array[i] >= num:
             num = array[i]
             j = i
    answer.append(num)
    answer.append(j)
    return answer