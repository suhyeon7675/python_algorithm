# 딕셔너리를 이용한 풀이
# 반복문 안에 s += n의 위치 아주 중요! 전에도 이거때문에 시간걸림
def solution(numbers):
    num_dict = {'zero': '0', "one": '1', "two": '2',
             "three": '3', "four": '4', "five": '5', "six": '6',
             "seven": '7', "eight": '8', "nine": '9',}
    answer = ''
    s = ''
    for n in numbers: 
        s += n
        if s in num_dict:
            answer += num_dict[s]
            s = ''
        # else : s += n   #원래 작성했던 위치 => "eightnine" 의 경우 eight 다음 n은 저장 x ine으로 저장되어서 문제.
    return int(answer)
  
  # 위의 코드대로 작성하는 것은 모든 key가 중복되지 않기 때문. 즉, one과 onek가 함께 존재하면 k가 나오기 전에 처리해버린다는 문제가 있음.
  
  # 다른 풀이
  def solution(numbers):
    dic = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    i=0
    for word in dic:
        numbers = numbers.replace(word, str(i))
        i+=1
    return int(numbers)
