# Arjun Sarao


def main():
    def calculate_champernownes_constant(n: int) -> str:
        """
        Calculates the Champernownes constant for a given number.
        :param n: The number to calculate the Champernownes constant of.
        :return: The Champernownes constant of n.
        """
        champernownes_constant = "0."
        for i in range(1, n + 1):
            champernownes_constant += str(i)
        return champernownes_constant

    champerownes_constant = calculate_champernownes_constant(1_000_000)
    # We add 1 to the length of the string to account for the decimal point.
    ans = (
        int(champerownes_constant[1 + 1])
        * int(champerownes_constant[10 + 1])
        * int(champerownes_constant[100 + 1])
        * int(champerownes_constant[1_000 + 1])
        * int(champerownes_constant[10_000 + 1])
        * int(champerownes_constant[100_000 + 1])
        * int(champerownes_constant[1_000_000 + 1])
    )
    print(f"The product of the digits of the Champernownes constant is {ans}.")


if __name__ == "__main__":
    main()
