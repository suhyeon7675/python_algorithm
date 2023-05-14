# 230502
# [PGS] 7의 개수 / 레벨0 / 14분
# https://school.programmers.co.kr/learn/courses/30/lessons/120912

def solution(array):
    # 나의 풀이
    '''
    answer = 0

    for e in array:
        str_e = str(e)
        for i in range(len(str_e)):
            if str_e[i] == '7':
                answer += 1

    return answer
    '''

    # 다른 사람 풀이
    # str(list) 형변환하면 '[7, 77]' 이런식으로 괄호까지 값으로 들어감
    # count() => 문자열, 리스트 내에서 찾고 싶은 문자 개수 반환
    return str(array).count('7')
