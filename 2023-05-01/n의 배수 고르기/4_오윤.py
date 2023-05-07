#n의 배수 고르기
def solution(n, numlist):
    answer = []
    for num in numlist:
        if num % n == 0:
            answer.append(num)
    return answer
  
# 다른 사람 코드 참고 1 : 리스트 컴프리헨션
def solution(n, numlist):
    answer = [num for num in numlist if num % n == 0]
    return answer
  
# 다른 사람 코드 참고 2 : filter? lambda
def solution(n, numlist):
  retrun list(filter(lambda num: num%n==0, numlist)

