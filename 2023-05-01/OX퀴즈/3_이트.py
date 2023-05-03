def solution(quiz):
    answer = []
    for q in quiz:
        equal = q.find("=")
        Z = int(q[equal+1:])
        plus = q.find("+")
        if plus == -1:
            minus = q.find("-", 1)
            X = int(q[:minus-1])
            Y = int(q[minus+2:equal-1])
            if X - Y == Z:
                answer.append("O")
            else:
                answer.append("X")
        else:
            X = int(q[:plus-1])
            Y = int(q[plus+2:equal-1])
            if X + Y == Z:
                answer.append("O")
            else:
                answer.append("X")
    return answer