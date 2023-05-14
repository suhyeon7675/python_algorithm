# 효율성 테스트 3 실패
# prices의 길이는 2 이상 100,000 이하입니다.
# 십만개가 오름차순일 때 시간복잡도는 O(N^2) 최대치

from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        p = prices.popleft()
        for i in range(len(prices)):
            if prices[i] < p:
                answer.append(i+1)
                break
        else:
            answer.append(len(prices))
    return answer

# chatGPT
from collections import deque
def solution(prices):
    answer = [0] * len(prices) # 결과값을 담을 리스트
    stack = [] # 스택

    for i, price in enumerate(prices):
        # 스택이 비어있지 않고, 가격이 떨어졌을 경우
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i) # 인덱스를 스택에 추가

    # 스택에 남은 인덱스 처리
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j

    return answer
