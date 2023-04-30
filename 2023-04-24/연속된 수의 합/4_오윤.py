def solution(num, total):
    answer = []
    s = total//num
    while True:
        answer = [s+i for i in range(num)]
        if sum(answer) > total :
            s -= 1
            continue
        elif sum(answer) < total : 
            s += 1
            continue
        else: break
    return answer
  
  # 다른 사람의 간단한 풀이를 봐도 이해가 안가서 따라할 수가 없다.......
