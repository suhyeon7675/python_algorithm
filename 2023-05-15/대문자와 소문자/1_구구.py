def solution(my_string):
    for idx, s in enumerate(my_string):
        if s.islower():
            tmp = list(my_string)
            tmp[idx] = s.upper()
            my_string = "".join(tmp)
        else:
            tmp = list(my_string)
            tmp[idx] = s.lower()
            my_string = "".join(tmp)
    return my_string

#이렇게 풀걸..
def solution(my_string):
	answer = ''
	for idx, s in enumerate(my_string):
			if s.islower():
					answer += s.upper()
			else:
					answer += s.lower()
	return answer
