def solution(bin1, bin2):
    bin1 = int(bin1,2)
    bin2 = int(bin2,2)
    num =  bin1 + bin2
    return format(num, 'b')
  
# 다른 사람 풀이
def solution(bin1, bin2):
    answer = bin(int(bin1,2) + int(bin2,2))[2:]
    return answer
