def solution(s):
    answer = ''
    list_ = [0 for i in range(26)] #알파벳 개수
    for i in list(s):
        for j in range(26):
            if (i == chr(j+97)):
                list_[j] += 1
    for i in range(26):
        if list_[i] == 1:
            answer += chr(i+97)
    return ''.join(map(str, sorted(answer)))