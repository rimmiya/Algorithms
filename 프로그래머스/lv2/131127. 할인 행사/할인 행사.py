from collections import Counter

def solution(want, number, discount):
    answer = 0
    can = {}
    for i in range(len(want)):
        can[want[i]] = number[i]
    for i in range(len(discount)-9):
        tmp = dict(Counter(discount[i:10+i]))
        if can == tmp:
            answer += 1
    return answer