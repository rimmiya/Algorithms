import math

def prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    num = ""
    
    while n > 0:
        r = n % k
        if r == 0 and n > k:
            if len(num) > 0 and int(num) != 1 and prime(int(num)):
                answer += 1
            num = ""
        if r != 0 and n > k:
            num = str(r) + num
        if r == 0 and n < k:
            if len(num) > 0 and int(num) != 1 and prime(int(num)):
                answer += 1
        elif r != 0 and n < k:
            num = str(n) + num
            if prime(int(num)):
                answer += 1
                return answer
        n //= k
    return answer