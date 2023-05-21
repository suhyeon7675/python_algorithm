# 230518
# [PGS] 대문자와 소문자 / 레벨0 / 3분50초
# https://school.programmers.co.kr/learn/courses/30/lessons/120893

def solution(my_string):
    answer = ''
    for ch in my_string:
        if ch.islower():
            answer += ch.upper()
        else:
            answer += ch.lower()
    return answer
