import numpy as np

def solution(answers):
    f = [1,2,3,4,5]
    s = [2,1,2,3,2,4,2,5]
    t = [3,3,1,1,2,2,4,4,5,5]
    fa, sa, ta = 0, 0, 0
    
    for i in range(len(answers)):
        if answers[i] == f[(i+1) % len(f) - 1]:
            fa += 1
        if answers[i] == s[(i+1) % len(s) - 1]:
            sa += 1
        if answers[i] == t[(i+1) % len(t) - 1]:
            ta += 1
            
    a = [fa, sa, ta]
    return [i+1 for i, j in enumerate(a) if j == max(a)]