from itertools import permutations

def solution(babbling):
    answer = 0
    #발음 가능 list
    canSpeak = ["aya", "ye", "woo", "ma"]
    #조합가능 단어 list
    speakables=[]

    #순열 생성
    #permutations(canSpeak, 1) ~ permutations(canSpeak, len(canSpeak))
    for i in range(1, len(canSpeak)+1):
        for j in permutations(canSpeak, i):
            #조합을 공백없이 합쳐서 단어 list에 추가
            speakables.append("".join(j))

    #인입 된 babbling 중 조합가능단어에 포함된 경우 count += 1
    for word in babbling:
        if word in speakables:
            answer += 1

    return answer
