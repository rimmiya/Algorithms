def solution(s):
    answer = ''
    
    S = list(map(int, s.split(" ")))
    answer = str(min(S)) + " " + str(max(S))
    return answer