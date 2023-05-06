def solution(babbling):
    answer = 0
    
    list_can = ['aya', 'ye', 'woo', 'ma']
    
    
    for ba in babbling:
        for can in list_can:

            ba = ba.replace(can,'.')
        
        if ba.replace('.','') == '':
            answer += 1

    
    return answer


# 너무 어려웠다..... 풀이 보고 풀었음 나중에 다시 풀어보기.
# replace함수로 해당하는 문자열을 치환해서 있는지 확인하는 방식.