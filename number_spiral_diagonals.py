# Arjun Sarao


def main():
    def calculate_sum(n: int) -> int:
        """
        Calculates the sum of the diagonals of a nxn spiral.
        Formula was found on:
        https://www.educative.io/edpresso/how-to-solve-the-number-spiral-diagonals-problem
        """
        n = (1001 - 1) / 2
        answer = (3 + 2 * n * (8 * n * n + 15 * n + 13)) / 3
        return int(answer)

    print(f"The sum of the diagonals of a 1001x1001 spiral is {calculate_sum(1001)}")


if __name__ == "__main__":
    main()
