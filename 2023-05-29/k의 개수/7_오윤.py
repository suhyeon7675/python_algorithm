def solution(i, j, k):
    answer = 0
    arr = ''
    for num in range(i, j+1):  # 실수한 부분. 숫자는 i부터 j까지이므로 반복문 시작은 i부터.
        arr += str(num)
    answer += arr.count(str(k))
    return answer
