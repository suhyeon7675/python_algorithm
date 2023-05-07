def solution(s1, s2):
    s3 = s1 + s2
    answer = len(s3) - len(set(s3))
    return answer
