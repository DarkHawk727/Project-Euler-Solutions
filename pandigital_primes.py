# Arjun Sarao
# !TODO
from tqdm import tqdm, trange
from itertools import chain, combinations


def main():
    def is_prime(n: int) -> bool:
        """
        Checks if a number is prime.
        :param n: The number to check.
        :return: True if n is prime, False otherwise.
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def generate_pandigital_nums() -> list:
        """
        Generates all pandigital numbers.
        :return: A list of all pandigital numbers.
        """
        digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        return list(chain.from_iterable(combinations(digits, r) for r in range(11)))



    pandigital_number_list = generate_pandigital_nums()
    print(pandigital_number_list)



if __name__ == "__main__":
    main()
