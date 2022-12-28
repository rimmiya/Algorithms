def solution(n):
    way = [0, 1, 2]
    
    if n <= 2:
        return way[n]
    
    for i in range(3, n+1):
        way.append(((way[i-2] % 1234567) + (way[i-1] % 1234567)) % 1234567)
        
    return way[-1]