# Arjun Sarao

from tqdm import tqdm


def main():
    def calculate_sum_of_divisors(n: int) -> int:
        """
        Calculates the sum of the divisors of a number.
        :param n: The number to calculate the sum of the divisors of.
        :return: The sum of the divisors of n.
        Algorithm taken from https://www.geeksforgeeks.org/sum-of-all-proper-divisors-of-a-natural-number/
        """
        sum_of_divisors = 0
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                if n == n / i:
                    sum_of_divisors += i
                else:
                    sum_of_divisors += i + n // i
        return sum_of_divisors

    limit = 28_123
    abundant_numbers, non_abundant_numbers = set(), set()
    for i in tqdm(range(12, limit)):
        if calculate_sum_of_divisors(i) > i:
            abundant_numbers.add(i)
    
    for i in tqdm(range(1, limit+1)):
        for j in abundant_numbers:
            if i - j not in abundant_numbers:
                non_abundant_numbers.add(i)
    print(f"The sum of all the positive integers which cannot be written as the sum of two abundant numbers is {sum(set(non_abundant_numbers))}.")


if __name__ == "__main__":
    main()
