def solution(n, words):
    used = []
    
    for i, w in enumerate(words):
        if not used:
            used.append(w)
            continue
        if (w in used) or (used[-1][-1] != w[0]):
            return [(i % n) + 1, (i // n) + 1]
        used.append(w)
    return [0, 0]