def solution(bin1, bin2):
    answer = ''
    bin1, bin2, next = int(bin1), int(bin2), 0
    while True:
        temp = bin1 % 10 + bin2 % 10 + next
        bin1, bin2 = bin1 // 10, bin2 // 10
        if temp >= 2:
            next = 1
            answer += str(temp-2)
        else:
            next = 0
            answer += str(temp)
            if bin1 + bin2 == 0:
                break
    return ''.join(reversed(list(answer)))