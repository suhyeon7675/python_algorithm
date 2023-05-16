def solution(prices):
    answer = [0] * len(prices)
    for p in range(len(prices)):
        q = p + 1
        while q != len((prices)):
            if prices[p] <= prices[q]:
                answer[p] += 1
                q += 1
            else:
                answer[p] += 1
                break
    return answer
