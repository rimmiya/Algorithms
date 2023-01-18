def solution(brown, yellow):
    for h in range(brown):
        for w in range(brown):
            if w >= h:
                if (w - 2) * (h - 2) == yellow:
                    if 2 * (w + h) - 4 == brown:
                        return [w, h]