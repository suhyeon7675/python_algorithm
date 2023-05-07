# 230502
# [PGS] 문자열 정렬하기 (2) / 레벨0 / 3분40초
# https://school.programmers.co.kr/learn/courses/30/lessons/120911

def solution(my_string):
    # sorted는 리스트나 문자열을 오름차순으로 정렬한 후 리스트 형태로 반환 => join() 사용한 이유
    return ''.join(sorted(my_string.lower()))
