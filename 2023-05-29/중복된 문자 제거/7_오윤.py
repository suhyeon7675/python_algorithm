# 헷갈린 문법
# 리스트에서 요소 찾기
# 리스트 문자열로 출력하기
def solution(my_string):
    answer = []
    for str in my_string:
        if str not in answer:
            answer.append(str)
    return "".join(answer)
