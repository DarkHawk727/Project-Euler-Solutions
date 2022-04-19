# Arjun Sarao
from math import factorial


def main():
    def calculate_combinations(n: int, r: int) -> int:
        """
        Calculates the number of combinations of n choose r.
        """
        return factorial(n) // (factorial(r) * factorial(n - r))

    m = 20
    n = 20
    print(
        f"There are {calculate_combinations(m+n, n)} paths from the top left to the bottom right of a {m}x{n} grid."
    )


if __name__ == "__main__":
    main()
