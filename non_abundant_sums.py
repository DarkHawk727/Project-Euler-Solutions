# Arjun Sarao

from tqdm import tqdm


def main():
    def calculate_sum_of_divisors(n: int) -> int:
        """
        Calculates the sum of the divisors of a number.
        :param n: The number to calculate the sum of the divisors of.
        :return: The sum of the divisors of n.
        """
        sum_of_divisors = 0
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                if n == n / i:
                    sum_of_divisors += i
                else:
                    sum_of_divisors += i + n // i
        return sum_of_divisors

    limit = 28123
    abundant_numbers = []
    for i in tqdm(range(12, limit)):
        if calculate_sum_of_divisors(i) > i:
            abundant_numbers.append(i)
    non_abundant_sums = [
        i
        for i in range(1, limit)
        if not any(i - j in abundant_numbers for j in abundant_numbers)
    ]
    print(sum(non_abundant_sums))


if __name__ == "__main__":
    main()
