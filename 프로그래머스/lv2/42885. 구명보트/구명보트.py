def solution(people, limit):
    answer = 0
    people.sort()
    s = 0
    e = len(people) - 1
    
    while(s <= e):
        if (len(people) >= 2) and (people[s] + people[e] <= limit):
            answer += 1
            s += 1
            e -= 1
        else:
            answer += 1
            e -= 1
    return answer