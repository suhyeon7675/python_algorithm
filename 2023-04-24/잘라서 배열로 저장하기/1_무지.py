def solution(my_str, n):
    answer=[]
    # 문자열을 list로 변환
    my_strList = list(my_str)
    print(my_strList)
    if(len(my_strList) % n == 0):
        number = len(my_strList) // n
    else:
        number = len(my_strList) // n + 1 

    for i in range(number):
        answer.insert(i, ''.join(s for s in my_strList[n*i:n*(i+1)]))
    return answer
