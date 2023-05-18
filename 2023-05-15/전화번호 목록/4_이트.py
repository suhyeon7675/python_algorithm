# 정확성 테스트 1, 5, 13, 14 실패
# 효율성 테스트 3, 4 시간 초과
def solution(phone_book):
    answer = True
    temp = phone_book.copy()
    for p in phone_book:
        temp.remove(p)
        for t in temp:
            if p in t:
                return False
        temp.append(p)
    return answer

# ["119", "97674223", "5524421119"] 접두사만 False 처리해야 하므로 True
# 효율성 테스트 3, 4 시간 초과
def solution(phone_book):
    pb = sorted(phone_book, key=lambda x: len(x))
    for i in range(len(pb)):
        for j in range(i+1, len(pb)):
            if pb[i] in pb[j][:len(pb[i])]:
                return False
    return True

# chatGPT
def solution(phone_book):
    phone_book.sort() # 전화번호를 정렬하여 접두어 관계가 인접하도록 함

    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i+1]: # 현재 번호가 다음 번호의 접두어인 경우
            return False

    return True