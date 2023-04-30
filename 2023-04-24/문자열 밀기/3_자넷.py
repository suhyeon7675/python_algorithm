def solution(A, B):
    answer = 0
    compareA = A
    
    #A와 B 단어가 같지 않을경우만 로직실행
    if A != B: 
        #A 단어의 길이만큼 돌아가면서
        for i in range(0, len(A)):
            #list slicing을 통해 맨뒤를 앞으로 가져오기
            compareA = compareA[-1:] + compareA[:-1]
            answer += 1 
            if compareA == B:
                break
    
        #중간에 break한게 아니면 길이만큼 돌았을테니 -1 리턴
        if answer == len(A):
            answer = -1
    
    return answer
