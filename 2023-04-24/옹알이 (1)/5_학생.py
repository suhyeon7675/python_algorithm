#옹알이 (1)
def solution(babbling):
    List = ["aya", "ye", "woo", "ma"]
    sum, answer = 0, 0
    for i in babbling:
        for j in List:
            if j in i:
                sum += len(j)
        if len(i) == sum:
            answer += 1
        sum = 0
    return answer