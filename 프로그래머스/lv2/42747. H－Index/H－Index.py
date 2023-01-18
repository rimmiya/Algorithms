def solution(citations):
    citations.sort()
    
    for i in range(len(citations)):
        h = len([x for x in citations if x >= (i+1)])
        # print(h, i+1, len(citations) - (i+1))
        if h < (i+1) or len(citations) - h > (i+1):
            return i
    return len(citations)

# 테스트 1 〉	통과 (14.29ms, 10.2MB)
# 테스트 2 〉	통과 (38.67ms, 10.2MB)
# 테스트 3 〉	통과 (39.08ms, 10.2MB)
# 테스트 4 〉	통과 (33.96ms, 10.2MB)
# 테스트 5 〉	통과 (38.60ms, 10.1MB)
# 테스트 6 〉	통과 (48.24ms, 10.3MB)
# 테스트 7 〉	통과 (11.77ms, 10.3MB)
# 테스트 8 〉	통과 (0.43ms, 10.2MB)
# 테스트 9 〉	통과 (0.72ms, 10.1MB)
# 테스트 10 〉	통과 (9.61ms, 10.2MB)
# 테스트 11 〉	통과 (74.99ms, 10.2MB)
# 테스트 12 〉	통과 (1.79ms, 10.2MB)
# 테스트 13 〉	통과 (48.16ms, 10.2MB)
# 테스트 14 〉	통과 (40.08ms, 10.2MB)
# 테스트 15 〉	통과 (88.14ms, 10.2MB)
# 테스트 16 〉	통과 (0.01ms, 10.2MB)