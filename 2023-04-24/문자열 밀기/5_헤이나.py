def solution(A, B):
    answer = 0

    A += A
    
    # "hellohello"를 만들어서 오른쪽으로 밀기 , index slice 사용
    for i in range(len(B)):
        
        if A[len(B)-i:len(A)-i] ==B:
             return i
             
    return -1

