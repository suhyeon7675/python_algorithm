def solution(i, j, k):
    numList = [str(i) for i in range(i, j + 1) if str(i).count(str(k)) > 0]
    return ''.join(numList).count(str(k))
