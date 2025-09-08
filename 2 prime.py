x = int(input())
primeCount=0
for i in range(2,x+1):
    n = i
    fact = 0
    for j in range(1, n+1):
        if n % j == 0:
            fact += 1
    if fact == 2:
        primeCount += 1
print(primeCount)               
