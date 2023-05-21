def solution(phone_book):
    answer = True
    
    #정렬을 통해 앞자리 같은것끼리 맞추기
    phone_book.sort()
    # print(phone_book)
    
    for i in range(len(phone_book)-1):
        # 접두사가 같은지 비교
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False        
    
    return answer