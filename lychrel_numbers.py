# Arjun Sarao


def main():
    def is_lychrel(n: int) -> bool:
        for _ in range(50):
            n += int(str(n)[::-1])
            if str(n) == str(n)[::-1]:
                return False
        return True

    print(sum(1 for n in range(1, 10000) if is_lychrel(n)))


if __name__ == "__main__":
    main()
