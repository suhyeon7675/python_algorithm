# 230521
# [PGS] 베스트앨범 / 레벨3 / 검색 도움 받음
# https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []

    dict1 = {}
    dict2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dict1:  # key: 장르, value: [(고유번호, 재생횟수)]
            dict1[g] = [(i, p)]
        else:
            dict1[g].append((i, p))

        if g not in dict2:  # key: 장르, value: 재생횟수 합산
            dict2[g] = p
        else:
            dict2[g] += p

    for (k, v) in sorted(dict2.items(), key=lambda x: x[1], reverse=True):  # 재생횟수 많은 장르 먼저
        for (i, p) in sorted(dict1[k], key=lambda x: x[1], reverse=True)[:2]:   # 장르 내에서 재생횟수 많은 2가지만
            answer.append(i)

    return answer
