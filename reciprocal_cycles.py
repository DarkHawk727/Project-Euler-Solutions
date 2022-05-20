# Arjun Sarao

from tqdm import tqdm


def main():
    def convert_to_decimal(numerator: int, denominator: int) -> str:
        """
        Convert a fraction to decimal with the repeating sequence
        params:
            numerator: int
            denominator: int
        return:
            str
        Algorithm taken from: https://stackoverflow.com/questions/36529512/convert-fraction-to-string-with-repeating-decimal-places-in-brackets
        """

        result = [str(numerator // denominator) + "."]
        subresults = [numerator % denominator]
        numerator %= denominator
        while numerator != 0:
            numerator *= 10
            result_digit, numerator = divmod(numerator, denominator)
            result.append(str(result_digit))

            if numerator not in subresults:
                subresults.append(numerator)

            else:
                result.insert(subresults.index(numerator) + 1, "(")
                result.append(")")
                break
        return "".join(result)

    fractions = {}

    for denominator in tqdm(range(1, 1001)):
        expansion = convert_to_decimal(1, denominator)
        fractions["1/" + str(denominator)] = [expansion, len(expansion) - 2]

    maximum = max(fractions.values(), key=lambda x: x[1])
    print(
        f"The fraction with the longest recurring cycle is {maximum[0]} with {maximum[1]} digits."
    )


if __name__ == "__main__":
    main()
