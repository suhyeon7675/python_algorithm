def solution(bin1, bin2):
    addition = int(bin1,2)+int(bin2, 2)
    return bin(addition)[2:]
