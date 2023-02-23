def solution(n):
    fib = [0, 1, 2]
    
    if n <= 2:
        return fib[n]
    
    for i in range(3, n+1):
        fib.append((fib[i - 1] + fib[i - 2])%1000000007)
    return fib[n]