import math

def isprime(b):
    if b == 1:
        return 0
    for i in range(2, int(math.sqrt(b))+1):
        if b % i == 0:
            return 0
    return 1

def solution(n, k):
    result = 0
    bin = ''
    
    while n > 0:
        bin = str(n%k) + bin
        n //= k
        
    bin = list(bin.split("0"))
    
    for b in bin:
        if not b: continue
        else:
            result += isprime(int(b))
        
    return result