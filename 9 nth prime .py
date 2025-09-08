n = int(input("Enter n: "))   
count = 0
num = 1
while True:
    num += 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        count += 1
        if count == n:
            print(f"{n}th prime number is: {num}")
            break
