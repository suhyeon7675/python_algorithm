import math
from collections import deque
def solution(jobs):
    answer = []
    jobs.sort()
    q = deque(jobs)
    s, c = q.popleft()
    end = s + c
    answer.append(end - s)
    i = 1
    while i < len(jobs):
        pos = sorted([[s, c] for s, c in q if s <= end], key=lambda x: x[1])
        if pos != []:
            q.remove(pos[0])
            end += pos[0][1]
            answer.append(end - pos[0][0])
        else:
            s, c = q.popleft()
            end = s + c
            answer.append(c)
        i += 1
    return math.floor(sum(answer)/len(answer))