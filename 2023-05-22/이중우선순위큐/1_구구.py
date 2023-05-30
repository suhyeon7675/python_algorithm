import heapq

def solution(operations):
    hq = []
    for e in operations:
            command = e.split(' ')
            if command[0] == 'I':
                heapq.heappush(hq, int(command[1]))
            else:
                if int(command[1]) < 0:
                    if len(hq) > 0:
                        heapq.heappop(hq)
                else:
                    if len(hq) > 0:
                        hq.pop()
    hq.sort()
    if len(hq) > 0:
        return [hq[-1],hq[0]]
    else:
        return [0,0]
