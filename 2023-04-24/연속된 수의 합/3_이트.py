# 시도 1: while sum(answer) != total
# [-1, 0, 1] 3개가 만족되기 전에 0에서 total이 만족

def solution(num, total):
    answer = []
    if num % 2 == 0:
        left = total // num
        right = left + 1
        answer.extend([left, right])
        while len(answer) != num:
            left = left - 1
            right = right + 1
            answer.extend([left, right])
    else:
        med = total / num
        answer.append(med)
        i = 1
        while len(answer) != num:
            answer.extend([med - i, med + i])
            i += 1
    answer.sort()
    return answer