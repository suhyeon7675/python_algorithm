def solution(num, total):
    answer = []
    d=0
    # 1 ~ (num - 1)의 합을 구함
    for i in range(1, num) : 
        d += i
    # 첫번째 값을 얻는다
    start_val = (total - d) // num 
    # 첫번째 값부터 1씩 증가한 마지막 값을 i로 반환해 list에 담는다
    answer = [i for i in range(start_val, start_val+num)]

    return answer
