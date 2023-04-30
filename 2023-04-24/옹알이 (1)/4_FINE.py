'''
itertools : 순열과 좌합을 만들어주는 모듈
permutations(객체, r)
서로 다른 n개에서 r개를 선택할 때, "순서를 고려"하여 중복없이 뽑을 경우의 수
=>반복 가능한 객체(리스트, 튜플, 문자열) 안에서 r개를 선택한다.
permutations('ABCD', 2) | AB, AC, AD, BA, BC, BD, CA, CB, CD, DA, DB, DC

vs

product('ABCD', repeat=2) | AA, AB, AC, AD, BA, BB, BC, BD, CA, CB, CC, CD, DA, DB, DC, DD
combinations('ABCD', 2) | AB, AC, AD, BC, BD, CD
combinations_with_replacement('ABCD', 2) | AA, AB, AC, AD, BB, BC, BD, CC, CD, DD
'''
from itertools import permutations

def solution(babbling):
    answer = 0
    speek = ["aya", "ye", "woo", "ma"]
    word = []
    for i in range(1, len(speek)+1):
        for j in permutations(speek, i):
            word.append(''.join(j))

    for i in babbling:
        if i in word:
            answer += 1

    return answer