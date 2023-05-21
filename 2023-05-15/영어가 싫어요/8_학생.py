def solution(numbers):
    a = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num= ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    answer = ''
    what = ''
    for i in numbers:
        what += i
        for i in range(10):
            if what == a[i]:
                answer += num[i]
                what = ''
    return int(answer)