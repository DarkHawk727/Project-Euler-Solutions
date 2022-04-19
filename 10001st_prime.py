# Arjun Sarao


def main():
    NUM = 1000000  # Selected arbitrarily
    primes = [True] * NUM
    primes[0] = primes[1] = False
    for i in range(2, int(NUM**0.5) + 1):
        if primes[i]:
            for j in range(i * i, NUM, i):
                primes[j] = False
    print([i for i in range(NUM) if primes[i]][10000])


if __name__ == "__main__":
    main()
     