def solution(array):
    answer = 0
    digit_list = []
    
    for num in array:
        if num > 9: #2-digit인 경우 각각 slice해서 리스트에 추가
            digit_list += [int(i) for i in str(num)]
        else:
            digit_list.append(num)
            
    for digit in digit_list:
        if digit == 7:
            answer += 1
    return answer
