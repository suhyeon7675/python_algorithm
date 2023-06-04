def solution(genres, plays):
    dic = {}
    dic2 = {}
    answer = []
    
    for i, (key, v) in enumerate(zip(genres, plays)):
        if key in dic:
            dic[key].append((i, v))
        else:
            dic[key] = [(i,v)]
        
        if key in dic2:
            dic2[key] += v
        else:
            dic2[key] = v

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)
    return answer
