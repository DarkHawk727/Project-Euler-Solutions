# Arjun Sarao


def main():
    NUMBER = 600851475143
    factors, not_prime_factors = [], []
    # Find ALL factors of NUMBER
    for num in range(2, int(NUMBER**0.5) + 1):
        if NUMBER % num == 0:
            factors.append(num)

    # Find all non-prime factors of NUMBER
    for factor in factors:
        for num in range(2, int(factor**0.5) + 1):
            if factor % num == 0:
                not_prime_factors.append(factor)

    # Find the largest prime factor
    print(max(set(factors) - set(not_prime_factors)))


if __name__ == "__main__":
    main()
