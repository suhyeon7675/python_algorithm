def solution(citations):
    answer = 0
    for i in range(max(citations), 0, -1):
        newArr = [num for num in citations if num >= i]
        if len(newArr) >= i:
            answer = i
            break
    return answer
