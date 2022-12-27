import math

def solution(n, words):
    answer = [0,0]
    used = []

    for i, w in enumerate(words):
        if not used:
            used.append(w)
            continue
        if (w in used) or (used[-1][-1] != w[0]):
            if (i+1) % n == 0:
                answer[0] = n
            else:
                answer[0] = (i+1) % n
            answer[1] = math.ceil((i+1) / n)
            break
        used.append(w)
    return answer