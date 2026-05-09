# Q3: First N prime numbers

N = int(input("Enter N: "))

primes = []

num = 2
while len(primes) < N:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    num += 1

total = sum(primes)
avg = total / N

print("\nPrime Numbers:", primes)
print("Sum:", total)
print("Average:", avg)