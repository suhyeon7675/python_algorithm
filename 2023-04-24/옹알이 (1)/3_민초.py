from itertools import permutations

def solution(babbling):
    answer = 0
    speek = ["aya", "ye", "woo", "ma"]
    bab = []
    for i in range(1, len(speek)+1):
        for j in permutations(speek, i):
            bab.append(''.join(j))

    for i in babbling:
        if i in bab:
            answer+=1
    return answer
