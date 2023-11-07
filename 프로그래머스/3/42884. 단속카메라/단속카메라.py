def solution(routes):
    answer = 1
    routes.sort()
    
    camera = routes[0]
    
    for r in routes[1:]:
        if r[0] <= camera[1]:
            camera = [r[0], min(camera[1], r[1])]
        else:
            camera = r
            answer += 1
    return answer