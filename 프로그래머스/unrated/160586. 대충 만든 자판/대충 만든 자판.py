def solution(keymap, targets):
    answer = []
    
    for word in targets:
        times = 0
        
        for w in word:
            flag = False
            time = 101
            for key in keymap:
                if w in key:
                    time = min(key.index(w)+1, time)
                    flag = True
            if not flag:
                times = -1
                break
            times += time
        answer.append(times)
    return answer