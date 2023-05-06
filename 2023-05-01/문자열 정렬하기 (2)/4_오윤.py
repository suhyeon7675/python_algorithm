def solution(my_string):
    answer = ''
    for i in sorted(my_string.lower()):
        answer += i
    return answer
  
# 다른 사람 간단 풀이 : .join
# return ''.join(sorted(my_string.lower())
