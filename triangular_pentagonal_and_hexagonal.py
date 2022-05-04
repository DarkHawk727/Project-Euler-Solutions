# Arjun Sarao


def main():
    def generate_triangular_numbers(n: int) -> list:
        """
        Generates the first n triangular numbers.
        :param n: The number of triangular numbers to generate.
        :return: A list of the first n triangular numbers.
        """
        return [i * (i + 1) // 2 for i in range(n)]

    def generate_pentagonal_numbers(n: int) -> list:
        """
        Generates the first n pentagonal numbers.
        :param n: The number of pentagonal numbers to generate.
        :return: A list of the first n pentagonal numbers.
        """
        return [i * (3 * i - 1) // 2 for i in range(n)]

    def generate_hexagonal_numbers(n: int) -> list:
        """
        Generates the first n hexagonal numbers.
        :param n: The number of hexagonal numbers to generate.
        :return: A list of the first n hexagonal numbers.
        """
        return [i * (2 * i - 1) for i in range(n)]

    triangular_numbers = set(generate_triangular_numbers(100_000))
    pentagonal_numbers = set(generate_pentagonal_numbers(100_000))
    hexagonal_numbers = set(generate_hexagonal_numbers(100_000))

    print(triangular_numbers & pentagonal_numbers & hexagonal_numbers)


if __name__ == "__main__":
    main()
