# Arjun Sarao

from tqdm import tqdm


def main():
    def is_prime(n: int) -> bool:
        """
        Determines if a number is prime.
        :param n: The number to check.
        :return: True if the number is prime, False otherwise.
        """
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    count = 0
    for i in tqdm(range(2, 1_000_000)):
        if is_prime(i):
            s = str(i)
            if all(is_prime(int(s[j:] + s[:j])) for j in range(len(s))):
                count += 1

    print(f"The number of circular primes below 1,000,000 is {count}.")


if __name__ == "__main__":
    main()
