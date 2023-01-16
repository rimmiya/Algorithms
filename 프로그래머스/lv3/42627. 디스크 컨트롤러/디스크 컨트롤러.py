import heapq

def solution(jobs):
    heap = []
    answer = 0
    
    start, now = -1, 0
    i = 0
    
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        if heap:
            d, r = heapq.heappop(heap)
            start = now
            now += d
            answer += now - r
            i += 1
        else:
            now += 1
            
    return answer // len(jobs)