from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    for city in cities:
        city = city.lower()
        if not city in cache:
            if (len(cache) < cacheSize) or (not cache):
                cache.append(city)
            else:
                cache.popleft()
                cache.append(city)
            answer += 5
        else:
            answer += 1
            if len(cache) == 1:
                continue
            else:
                cache.remove(city)
                cache.append(city)
    return answer