def solution(s):
    stack = []
    answer = True
    for i in s:
        if len(stack) == 0 and i == ")":
            answer = False
        elif i == ")" and stack[-1] == "(":
            stack.pop()
        else :
            stack.append(i)
    if len(stack) != 0:
        answer = False
    return answer
