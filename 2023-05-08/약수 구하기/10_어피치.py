# 230512
# [PGS] 약수 구하기 / 레벨0 / 9분30초
# https://school.programmers.co.kr/learn/courses/30/lessons/120897

def solution(n):
    # 제곱근과 집합을 사용 => 매개변수 값 커졌을 때 훨씬 빠름
    answer = set()
    sqrt_val = int(n ** 0.5)

    for i in range(1, sqrt_val + 1):
        share, remainder = divmod(n, i)
        if remainder == 0:
            answer.add(i)
            answer.add(share)

    return sorted(list(answer))
