import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        try:
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        except IndexError:
            return -1
        answer += 1

    return answer

# import heapq

# def solution(scoville, k):
#     heap = []
#     for num in scoville:
#         heapq.heappush(heap, num)

#     mix_cnt = 0
#     while heap[0] < k:
#         try:
#             heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
#         except IndexError:
#             return -1
#         mix_cnt += 1

#     return mix_cnt