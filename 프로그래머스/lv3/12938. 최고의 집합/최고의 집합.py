def solution(n, s):
    answer = []
    
    if n > s:
        return [-1]

    r = s // n
    q = s % n
        
    for _ in range(n - q):
        answer.append(r)
    for _ in range(q):
        answer.append(r+1)
    return answer