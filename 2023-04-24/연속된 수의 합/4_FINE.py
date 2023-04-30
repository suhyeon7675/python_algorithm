def solution(num,total):
    answer=[]
    average = total // num
    for i in range(average - (num - 1) // 2, average + (num + 2) // 2):
        answer.append(i)
    return answer