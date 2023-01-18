def solution(sentence):
    stack = []

    for s in sentence:
        if stack and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)
    if stack:
        return 0
    else:
        return 1
    