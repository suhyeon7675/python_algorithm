def solution(participant, completion):
    answer = ''
    
#     for com in completion:
#         if com in participant:
#             participant.remove(com)
    
#     # print(participant)
#     answer = participant[0]
    
    #1차시도 : 정확성은 모두 통과, 효율성은 모두 시간초과
    
    # for person in participant:
    #     if person not in completion:
    #         return person
    #2차시도 : participant 먼저 돌려봤으나 애초에 이 방법은 효율성에 걸리는 듯 하다.
    
    
    
    
    # 인덱스로 찾는 것은 효율이 떨어지기 때문에 key-value로 찾는 것이 효율적이다.
    # 인덱스 find로 찾는 것은 O(n^2)이고 hash는 O(n)
    
    part_dict = {}
    
    for person in participant:
        if person in part_dict:
            part_dict[person] += 1
        else:
            part_dict[person] = 1
    
    for person in completion:
        part_dict[person] -= 1
        
    for part in part_dict:
        if part_dict[part] > 0:
            return part
        

    return answer