def solution(my_string, num1, num2):
    #string을 list로 바꾸면 인덱스 접근이 편하다
    answer = list(my_string)

    answer[num1], answer[num2] = answer[num2], answer[num1]
    
    # print(answer)
    
    return ''.join(answer)