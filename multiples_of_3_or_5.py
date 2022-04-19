# Arjun Sarao


def main():
    nums = []
    for num in range(1, 1000):
        if num % 3 == 0 or num % 5 == 0:
            nums.append(num)
    print(sum(nums))


if __name__ == "__main__":
    main()
