# 문제 이해 처음부터 틀림! 어차피 한 번만 등장한 문자를 answer에 추가하므로 중복제거를 위한 set은 무의미함 ㅋ
def solution(s):
    s_set = set(s) #answer에 중복 저장 제외하기 위한 set 사용
    answer = ''
    for i in sorted(s_set):
        if s.count(i) == 1:
            answer += i
    return answer
  

  # 다른 풀이
  def solution(s):
    answer = ''.join(sorted(ch for ch in s if s.count(ch) == 1))
    return answer
  
