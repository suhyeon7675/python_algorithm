def solution(array):
    answer = 0
    listsplit = []
    for i in range(len(array)):
        listsplit = list(map(int,str(array[i])))
        for i in listsplit:
            if(i == 7):
                answer += 1
    return answer
