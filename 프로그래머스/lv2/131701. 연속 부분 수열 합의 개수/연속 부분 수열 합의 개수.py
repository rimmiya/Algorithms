def solution(elements):
    answer = 0
    seq = set()
    length = len(elements)
    elements += elements
    for i in range(1,length+1):
        for j in range(length):
            seq.add(sum(elements[j:i+j]))
    return len(seq)