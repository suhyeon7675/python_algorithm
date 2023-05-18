def solution(s):
    singlelist = []
    strMap = dict()
    
    for i in [str(x) for x in s]:
        if i in strMap.keys():
            strMap[i] += 1
        else:
            strMap[i] = 1
    
    for i in strMap.keys():
        if strMap[i] == 1:
            singlelist.append(i)

    return ''.join(sorted(singlelist))
