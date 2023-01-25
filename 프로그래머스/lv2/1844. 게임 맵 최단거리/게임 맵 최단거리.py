from collections import deque
def solution(maps):
    answer = 0
    
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    n = len(maps)
    m = len(maps[0])
    
    check = [[-1 for _ in range(m)] for _ in range(n)]
    check[0][0] = 1
    
    queue = deque()
    queue.append([0,0])
    
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            dx = a + d[i][0]
            dy = b + d[i][1]
            
            if -1 < dx < n and -1 < dy < m:
                if maps[dx][dy] == 1:
                    if check[dx][dy] == -1:
                        check[dx][dy] = check[a][b] + 1
                        queue.append([dx, dy])
    answer = check[-1][-1]
    return answer