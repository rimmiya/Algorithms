def solution(n, t, m, p):
    answer = []
    max_cnt = t * (m-1) + p
    st = ['0']
    i = 1
    while len(st) <= max_cnt + t:
        tmp = ''
        j = i
        while j > 0:
            if j % n < 10:
                tmp += str(j%n)
            else:
                tmp += 'ABCDEF'[(j%n)%10]
            j //= n
        st.extend(list(tmp[::-1]))
        i += 1
    for k in range(t):
        answer.append(st[k*m+((p-1)%m)])
    return ''.join(answer)