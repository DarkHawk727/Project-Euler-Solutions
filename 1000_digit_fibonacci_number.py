# Arjun Sarao
from tqdm import tqdm


def main():
    def calculate_fibonacci_number(n: int) -> int:
        """
        Calculates the nth Fibonacci number.
        """
        a, b = 0, 1
        while n > 1:
            a, b = a + b, a
            n -= 1
        return a

    for num in tqdm(range(1, 5000)):
        if len(str(calculate_fibonacci_number(num))) == 1000:
            print(
                f"The index of the first fibonacci number with 1000 digits is: the {num-1} number whose value is: {calculate_fibonacci_number(num)}.\n"
            )
            break


if __name__ == "__main__":
    main()
