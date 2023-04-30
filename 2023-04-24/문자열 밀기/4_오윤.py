#문자열 밀기
def solution(A, B):
    answer = 0
    if A != B:
        B = list(B)
        for i in range(len(A)):
            ch = []
            ch = [A[i-1] for i in range(len(A))]
            A = ch
            answer += 1
            if A != B and len(A)==answer:
                answer = -1
            elif A == B: break       
    return answer
  
  # 다른 사람 대박적 풀이
  # solution=lambda a,b:(b*2).find(a) 본받기..ㅠㅠ
