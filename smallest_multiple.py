# Arjun Sarao
from math import gcd, lcm
from functools import reduce


def main():
    ans = reduce(lcm, range(1, 21))
    print(ans)


if __name__ == "__main__":
    main()
