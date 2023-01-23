def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        can_tree = []
        for t in tree:
            if t in skill:
                can_tree.append(skill.index(t))

        for i in range(len(can_tree)):
            if i != can_tree[i]:
                break
        else:
            answer += 1
    return answer