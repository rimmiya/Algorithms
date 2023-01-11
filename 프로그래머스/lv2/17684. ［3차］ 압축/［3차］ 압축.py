from string import ascii_uppercase

def solution(msg):
    answer = []
    alpha = [i for i in ascii_uppercase]
    s = ''
    for i in range(len(msg)-1):
        s += msg[i]
        if s+msg[i+1] in alpha:
            continue
        else:
            alpha.append(s+msg[i+1])
            answer.append(alpha.index(s)+1)
            s = ''
    if s + msg[-1] in alpha:
        answer.append(alpha.index(s+msg[-1])+1)
    return answer
