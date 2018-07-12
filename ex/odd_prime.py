odds = {n for n in range(51, 100, 2)}  # set comprehension
# print(odds)

primes = set()  # empty set
for n in range(51, 100, 2):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            break
    else:
        primes.add(n)

print( sorted(odds - primes))
