# 230518
# [PGS] 영어가 싫어요 / 레벨0 / 5분
# https://school.programmers.co.kr/learn/courses/30/lessons/120894

def solution(numbers):
    numbers_en = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(len(numbers_en)):
        numbers = numbers.replace(numbers_en[i], str(i))
    return int(numbers)
