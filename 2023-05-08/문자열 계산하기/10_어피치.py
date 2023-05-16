# 230512
# [PGS] 문자열 계산하기 / 레벨0 / 7분
# https://school.programmers.co.kr/learn/courses/30/lessons/120902

def solution(my_string):
    # 연산자가 여러개일 수 있음

    # eval 함수는 보안 취약하므로 사용 지양!
    return eval(my_string)

    # 다른 사람 풀이
    # 뺄셈을 덧셈과 음수로 변경한 뒤, 덧셈 기준 split
    '''
    x = my_string.replace('- ', '+ -').split(' + ')
    return sum(map(int, x))
    '''
