def solution(num, total):
    answer = []
    #더하는 숫자들의 중앙값을 찾아주기
    middle = total//num
    #중앙 카운트 찾아주기
    middleNum = num//2
    startNum = 0;
    endNum = 0;
    
    if num%2 == 0: #num이 짝수의 경우
        #중앙숫자가 list 반의 왼쪽에 위치해서 중앙값 - 왼쪽으로 남은 카운트 해주면 시작값이 나옴
        startNum = middle - middleNum + 1
        #오른쪽으로 남은 카운트 더해주는데
        endNum = middle + middleNum + 1
    else: #num이 홀수의 경우
        #중앙값 - 왼쪽으로 남은 카운트
        startNum = middle - middleNum
        #중앙값 + 오른쪽으로 남은 카운트
        endNum = middle + middleNum + 1

    answer.extend(range(startNum, endNum))
    
    return answer
