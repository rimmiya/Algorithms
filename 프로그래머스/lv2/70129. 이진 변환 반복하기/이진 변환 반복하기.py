def solution(s):
    answer = [0,0]
    zero = 0
    
    while(len(s) != 1):
        zero = s.count("0")
        answer[1] += zero
        answer[0] += 1
        s = format(len(s)-zero, 'b')
        
    return answer