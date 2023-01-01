def solution(k, tangerine):
    answer = 0
    
    size = {}
    
    for t in tangerine:
        if t not in size:
            size[t] = 0
        size[t] += 1
        
    size = dict(sorted(size.items(), key = lambda x : x[1], reverse = True))
    cnt = 0
    
    for key in size.keys():
        cnt += size[key]
        answer += 1
        if cnt >= k:
            return answer