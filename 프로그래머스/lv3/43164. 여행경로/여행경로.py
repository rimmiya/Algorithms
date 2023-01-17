def solution(tickets):
    answer = []
    stack = ["ICN"]
    route = dict()
    for fr, to in tickets:
        if fr in route.keys():
            route[fr].append(to)
        else: route[fr] = [to]

    for k in route.keys():
        route[k] = sorted(route[k], reverse=True)
        
    while stack:
        top = stack[-1]
        if top not in route.keys() or len(route[top]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(route[top].pop())
    return answer[::-1]