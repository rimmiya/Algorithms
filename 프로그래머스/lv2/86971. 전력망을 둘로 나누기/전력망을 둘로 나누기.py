def dfs(graph, v, visited, check_link):
    visited[v] = True
    cnt = 1
    
    for i in graph[v]:
        if not visited[i] and check_link[v][i]:
            cnt += dfs(graph, i, visited, check_link)
    return cnt

def solution(n, wires):
    answer = 100
    
    graph = [[] for _ in range(n+1)]
    check_link = [[True] * (n+1) for _ in range(n+1)]
    
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    for v1, v2 in wires:
        visited = [False] * (n+1)
        
        check_link[v1][v2] = False
        n1 = dfs(graph, v1, visited, check_link)
        n2 = dfs(graph, v2, visited, check_link)
        check_link[v1][v2] = True
        
        answer = min(answer, abs(n1 - n2))
    return answer