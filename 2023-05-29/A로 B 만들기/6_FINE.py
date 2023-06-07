'''
TypeError: 'str' object does not support item assignment

=> 문자열은 변경 불가능한 자료형이다.

-> 문자열을 변경하려면, 문자열을 리스트로 변환한 후, 리스트의 요소를 변경하고, 리스트를 다시 문자열로 변환해야 한다.
또는
-> replace() 메서드를 사용한다. 문자열에서 특정 문자를 다른 문자로 치환할 때 사용한다.

'''
def solution(before, after):
    for i in range(len(before)):
        for j in range(len(after)):
            if before[i] == after[j]:
                after = after.replace(after[j], ' ')
                break
            elif j == len(after)-1:
                return 0
    return 1