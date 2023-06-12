def solution(sizes):
    answer = 0
    
    for size in sizes:
        size = size.sort()
    
    
    wid = 0
    hei = 0
    for i in range(len(sizes)):
        # print(sizes[i])
        if wid < sizes[i][0]:
            wid = sizes[i][0]
        if hei < sizes[i][1]:
            hei = sizes[i][1]
    
    # width = max(sizes[0])
    # height = max(size[1])
    
    # print(wid)
    answer = wid * hei
    
    
    return answer
