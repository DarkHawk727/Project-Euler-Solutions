# Arjun Sarao
from tqdm import tqdm


def main():
    def generate_triangular_number(n: int) -> int:
        """
        Generates the nth triangular number.
        """
        return n * (n + 1) // 2

    def calculate_number_of_divisors(n: int) -> int:
        """
        Calculates the number of divisors of n.
        """
        divisors = 0
        for i in range(1, int(n ** 0.5 + 1)):
            if n % i == 0:
                divisors += 2
        return divisors

    for num in tqdm(range(100001)):
        if calculate_number_of_divisors(generate_triangular_number(num)) >= 500:
            print(
                f"The first number with over 500 divisors is: the {num} whose value is: {generate_triangular_number(num)}.\n"
            )
            break


if __name__ == "__main__":
    main()
