l = list(map(int,input().split()))
r = []
sum = 0
for i in l:
    sum += i
    r.append(sum)
print(r)
