def solution(my_string):
    s = my_string.split()
    answer = int(s[0])
    for i in range(1,len(s)):
        if s[i] == "-":
            answer -= int(s[i+1])
        elif s[i] == "+":
            answer += int(s[i+1])
        
    return answer
  
  
# 다른 사람 코드 참고
def solution(my_string): 
    return sum(int(i) for i in my_string.replace(" - "," + -").split(" + "))
