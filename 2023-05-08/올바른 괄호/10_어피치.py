# 230513
# [PGS] 올바른 괄호 / 레벨2 / 9분
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):

    # list형을 스택으로 사용
    stack = []

    for e in s:
        if e == '(':
            stack.append(e)
        else:   # e == ')'인 경우
            if not stack:   # stack 비어 있으면 False 리턴
                return False
            else:           # stack 비어 있지 않으면 마지막 요소 pop
                stack.pop()

    # '(()(' 같은 경우 존재하므로 마지막에도 조건문 추가
    return False if stack else True
