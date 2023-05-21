def solution(numbers):
    engList = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for idx, e in enumerate(engList):
        numbers = numbers.replace(e, str(idx))
    return int(numbers)
