def solution(score):
    hap = [sum(i) for i in score]
    answer = []
    for h in hap:
        rank = 1
        for j in hap:
            if h < j:
                rank += 1
        answer.append(rank)
    return answer
