# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a

from math import gcd

def solution(arr):
    answer = arr[0]

    for i in range(len(arr)):
        answer = (answer * arr[i]) // gcd(answer, arr[i])
    return answer