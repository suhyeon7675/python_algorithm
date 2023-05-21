def solution(genres, plays):
    answer = []
    
    music_dict = dict(zip(plays,genres))
    sum_dict = {}
    print(music_dict)
            
    # 장르순위
    for k, v in zip(genres, plays):
        sum_dict[k] = sum_dict.get(k,0) + int(v)
    sortsum = sorted(sum_dict.items(), key=lambda x:x[1], reverse = True)
    
    #인덱스로 정렬
    arr = []
    for idx, (genre,play) in enumerate(zip(genres, plays)):
        arr.append([idx, genre, play])
    sortarr=sorted(arr,key=lambda x:x[2], reverse=True)
    
    #장르합 높은 것부터, 두개까지 인덱스 저장하고 다음장르로 넘어가서 다시 저장
    for big_genre, _ in sortsum:
        cnt=0
        for i in sortarr:
            if cnt==2:
                break
            if i[1]==big_genre:
                answer.append(i[0])
                cnt+=1
    

    return answer