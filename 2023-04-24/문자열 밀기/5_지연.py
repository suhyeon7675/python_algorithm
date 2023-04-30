def solution(A, B):
    for idx in range(len (A)):
        #A를 밀어서 B가 될 수 있다면
        if A == B:
            #몇 번 밀어야 하는지 횟수를 리턴하고
             return idx
        #각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동
        A = A[-1] + A[:-1]
    # 밀어서 B가 될 수 없으면 -1을 리턴
    return -1
