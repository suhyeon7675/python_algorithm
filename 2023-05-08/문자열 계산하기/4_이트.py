import re
def solution(my_string):
    integer = re.split(r'\s[-|\+]\s', my_string)
    
    cal = []
    for s in my_string:
        if s == '+' or s == '-':
            cal.append(s)
            
    if my_string[0] == '-':
        temp = -int(integer[0])
        for i in range(1, len(integer)):
            if cal[i] == '+':
                temp += int(integer[i])
            else:
                temp -= int(integer[i])
    else:
        temp = int(integer[0])
        for i in range(len(cal)):
            if cal[i] == '+':
                temp += int(integer[i+1])
            else:
                temp -= int(integer[i+1])
        
    return temp