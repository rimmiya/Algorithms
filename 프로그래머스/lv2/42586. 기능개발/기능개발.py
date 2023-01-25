import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    
    done = []
    for p, s in zip(progresses, speeds):
        done.append(math.ceil((100 - p) / s))

    i, j = 0, 1
    while i < len(done) and j < len(done):
        if done[i] < done[j]:
            answer.append(j - i)
            i = j
        j += 1
    answer.append(j - i)
    return answer