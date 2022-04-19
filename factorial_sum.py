# Arjun Sarao


def main():
    def factorial(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
    NUM = factorial(100)
    print(sum(int(i) for i in str(NUM)))


if __name__ == "__main__":
    main()
