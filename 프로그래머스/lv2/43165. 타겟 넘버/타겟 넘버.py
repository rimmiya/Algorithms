# BFS
from collections import deque

def solution(numbers, target):
    answer = 0
    
    if sum(numbers) == target:
        return 1
    
    queue = [[numbers[0], 0], [-numbers[0], 0]]
    
    while queue:
        num, idx = queue.pop()
        idx += 1
        if idx < len(numbers):
            queue.append([num + numbers[idx], idx])
            queue.append([num - numbers[idx], idx])
        else:
            if num == target:
                answer += 1
    return answer
        