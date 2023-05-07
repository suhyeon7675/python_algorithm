def solution(num, k):
    answer = 0
    numList = [int(x) for x in str(num)]
    for i in range(0, len(numList)):
        if numList[i] == k:
            answer = i + 1
            return answer
    
    return -1
