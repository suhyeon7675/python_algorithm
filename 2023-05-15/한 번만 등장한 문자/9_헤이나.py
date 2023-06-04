def solution(s):
    answer = ''
    
    dict = {}
    
    for c in s:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
    print(dict)
    
    for d in dict:
        if dict[d] == 1:
            answer += d
    answer = ''.join(sorted(answer))
    
    return answer