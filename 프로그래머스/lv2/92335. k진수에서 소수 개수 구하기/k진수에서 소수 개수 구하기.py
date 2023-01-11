import math

def isprime(num):
    if num == 1: return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def conv(n, k):
    s = ''
    while n:
        s = str(n%k) + s
        n //= k
    return s

def solution(n, k):
    answer = 0
    num = list(conv(n, k).split("0"))
    
    for i in num:
        if not i: continue
        elif isprime(int(i)): answer += 1
    return answer