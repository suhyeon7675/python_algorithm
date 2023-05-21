def solution(participant, completion):
    dic={}
    sumHash=0
    
    for i in participant:
        dic[hash(i)]=i
        sumHash += hash(i)
    
    for i in completion:
        sumHash -= hash(i)
    
    return dic[sumHash]
