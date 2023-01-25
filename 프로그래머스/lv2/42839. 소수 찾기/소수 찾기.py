import itertools
import math

def solution(numbers):
    answer = 0
    perm = []

    for i in range(1, len(numbers)+1):
        for p in list(itertools.permutations(numbers,i)):
            perm.append(int(''.join(p)))
            
    perm = list(set(perm))
    
    for p in perm:
        if p < 2:
            continue
        for i in range(2, int(math.sqrt(p))+1):
            if p % i == 0:
                break
        else:
            answer += 1
    return answer