# Arjun Sarao

from tqdm import tqdm


def main():
    def digit_sum(num: int) -> int:
        return sum(int(d) for d in str(num))

    maximum_digit_sum = -999_999
    for a in tqdm(range(1, 100)):
        for b in range(1, 100):
            num = a ** b
            if digit_sum(num) > maximum_digit_sum:
                maximum_digit_sum = digit_sum(num)

    print(f"The maximum digit sum is {maximum_digit_sum}")


if __name__ == "__main__":
    main()
