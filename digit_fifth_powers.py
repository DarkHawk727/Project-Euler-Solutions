# Arjun Sarao

from tqdm import tqdm


def main():
    def calc_fifth_power(n: int) -> int:
        return sum([int(i) ** 5 for i in str(n)])

    nums = []
    for num in tqdm(range(2, 500000)):
        if calc_fifth_power(num) == num:
            print(f"{num} is a fifth power.")
            nums.append(num)

    print(f"The sum of these numbers is {sum(nums)}.")


if __name__ == "__main__":
    main()
