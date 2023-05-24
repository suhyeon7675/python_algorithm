# 230524
# [PGS] 암호 해독 / 레벨0 / 4분
# https://school.programmers.co.kr/learn/courses/30/lessons/120892

def solution(cipher, code):
    answer = ''

    for i in range(len(cipher)):
        if i % code == code - 1:
            answer += cipher[i]

    return answer

    # 다른 풀이
    # 문자열 슬라이싱 => string[start:end:step] => start 인덱스는 포함, end 인덱스는 미포함
    #return cipher[code-1::code]
