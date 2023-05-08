def solution(num, k):
    answer = -1
    
    s = str(num)
    
    for i in range(len(s)):

        if int(s[i])==k:
            answer = i+1 #숫자 카운팅은 1부터 하니까 +1
            break
    
    
    return answer