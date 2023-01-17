def dfs(n, computers, visited, i):
    visited[i] = True
    for j in range(n):
        if computers[i][j] == 1:
            computers[i][j] = 0
            dfs(n, computers, visited, j)
    
def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            dfs(n, computers, visited, i)
            answer += 1
    return answer
