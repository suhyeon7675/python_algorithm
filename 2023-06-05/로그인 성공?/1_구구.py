def solution(id_pw, db):
    if id_pw in db:
        return 'login'
    for user in db:
        if id_pw[0] == user[0]:
            return 'wrong pw'
    return 'fail'
