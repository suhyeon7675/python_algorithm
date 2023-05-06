def solution(my_string):
    answer = ''

    st = my_string.lower()
    arr = []

    for ch in st:
        arr.append(ch)

    arr = sorted(arr)

    for a in arr:
        answer += a

    return answer