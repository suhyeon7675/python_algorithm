def solution(phone_book):
    phone_book.sort()
    for i,p in enumerate(phone_book):
        copy_book = ''.join(phone_book[i+1:i+2])[0:len(p)]
        if p == copy_book:
            return False
    return True

def solution(phone_book):
    phone_book.sort()
    for i,p in enumerate(phone_book):
        copy_book = [h[0:len(p)] for h in phone_book[i+1:i+2]]
        if p in copy_book:
           return False
    return True

#def solution(phone_book):
#    phone_book.sort()
#    for i in range(len(phone_book)-1):
#        if phone_book[i] in phone_book[i+1]:
#            return False
#    return True
