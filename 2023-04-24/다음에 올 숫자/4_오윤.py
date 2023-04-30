def solution(common):
    answer = 0
    if common[1]-common[0] == common[2]-common[1]:
        answer = common[-1] + common[1]-common[0]
    else:
        answer = common[-1] * common[1]//common[0]
    return answer
    
# [다른 사람 풀이] 내가 common[1]-common[0] ..으로 가시성이 좋지않게 작성한 부분을 a,b,c = common[:3] 으로 받아 b-a , b//a 등으로 깔끔하게 작성함.
