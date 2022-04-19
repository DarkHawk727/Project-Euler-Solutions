# Arjun Sarao


def main():
    def prime_sieve(n: int) -> list:
        """
        Sieve of Eratosthenes
        params:
            n: int
        returns:
            list of primes
        """
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False
        return [i for i in range(n) if primes[i]]

    print(sum(prime_sieve(2000000)))


if __name__ == "__main__":
    main()
