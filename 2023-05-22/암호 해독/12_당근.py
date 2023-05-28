def solution(cipher, code):
    
    answer = ''
    
    for n in range(1, len(cipher)//code+1) :
    
        answer_n = cipher[code*n - 1]
        answer = answer + answer_n
    
    return answer
