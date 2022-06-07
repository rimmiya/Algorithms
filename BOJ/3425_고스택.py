# G3 : 3425_고스택
# 구현, 자료 구조, 스택
import sys

input = sys.stdin.readline


def exec(commands, num):
    stack = [num]
    for cmd in commands:
        if cmd[:3] == "NUM":
            stack.append(int(cmd[4:]))
        elif not stack:
            return "ERROR"
        elif cmd == "POP":
            stack.pop()
        elif cmd == "INV":
            stack[-1] *= -1
        elif cmd == "DUP":
            stack.append(stack[-1])
        elif len(stack) == 1:
            return "ERROR"
        elif cmd == "SWP":
            stack[-2], stack[-1] = stack[-1], stack[-2]
        elif cmd == "ADD":
            tmp = stack.pop() + stack.pop()
            if abs(tmp) > 10**9:
                return "ERROR"
            stack.append(tmp)
        elif cmd == "SUB":
            tmp = -stack.pop() + stack.pop()
            if abs(tmp) > 10**9:
                return "ERROR"
            stack.append(tmp)
        elif cmd == "MUL":
            tmp = stack.pop() * stack.pop()
            if abs(tmp) > 10**9:
                return "ERROR"
            stack.append(tmp)
        elif cmd == "DIV":
            a = stack.pop()
            b = stack.pop()
            if a == 0:
                return "ERROR"
            tmp = abs(b) // abs(a)
            if abs(tmp) > 10**9:
                return "ERROR"
            if (a < 0 and b > 0) or (a > 0 and b < 0):
                tmp = -tmp
            stack.append(tmp)
        elif cmd == "MOD":
            a = stack.pop()
            b = stack.pop()
            if a == 0:
                return "ERROR"
            tmp = abs(b) % abs(a)
            if abs(tmp) > 10**9:
                return "ERROR"
            if b < 0:
                tmp = -tmp
            stack.append(tmp)
        else:
            return "ERROR"

    if len(stack) == 1:
        return stack[0]
    return "ERROR"


while True:
    commands = []
    while True:
        cmd = input().strip()
        if cmd == 'QUIT':
            quit()
        if cmd == 'END':
            break
        commands.append(cmd)

    n = int(input())
    for _ in range(n):
        num = int(input())
        print(exec(commands, num))

    print()
    input()
