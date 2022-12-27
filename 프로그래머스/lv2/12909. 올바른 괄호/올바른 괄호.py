def solution(s):
    answer = True
    
    stack = []
    
    for i in s:
        if i == "(":
            stack.append(i)
        elif not stack and i == ")":
            return False
        else:
            stack.pop()
    if not stack:
        return True
    else:
        return False