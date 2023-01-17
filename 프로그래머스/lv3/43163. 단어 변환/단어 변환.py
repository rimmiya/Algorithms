from collections import deque

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    visited = [False for _ in range(len(words))]
    queue = deque([[begin, 0]])
    
    while queue:
        cur, depth = queue.popleft()
        
        if cur == target:
            return depth
        
        for i, w in enumerate(words):
            diff = 0
            if not visited[i]:
                for j in range(len(cur)):
                    if cur[j] != w[j]:
                        diff += 1
                if diff == 1:
                    visited[i] = True
                    queue.append([w, depth+1])