x = int(input())
l = []
for n in range (1, x*4):
    fact = 0
    for i in range (1, n+1):
        if n % i == 0:
            fact += 1
    if fact == 2:
        l.append(n)
    if (len(l) == x):
        break
print(sum(l))


