def solution(babbling):
    answer = 0
    for babble in babbling:
        while babble:
            if babble[:3] in ["aya", "woo"]:
                babble = babble[3:]
            elif babble[:2] in ["ye", "ma"]:
                babble = babble[2:]
            else:
                break
        if babble =="":
            answer += 1
    return answer
