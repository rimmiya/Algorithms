def solution(n):
    answer = n+1
    n_b = format(n, 'b').count('1')

    while(1):
        if n_b == format(answer, 'b').count('1'):
            return answer
        else:
            answer += 1