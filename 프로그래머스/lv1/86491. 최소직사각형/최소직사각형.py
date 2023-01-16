def solution(sizes):
    w, h = 0, 0
    
    for s in sizes:
        if s[0] < s[1]:
            s[0], s[1] = s[1], s[0]
        w = max(w, s[0])
        h = max(h, s[1])
    return w * h