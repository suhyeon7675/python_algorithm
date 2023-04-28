# [PRG]잘라서 배열로 저장하기
def solution(my_str, n):
    answer = []
    
    while len(my_str) > 0:  # while문 안에서 매개변수 my_str을 n개씩 잘라낼 것이기 때문에 my_str의 길이가 0보다 큰 동안만 반복한다.
        if len(my_str) > n:  # 잘라내는 동안 my_str의 길이가 n보다 작아지면 인덱스 에러가 발생할 수도 있으므로 조건문으로 상황을 나눠준다.
            answer.append(my_str[:n])  # 슬라이싱으로 n개씩 자르기
            my_str = my_str[n:]  # 슬라이싱으로 answer에 추가한 부분 삭제
        else:                       
            answer.append(my_str)
            break

    return answer


# TIL : 슬라이싱을하면 인덱스가 len(my_str)을 초과하는 경우가 생길거라 생각했는데 슬라이싱은 초과해도 에러가 나지 않는다고 한다...!!!!
