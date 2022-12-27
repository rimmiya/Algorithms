def solution(data, col, row_begin, row_end):
    answer = 0
    
    data.sort(key=lambda x:(x[col-1], -x[0]))
    
    mod_list = []
    for i in range(row_begin-1, row_end):
        tmp = 0
        for s in data[i]:
            tmp += s % (i+1)
            
        mod_list.append(tmp)
        
    answer = mod_list[0]
    
    for i in range(1, len(mod_list)):
        answer ^= mod_list[i]
        
    return answer