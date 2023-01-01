def dp(triangle, i, j, result):
    left = result[i][j] + triangle[i+1][j]
    right = result[i][j] + triangle[i+1][j+1]
    result[i+1][j] = max(result[i+1][j], left)
    result[i+1][j+1] = max(result[i+1][j+1], right)
    return result
    
def solution(triangle):
    answer = 0
    result = [[0] * i for i in range(1, len(triangle) + 1)]

    result[0] = triangle[0]
    
    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i+1])-1):
            result = dp(triangle, i, j, result)
            
    return max(result[-1])