def solution(prices):
    answer = []
    end = len(prices)-1
    for i in range(0,end):
        sec = 0
        for j in range(i,end):
            if prices[i] <= prices[j]:
                sec+=1
            else:
                break
        answer.append(sec)
    answer.append(0)
    return answer
