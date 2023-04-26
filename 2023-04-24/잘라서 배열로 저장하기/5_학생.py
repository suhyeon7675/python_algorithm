#잘라서 배열로 저장하기
def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str)//n):
        str = my_str[(i*n):(i+1)*n] 
        answer.append(str)
    if(len(my_str) % n != 0):
        answer.append(my_str[((i+1)*n):] )
    return answer
