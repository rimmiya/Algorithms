def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x:x[2])
    road = set([costs[0][0]])
    
    while len(road) != n:
        for c in costs:
            # 이미 연결
            if c[0] in road and c[1] in road:
                continue
            # 연결 한 것과 연결
            if c[0] in road or c[1] in road:
                road.update([c[0], c[1]])
                answer += c[2]
                break
    return answer