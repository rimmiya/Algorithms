def solution(cap, n, deliveries, pickups):
    answer = 0      
    s_delivery = [-1]
    s_pickup = [-1]
    
    for i in range(n):
        if deliveries[i] > 0: s_delivery.append(i)
        if pickups[i] > 0: s_pickup.append(i)
    
    d = s_delivery.pop()
    p = s_pickup.pop()

        
    while d > -1 or p > -1:
        answer += 2 * (max(d, p) + 1)
        # delivery
        d_left = cap
        while d_left and s_delivery:
            if deliveries[d] > d_left:
                deliveries[d] -= d_left
                d_left = 0
            else:
                d_left -= deliveries[d]
                deliveries[d] = 0
                d = s_delivery.pop()

        p_left = cap
        while p_left and s_pickup:
            # pickup
            if pickups[p] > p_left:
                pickups[p] -= p_left
                p_left = 0
            else:
                p_left -= pickups[p]
                pickups[p] = 0
                p = s_pickup.pop()

    return answer