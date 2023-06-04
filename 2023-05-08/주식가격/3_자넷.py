def solution(prices):
    answer = []
    steady = 0
    
    for i in range(0, len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] >= prices[i]:
                steady += 1
            else:
                steady += 1
                break
        answer.append(steady) 
        steady = 0
    return answer
