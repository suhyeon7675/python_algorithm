def solution(n):
    answer = [1]
    for i in range(1, n // 2):
        if n % i == 0:
            answer.append(i)
            answer.append(int(n // i))
    answer = list(set(answer))
    answer.sort()
    return answer
