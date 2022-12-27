def solution(s):
    S = list(map(int, s.split(" ")))
    return str(min(S)) + " " + str(max(S))