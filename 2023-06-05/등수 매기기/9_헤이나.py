def solution(score):
    answer = [1]*len(score)
    average = []
    print(answer)
    
    for s in score:
        average.append((s[0]+s[1])/2)
    
    # print(average)
    for i in range(len(average)):
        for j in average:
            # print(i, j)
            if average[i] < j:
                answer[i] +=1
    
    
    return answer
