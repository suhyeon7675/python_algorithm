def solution(num, total):
    answer = []
    totMid = total//num
    numMid = num//2
    
    if num%2 == 0:
        answer = [i for i in range(totMid-numMid+1, totMid+numMid+1)]
    else:
        answer = [i for i in range(totMid-numMid, totMid+numMid+1)]
    
    return answer
