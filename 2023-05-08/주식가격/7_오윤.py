def solution(prices):
    answer = [i-1 for i in range(len(prices),0,-1)]
    stack = []
    for cur_day, cur_pri in enumerate(prices):
        while stack and stack[-1][1] > cur_pri:
            prev_day,_ = stack.pop()
            answer[prev_day] = cur_day - prev_day
        stack.append((cur_day, cur_pri))
    return answer
