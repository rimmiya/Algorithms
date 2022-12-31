# 1806 부분합

n, s = map(int, input().split())
seq = list(map(int, input().split()))

low = 0
high = 0
sum = 0
cnt = 100001

while True:
    if sum >= s:
        cnt = min(cnt, (high - low))
        sum -= seq[low]
        low += 1
    elif (low == n) or (high == n):
        break
    else:
        sum += seq[high]
        high += 1


if cnt > 100000:
    print(0)
else:
    print(cnt)
