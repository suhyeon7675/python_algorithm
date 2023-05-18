# 정확성 테스트 2, 15 실패
from collections import Counter, defaultdict
def solution(genres, plays):
    answer = []
    d = defaultdict(list)
    for i in range(len(genres)):
        d[genres[i]].append(plays[i])
    gs = sorted(d, key=lambda x: sum(d[x]), reverse=True)
    ps = []
    for g in gs:
        ps.extend(sorted(d[g], reverse=True)[:2])
    for p in ps:
        answer.append(plays.index(p))
    return answer

# chatGPT
from collections import Counter, defaultdict
def solution(genres, plays):
    answer = []
    d = defaultdict(list)
    for i in range(len(genres)):
        d[genres[i]].append((plays[i], i))  # (재생 횟수, 고유 번호) 형태로 저장

    # 장르별 재생 횟수의 합을 기준으로 내림차순 정렬
    sorted_genres = sorted(d, key=lambda x: sum(play for play, _ in d[x]), reverse=True)

    for genre in sorted_genres:
        # 장르 내에서 재생 횟수를 기준으로 내림차순 정렬하고 최대 2개까지 선택
        sorted_songs = sorted(d[genre], key=lambda x: x[0], reverse=True)[:2]
        for play, index in sorted_songs:
            answer.append(index)  # 고유 번호를 answer에 추가

    return answer