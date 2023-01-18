def solution(citations):
    answer = 0
    
    citations = sorted(citations, reverse=True)
    
    for i in range(1,len(citations)+1):
        cnt = 0
        for j in range(len(citations)):
            if i <= citations[j]:
                cnt += 1
        if cnt >= i:
            answer = i
    return answer