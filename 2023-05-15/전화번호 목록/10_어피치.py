# 230521
# [PGS] 전화번호 목록 / 레벨2 / 20분
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    # sort하기 때문에 바로 다음에 오는 숫자랑만 비교하면 된다
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return True
