def solution(array):
    answer = 0
    arr = ''.join(list(map(str,array)))
    for i in arr:
        if '7' == i:
            answer += 1
    return answer
  
# 다른 사람 간단 풀이
def solution(array):
    return str(array).count('7')
