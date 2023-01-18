def solution(people, limit):
    answer = 0
    people = sorted(people)
    boat = 0
    i = 0
    j = len(people) - 1
    while i < j:
        boat += people[j]
        if limit - boat < people[i]:
            answer += 1
            j -= 1
        else:
            while i < j:
                boat += people[i]
                i += 1
                if limit - boat < people[i]:
                    answer += 1
                    j -= 1
                    break
        boat = 0
    if i == j:
        answer += 1
    return answer