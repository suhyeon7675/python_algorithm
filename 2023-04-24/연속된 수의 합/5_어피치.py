# 230430
# [PGS] 연속된 수의 합 / 레벨0 / 15분5초
# https://school.programmers.co.kr/learn/courses/30/lessons/120923

def solution(num, total):
    # 몫과 나머지 이용
    answer = []
    share, remainder = divmod(total, num)

    if remainder == 0:
        x = (num-1) // 2
        for i in range(share-x, share+x+1):
            answer.append(i)
    else:
        for i in range(share-remainder+1, share+remainder+1):
            answer.append(i)

    return answer
