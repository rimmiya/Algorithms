def solution(answers):
    answer = []
    
    a_list = [1, 2, 3, 4, 5]
    b_list = [2, 1, 2, 3, 2, 4, 2, 5]
    c_list = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    rank = [0, 0, 0]
    
    for i in range(len(answers)):
        if a_list[i % len(a_list)] == answers[i]:
            rank[0] += 1
        if b_list[i % len(b_list)] == answers[i]:
            rank[1] += 1
        if c_list[i % len(c_list)] == answers[i]:
            rank[2] += 1
            
    for i, r in enumerate(rank):
        if r == max(rank):
            answer.append(i+1)
    return answer