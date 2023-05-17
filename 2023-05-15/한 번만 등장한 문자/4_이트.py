from collections import Counter
def solution(s):
    answer = ''
    for key, value in Counter(s).items():
        if value == 1:
            answer += key
    return ''.join(sorted(answer))