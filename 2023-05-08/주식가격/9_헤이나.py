def solution(prices):
    answer = []
    
    #1차시도
#     whole_time = len(prices)
    
#     for i in range(whole_time):
#         time = whole_time-i-1
#         for j in range(whole_time):
            
#             if prices[i]>prices[j] and j>i:         
#                 time = time-1             
#         answer.append(time)
    #테스트 1만 통과함..
    
    
    
    #진심 어려워서 chatGPT찬스.. 근데 반정도 이해됨
    n = len(prices)
    answer = [0]*n
    stack = [0] #비교할 인덱스를 저장함, 가격이 떨어지지 않은 기간의 인덱스
    
    for i in range(1, n):
        # print('stack', stack)
        # print(prices[stack[-1]])
        while stack and prices[i] < prices[stack[-1]]:  # 기준값보다 가격이 떨어졌을 때
            
            j = stack.pop()     #해당인덱스를 꺼내고
            # print('j', j)
            answer[j] = i-j  #임시저장. 해당 인덱스에, 가격이 떨어지지 않은 기간
            # print(answer)
        stack.append(i)
    
    # print(stack)
    
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j

    return answer