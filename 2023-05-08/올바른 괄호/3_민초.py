def solution(s):
    answer = True
    list = []
    for i in s:
        if i=='(':
            list.append(1)
        elif not list:
            return False
        else:
            list.pop()
    if list:
        return False
    return True
