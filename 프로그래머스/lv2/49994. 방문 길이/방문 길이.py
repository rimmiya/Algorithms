def solution(dirs):
    now = [0, 0]
    way = set()
    for d in dirs:
        if d == 'U':
            if -5 <= now[0]+1 <= 5:
                way.add(((now[0], now[1]), (now[0]+1, now[1])))
                way.add(((now[0]+1, now[1]), (now[0], now[1])))
                now[0] += 1
        elif d == 'D':
            if -5 <= now[0]-1 <= 5:
                way.add(((now[0], now[1]), (now[0]-1, now[1])))
                way.add(((now[0]-1, now[1]), (now[0], now[1])))
                now[0] -= 1
        elif d == 'R':
            if -5 <= now[1]+1 <= 5:
                way.add(((now[0], now[1]), (now[0], now[1]+1)))
                way.add(((now[0], now[1]+1), (now[0], now[1])))
                now[1] += 1
        elif d == 'L':
            if -5 <= now[1]-1 <= 5:
                way.add(((now[0], now[1]), (now[0], now[1]-1)))
                way.add(((now[0], now[1]-1), (now[0], now[1])))
                now[1] -= 1
    return len(way) / 2