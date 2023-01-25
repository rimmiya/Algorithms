from collections import deque

def solution(priorities, location):
    answer = 0
    
    d = deque([(i,p) for i,p in enumerate(priorities)])
    
    while True:
        cur = d.popleft()
        if any(cur[1] < q[1] for q in d):
            d.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer