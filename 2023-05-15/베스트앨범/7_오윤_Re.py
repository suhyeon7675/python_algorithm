# 풀지 못한 문제*** 
# 답안 출처 : https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL3-%EB%B2%A0%EC%8A%A4%ED%8A%B8%EC%95%A8%EB%B2%94-Python

def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {} # 장르의 총 재생 횟수. 조건1) 장르 별 재생 횟수가 가장 많은 순

    for i, (g, p) in enumerate(zip(genres, plays)):  # => i,(genres[i] , plays[i]) 인 셈.
        if g not in dic1:
            dic1[g] = [(i, p)]  # dic1에 장르를 키로 인덱스, 재생 횟수 저장
        else:
            dic1[g].append((i, p))  # 이미 dic1에 있는 장르면 인덱스, 재생 횟수 추가

        if g not in dic2:
            dic2[g] = p    # dic2에 장르를 키로 재생 횟수 저장
        else:
            dic2[g] += p   # dic2에 장르를 키로 장르의 총 재생 횟수 

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True): # 장르 별 재생 횟수 내림차순으로 순회 => (장르, 전체 횟수)
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]: # dic1에서 k(장르)에 해당 하는 각 재생 횟수 내림차순
            answer.append(i) # 내림차순으로 특정 장르의 고유번호 정렬 됨. 반복 => 모든 장르 완성

    print(answer)
    return answer
