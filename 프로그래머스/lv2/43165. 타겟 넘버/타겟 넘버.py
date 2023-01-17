# BFS
# def solution(numbers, target):
#     answer = 0
    
#     bfs = [[numbers[0], 0], [-1 * numbers[0], 0]]
    
#     while bfs:
#         num, idx = dfs.pop()
#         idx += 1
#         if idx < len(numbers):
#             bfs.append([num + numbers[idx], idx])
#             bfs.append([num - numbers[idx], idx])
#         else:
#             if num == target:
#                 answer += 1
#     return answer

# DFS
def solution(numbers, target):
    answer = dfs(numbers, target, 0)
    return answer 

def dfs(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        if sum(numbers) == target:
            return 1
        else:
            return 0
    else:
        answer += dfs(numbers, target, depth+1)
        numbers[depth] *= -1
        answer += dfs(numbers, target, depth+1)
    return answer