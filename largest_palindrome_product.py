# Arjun Sarao


def main():
    palindromic_numbers = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            if str(i * j) == str(i * j)[::-1]:
                palindromic_numbers.append(i * j)
    print(max(palindromic_numbers))


if __name__ == "__main__":
    main()
