def solution(A, B):
    answer = 0
    for answer in range(len(A)):
       if A == B:
        return answer
       A = A[-1] + A[:-1]
    return -1
