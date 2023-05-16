def solution(s):
    listS = list(s)
    openList = []
    answer = True
    if s[0] == ')' or s[-1] == '(' or listS.count('(') != listS.count(')'):
        answer = False
    else:
        for e in listS:
            if e == '(':
                openList.append(e)
            else:
                if len(openList) > 0:
                    openList.pop()
                else:
                    answer = False
                    break
    return answer
