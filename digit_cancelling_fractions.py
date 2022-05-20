# Arjun Sarao

from tqdm import tqdm
from math import gcd


def main():
    dp, np = 1, 1

    for c in tqdm(range(1, 10)):
        for d in range(1, c):
            for n in range(1, d):
                if (n * 10 + c) * d == (c * 10 + d) * n:
                    np *= n
                    dp *= d

    print(f"{dp / gcd(np, dp)}")


if __name__ == "__main__":
    main()
