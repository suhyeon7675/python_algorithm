def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]
    for bb in babbling:
        for i in word:
            if i in bb:
                bb = bb.replace(i," ")
        bb = bb.strip() #공백을 제거했을 때
        if len(bb) == 0: # 문자열의 길이가 0이라면 word 가능 조합
            answer += 1
    return answer
