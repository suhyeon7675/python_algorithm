'''
str() : 문자열로 변환
'''
def solution(i, j, k):
    answer = 0
    for n in range(i, j+1):
        if str(k) in str(n):
            answer += str(n).count(str(k))
    return answer