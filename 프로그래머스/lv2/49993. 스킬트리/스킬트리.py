def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        i = 0
        for t in tree:
            if t in skill:
                if skill[i] != t:
                    break
                else:
                    i +=1
        else:
            answer += 1
    return answer