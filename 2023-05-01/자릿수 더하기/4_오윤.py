# 자릿수 더하기
def solution(n):
    answer = [int(str(n)[i]) for i in range(len(str(n)))]
    return sum(answer)
  
# 다른 사람 간결한 코드
def solution(n):
    answer = [int(i) for i in str(n)]
    return sum(answer)
