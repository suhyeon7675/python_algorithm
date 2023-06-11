def solution(answers):
    answer = []
    score = [0,0,0]
    solve_1 = [1,2,3,4,5]
    solve_2 = [2,1,2,3,2,4,2,5]
    solve_3 = [3,3,1,1,2,2,4,4,5,5]
    iter_1 = 0
    iter_2 = 0
    iter_3 = 0
    
    
    for i in range(len(answers)):
        
        if answers[i]==solve_1[iter_1]:
            score[0] +=1
        iter_1 += 1
        if iter_1>= len(solve_1):
            iter_1 = 0
            
            
        if answers[i]==solve_2[iter_2]:
            score[1] += 1        
        iter_2 += 1
        if iter_2>= len(solve_2):
            iter_2 = 0
            
            
        if answers[i]==solve_3[iter_3]:
            score[2] += 1        
        iter_3 += 1
        if iter_3>= len(solve_3):
            iter_3 = 0
            
         
    # print(score)
    max_score = max(score)
    for i in range(3):
        if score[i]==max_score:
            answer.append(i+1)
    
    return answer
  
  
  
  #인덱스관련 런타임 에러가 났었다. 항상 인덱스 관리를 잘 하자.
