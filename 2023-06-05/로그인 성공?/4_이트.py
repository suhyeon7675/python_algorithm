def solution(id_pw, db):
    for key, value in db:
        if key == id_pw[0]:
            if value == id_pw[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"