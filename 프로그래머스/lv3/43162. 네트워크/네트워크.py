def dfs(n, computers, x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if computers[x][y] == 1:
        computers[x][y] = 0
        # 상 하 좌 우
        dfs(n, computers, x - 1, y)
        dfs(n, computers, x + 1, y)
        dfs(n, computers, x, y - 1)
        dfs(n, computers, x, y + 1)
        return True
    return False
    
def solution(n, computers):
    answer = 0
    for i in range(n):
        for j in range(n):
            if dfs(n, computers, i, j) == True:
                answer += 1
    return answer