from collections import deque

def solution(operations):
    
    max_queue = deque()
    
    for i in operations:
        command = i.split()
        if command[0] == "I":
            max_queue.append(int(command[1]))
            max_queue = deque(sorted(max_queue, reverse = True))
        elif command[0] == "D":
            if max_queue:
                if command[1] == "1":
                    max_queue.popleft()
                elif command[1] == "-1":
                    max_queue.pop()
        
    if not max_queue:
        return [0,0]
    
    return [max_queue.popleft(), max_queue.pop()]