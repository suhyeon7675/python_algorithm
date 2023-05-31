def solution(citations):
    if sum(citations) == 0:
        return 0
    
    citations = sorted(citations, reverse=True)
    mean = len(citations) // 2
    
    def upper(mean):
        half = 0
        for i in citations:
            if i >= mean:
                half += 1
            else:
                break
        return half
    
    def find_max_mean_plus_i(mean):
        i = 0
        while True:
            if upper(mean+i) >= mean+i:
                i += 1
            else:
                i -= 1
                break
        return mean+i

    return find_max_mean_plus_i(mean)