def solution(bin1, bin2):
    answer = ''
    
    # bin1 = "100001"
    # bin2 = "1010101"
    
    
    if bin1 == str(0):
        return bin2
    elif bin2 == str(0):
        return bin1
    elif bin2 ==str(0) and bin1 == str(0):
        return 0
    
    temp = '0'+str(int(bin1)+int(bin2))
    
    # print(temp)
    
    up = 0
    num = 0

    for t in reversed(temp):
        num = int(t)
        num += up
        up = 0
        
        if num >1:         
            num -= 2
            up += 1     
        else:
            up=0
        # print(num, up)
        answer = str(num)+answer
        
    if answer[0] == '0':
        # print('c')
        answer = answer.replace('0','',1)
   
    
    return answer