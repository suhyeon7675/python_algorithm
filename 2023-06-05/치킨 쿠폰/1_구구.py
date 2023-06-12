def solution(chicken):
    answer = 0
    coupon = 0
    while chicken != 0:        
        coupon += chicken % 10
        chicken //= 10
        answer += chicken
    while coupon >= 10:
        coupon -= 10
        answer += 1
        coupon += 1
    return answer
