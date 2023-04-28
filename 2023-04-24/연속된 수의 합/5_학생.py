#연속된 수의 합
def solution(num, total):
    answer = []
    if (total%num == 0):
        for i in range(total//num - num//2, num//2 + total//num + 1):
            answer.append(i) 
    else:
        for i in range(total//num - num//2 + 1, num//2 + total//num + 1):
            answer.append(i)
    return answer

