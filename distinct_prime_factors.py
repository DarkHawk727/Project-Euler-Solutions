# Arjun Sarao

from tqdm import tqdm


def main():
    def distinct_prime_factors(n: int) -> list:
        """
        Returns a list of distinct prime factors of n.
        params: n - an integer to find prime factors of
        returns: a list of distinct prime factors of n
        Prime factorization algorithm taken from https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
        """
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        for i in range(3, int(n ** 0.5) + 1, 2):
            while n % i == 0:
                factors.append(i)
                n //= i
        if n > 2:
            factors.append(n)
        return set(factors)

    for n in tqdm(range(1, 200_000)):
        if len(distinct_prime_factors(n)) == 4:
            if len(distinct_prime_factors(n + 1)) == 4:
                if len(distinct_prime_factors(n + 2)) == 4:
                    if len(distinct_prime_factors(n + 3)) == 4:
                        print(
                            f"{n}, {n + 1}, {n + 2}, and {n + 3} all have four distinct prime factors."
                        )
                        break


if __name__ == "__main__":
    main()
