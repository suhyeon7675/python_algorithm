def solution(common):
    # 등차인지 등비인지 확인
    #등차수열의 경우
    if common[1] - common[0] == common[2] - common[1]:
        return common[-1] + (common[1] - common[0])
    #등비수열의 경우
    elif common[1] // common[0] == common[2] // common[1]:
        return common[-1] * (common[1] // common[0])
