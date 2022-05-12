# Arjun Sarao

from tqdm import tqdm


def main():
    number_lengths = {}
    digits = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    teens = [
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    tens = [
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]

    def convert_num_to_word(num: int) -> str:
        """
        Converts a number to a word.
        params: num - an integer to convert to a word
        returns: the word representation of the number
        """
        if 1 <= num <= 9:
            return digits[num - 1]
        elif 10 <= num <= 19:
            return teens[num - 10]
        elif 20 <= num <= 99:
            if num % 10 == 0:
                return tens[(num // 10) - 2]
            else:
                return tens[(num // 10) - 2] + "-" + digits[num % 10 - 1]
        elif 100 <= num <= 999:
            if num % 100 == 0:
                return digits[num // 100 - 1] + " hundred"
            else:
                return (
                    digits[num // 100 - 1]
                    + " hundred and "
                    + convert_num_to_word(num % 100)
                )
        elif num == 1000:
            return "one thousand"

    for i in tqdm(range(1, 1001)):
        number_lengths[i] = len(
            convert_num_to_word(i).replace(" ", "").replace("-", "")
        )

    # Sort the dictionary by the length of the number
    sorted_by_length = sorted(number_lengths.items(), key=lambda x: x[1])
    for i in sorted_by_length:
        print(f"{i[0]} - {i[1]}")
    print(f"Sum: {sum(number_lengths.values())}")


if __name__ == "__main__":
    main()
