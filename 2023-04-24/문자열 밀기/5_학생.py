#문자열 밀기
def solution(A, B):
    list_A = A
    answer = 0
    if (A == B): return 0
    for i in range(len(A)-1):
        list_A = list_A[-1] + list_A[:-1]
        answer += 1
        if(list_A == B):
            return answer
    return -1