from itertools import permutations

def is_prime(num):
    if num == 0 or num == 1:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

def solution(numbers):
    pn = []
    for i in range(1, len(numbers)+1):
        for num in list(permutations(list(numbers),i)):
            pn.append(int(''.join(num)))

    pn = list(set(pn))
    answer = 0
    for p in pn:
        answer += is_prime(p)
    return answer