
def solution(phone_book):
    answer = True
    
    for i in range(0, len(phone_book)):
        for j in range(0, len(phone_book)):
            if len(phone_book[i]) < len(phone_book[j]) and i != j:
                if phone_book[i] == phone_book[j][0:len(phone_book[i])]:
                    answer = False
                    return answer
    
    return answer
