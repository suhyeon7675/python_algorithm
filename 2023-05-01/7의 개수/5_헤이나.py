def solution(array):
    answer = 0

    for a in array:

        while True:

            if a > 10:
                if a % 10 == 7:
                    answer += 1
                a = a // 10

            else:
                break

        if a == 7:
            answer += 1

    return answer


## 나는 int로 그대로 풀어서 자리수별로 나눴는데 str으로 바꿔서 풀면 더 간단한 것 같다.

# 새로운 풀이
def solution(array):
    answer = 0

    for a in array:
        for ch in str(a):
            if ch == '7':
                answer += 1

    return answer