import itertools

def solution(babbling):
    answer = 0
    p = ["aya", "ye", "woo", "ma"]
    pp = []
    for i in range(1, 5):
        for perm in itertools.permutations(p, i):
            pp.append("".join(perm))
    for bab in babbling:
        if bab in pp:
            answer += 1
    return answer