# Arjun Sarao

from tqdm import tqdm


def main():
    def check_prime(n: int) -> bool:
        """
        Returns True if n is a prime number.
        params: n - an integer to check if it is a prime number
        returns: True if n is a prime number, False otherwise
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    value, value_a, value_b, count = 1000, 0, 0, 0
    for a in tqdm(range(-value, value + 1)):
        for b in range(-value, value + 1):
            length = 0
            while check_prime(length ** 2 + a * length + b):
                length += 1

            if length > count:
                value_a, value_b = a, b
                count = length

    print(
        f"{value_a} x {value_b} = {value_a*value_b} is the product of the coefficients of the quadratic equation that produces the maximum number of primes for consecutive values of n, starting with n = 0."
    )
    print(f"The maximum number of primes is {count}.")


if __name__ == "__main__":
    main()
