# 230429
# [PGS] 잘라서 배열로 저장하기 / 레벨0 / 8분40초
# https://school.programmers.co.kr/learn/courses/30/lessons/120913

def solution(my_str, n):

    # 나의 풀이
    answer = []

    for i in range(len(my_str)):
        if (i % n) == 0:
            answer.append(my_str[i:i+n])    # 슬라이싱은 초과해도 에러나지 않음

    return answer
