import math

def solution(fees, records):
    answer = []
    
    parking = {}
    pay = {}
    
    for r in records:
        r = r.split()
        car = int(r[1])
        time = list(map(int, r[0].split(":")))
        if r[2] == "IN":
            parking[car] = time
            if car not in pay.keys():
                pay[car] = 0
        elif r[2] == "OUT":
            if parking[car][1] > time[1]:
                total = (time[0] - parking[car][0] - 1) * 60 + (60 + time[1] - parking[car][1])
            else:
                total = (time[0] - parking[car][0]) * 60 + (time[1] - parking[car][1])
            del parking[car]
            pay[car] += total
            
    pay = dict(sorted(pay.items()))
    
    for car in pay.keys():
        if car in parking.keys():
            pay[car] += (23 - parking[car][0]) * 60 + (59 - parking[car][1])
        
        if math.ceil((pay[car] - fees[0]) / fees[2]) < 0:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((pay[car] - fees[0]) / fees[2]) * fees[3])
    return answer