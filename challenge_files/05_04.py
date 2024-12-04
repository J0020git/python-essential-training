def allPrimesUpTo(num):
    primes = [2]
    for number in range(3, num):
        for prime in primes:
            if prime > int(number**0.5):
                primes.append(number)
                break
            if number % prime == 0:
                break
    return primes


print(allPrimesUpTo(100))
