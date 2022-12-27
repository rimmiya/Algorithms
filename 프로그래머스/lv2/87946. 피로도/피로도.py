import itertools

def solution(k, dungeons):
    answer = 0
    
    perm = list(itertools.permutations(dungeons, len(dungeons)))
    
    for p in perm:
        maxi = 0
        tmp = k
        for i in p:
            if tmp >= i[0]:
                tmp -= i[1]
                maxi += 1
            else:
                break
        if maxi == len(dungeons):
            return maxi
        elif maxi > answer:
            answer = maxi

    return answer