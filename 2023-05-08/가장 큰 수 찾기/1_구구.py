def solution(array):
    answer = []
    answer.append(max(array))
    answer.append(array.index(max(array)))
    return answer
  
#이렇게 줄이자..
def solution(array):
    answer = [max(array), array.index(max(array))]
    return answer
