def solution(s):
    answer = 0
    
    for i in s: #s 문자열의 하나씩 돌면서
        if answer < 0:
            break # 답이 마이너스가 되면 괄호가 제대로 안닫힌 것임으로, break
        if i == '(': # 괄호가 열리면 +1
            answer += 1
        else: #괄호가 닫히면 -1
            answer -= 1

    return answer == 0 #괄호 여닫이가 정상적인경우 0이 됨
