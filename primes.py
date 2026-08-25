def get_primes_under_1000():
    """
    Returns a list of all prime numbers less than 1000 in Python.
    """
    primes = []
    for num in range(2, 1000):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

if __name__ == "__main__":
    print(get_primes_under_1000())
