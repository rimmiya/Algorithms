def solution(s):
    answer = ''
    s = list(s.lower())
    tmp = ''
    for i in range(len(s)):
        if (s[i] == " ") or (i == len(s)-1):
            tmp += s[i]
            answer += tmp[0].upper() + tmp[1:]
            tmp = ''
        # elif i == len(s)-1:
        #     tmp += s[i]
        #     answer += tmp[0].upper() + tmp[1:]
        else:
            tmp += s[i]
    return answer
