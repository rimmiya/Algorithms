def solution(n, left, right):
    answer = []
    
    x = left // n
    y = left % n
    
    for i in range(left, right+1):
        if x > y:
            answer.append(x+1)
        elif x <= y:
            answer.append(y+1)
    
        if y < n-1:
            y += 1
        else:
            x += 1
            y = 0
        
    return answer