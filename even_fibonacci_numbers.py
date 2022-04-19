# Arjun Sarao
from math import sqrt


def main():
    def generate_fibonacci_numbers(n: int) -> list:
        fibonacci_numbers = [1, 1]
        for i in range(2, n):
            fibonacci_numbers.append(
                fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2]
            )
        return fibonacci_numbers

    nums = []
    for num in generate_fibonacci_numbers(33):
        if num % 2 == 0:
            nums.append(num)
    print(sum(nums))


if __name__ == "__main__":
    main()
