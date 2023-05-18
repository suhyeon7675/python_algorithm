def solution(numbers):
    numbWords = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(0, len(numbWords)):
        if numbWords[i] in numbers:
            numbers = numbers.replace(numbWords[i], str(i))
    
    return int(numbers)
