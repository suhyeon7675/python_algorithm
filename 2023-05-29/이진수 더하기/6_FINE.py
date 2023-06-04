'''
int() 함수는 문자열을 정수로 변환해주는 함수이다.
bin() 함수는 정수를 이진수로 변환해주는 함수이다.
'''
def solution(bin1, bin2):
    a = int(bin1, 2)
    b = int(bin2, 2)
    answer = bin(a+b)[2:]
    return answer