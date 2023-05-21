# 해시로 푸는 방법이 생각나지 않아서 리스트 인덱스와 startswith()를 사용하여 풀었다.
def solution(phone_book):
    phone_book = sorted(phone_book) #배열을 정렬하면 특정 원소 뒤에 이를 접두어로 포함하는 원소가 올 수 있다.
    ans = 1
    for i in range(1,len(phone_book)):
        if ans == 0 : break                 #앞에서 접두어를 찾은 경우 멈추기 위함
        elif phone_book[i].startswith(phone_book[i-1]): 
            ans = 0
    return bool(ans) #ans를 'true'/'false'로 하면 오답처리됨.


# 해시로 푼 다른 사람 코드
def solution(phone_book): # ["123","456","789"]
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
        
    for phone_number in phone_book:  # phone_number = '123'
        temp = ""
        for number in phone_number:  # '123' 에서 '1'->'2'->'3' 순으로 반복
            temp += number           # temp = '1'->'12'->'123' 순으로 
            if temp in hash_map and temp != phone_number:  # hash_map 에 있는지 확인. temp != phone_number로 자기 자신은 제외
                return False
    return True
