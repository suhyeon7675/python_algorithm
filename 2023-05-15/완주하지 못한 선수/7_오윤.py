# 리스트로 구현하면 효율성 문제로 통과 X, 딕셔너리로 구현해야함. (리스트의 in 과 딕셔너리의 in은 시간복잡도가 다르다.)
def solution(participant, completion):
    part_dict = {}
    ans = ''
    for v in participant:  # 딕셔너리에 참가자 삽입
        if v in part_dict:
            part_dict[v] += 1  #동명이인의 경우에 key 중복 안되므로 value를 +1 하여 인원수 표기
        else:
            part_dict[v] = 1

    for c in completion:  # 완주자 배열에서 한 명씩 뽑아서
        if c in part_dict:  # 참가자 명단에 완주자가 있을 경우 인원수(value)에서 -1
            part_dict[c] -= 1  #따라서 만일 동명이인 중에서 완주자와 미완주자가 있어도 value 1이 남음
        else:
            continue  #동명이인이 아닌 미완주자

    for v in participant:  # 딕셔너리에서 value = '1'로 key를 뽑아내기 위한 반복문
        if part_dict[v] == 1:
            ans = v
    return ans
