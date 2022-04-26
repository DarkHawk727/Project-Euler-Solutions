# Arjun Sarao

from tqdm import tqdm


def main():
    def calculate_sum_of_divisors(n: int) -> int:
        """
        Calculates the sum of the divisors of n.
        """
        sum_of_divisors = 1
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                sum_of_divisors += i + n // i
        return sum_of_divisors

    amicable_numbers = set()
    for a in tqdm(range(1, 10001)):
        b = calculate_sum_of_divisors(a)
        if a == calculate_sum_of_divisors(b):
            print(f"The sum of the divisors of {a} is {b}.")
            amicable_numbers.add(a)
            amicable_numbers.add(b)
    print(sum(amicable_numbers))


if __name__ == "__main__":
    main()
