def solution(common):
    answer = 0
    
    #등차수열 확인
    def diff(iter1, iter2):
        return common[iter2] - common[iter1]
    #등비수열 확인
    def divis(iter1, iter2):
        return common[iter2]/common[iter1]
    
    if diff(1,2)==diff(0,1):
        return common[-1] + diff(1,2)
    else:
        return common[-1]*divis(1,2)
    
    
    
    return answer