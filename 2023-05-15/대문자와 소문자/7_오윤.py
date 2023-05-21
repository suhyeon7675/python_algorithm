def solution(my_string):
    answer = ''
    for s in my_string:
        if s.isupper():
            answer += s.lower()
        else:
            answer += s.upper()
    return answer
  
  
  # 파이썬 대소문자 확인 .isupper() .islower()
  # 파이썬 대소문자 변환 .upper() .lower()
  
  # 다른 사람 풀이 
  # 파이썬의 .swapcase() 는 문자열의 대소문자 변환을 해주는 메서드
  def solution(my_string):
    return my_string.swapcase()
