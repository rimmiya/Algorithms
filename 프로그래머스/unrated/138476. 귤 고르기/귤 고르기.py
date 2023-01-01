def solution(k, tangerine):
    answer = 0
    
    size = {}
    
    for t in tangerine:
        if t in size.keys():
            size[t] += 1
        else:
            size[t] = 1
    size = dict(sorted(size.items(), key = lambda x : x[1], reverse = True))
    
    for key in size.keys():
        k = k - size[key]
        answer += 1
        if k <= 0:
            return answer