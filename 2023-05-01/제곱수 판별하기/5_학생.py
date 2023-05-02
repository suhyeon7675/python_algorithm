import math
def solution(n):
    if (math.sqrt(n) % int(math.sqrt(n)) == 0):
        return 1
    else: return 2