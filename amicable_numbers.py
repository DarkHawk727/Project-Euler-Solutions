# Arjun Sarao

from tqdm import tqdm


def main():
    def sum_of_divisors(n: int) -> int:
        """
        Calculates the sum of the divisors of n.
        params: n - an integer to find the sum of the divisors of
        returns: the sum of the divisors of n
        """
        sum_of_divisors = 0
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                if n == n / i:
                    sum_of_divisors += i
                else:
                    sum_of_divisors += i + n // i
        return sum_of_divisors

    amicable_numbers = []
    for a in tqdm(range(1, 10001)):
        b = sum_of_divisors(a)
        if a != b and sum_of_divisors(b) == a:
            amicable_numbers.append((a, b))

    print(
        f"The sum of the amicable numbers is: {sum([i[0] for i in amicable_numbers])}."
    )


if __name__ == "__main__":
    main()
