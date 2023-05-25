def solution(array, n):
    a = [abs(n-i) for i in array]
    minidx = [i for i, x in enumerate(a) if x == min(a)]
    if len(minidx) == 1:
        return array[minidx[0]]
    else:
        if array[minidx[0]] < array[minidx[1]]:
            return array[minidx[0]]
        else:
            return array[minidx[1]]