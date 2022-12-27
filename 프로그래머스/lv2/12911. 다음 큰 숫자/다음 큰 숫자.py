def solution(n):
    answer = n
    n_b = format(n, 'b').count('1')

    while(1):
        answer += 1
        if n_b == format(answer, 'b').count('1'):
            return answer