# Arjun Sarao


def main():
    big_numbers = []
    with open("associated_files/big_number.txt", "r") as f:
        for line in f:
            big_numbers.append(int(line.strip()))
    print(str(sum(big_numbers))[:10])


if __name__ == "__main__":
    main()
