def solution(s):
    if s[0] == ")":
        return False
    else:
        stack = []
        for i in s:
            if i == "(":
                stack.append("(")
            else:
                try:
                    stack.pop()
                except:
                    return False
        if stack == []:
            return True
        else:
            return False