# Arjun Sarao

from tqdm import tqdm


def main():
    distinct_powers = set()
    for a in tqdm(range(2, 101)):
        for b in range(2, 101):
            if a**b not in distinct_powers:
                distinct_powers.add(a**b)
    print(f"There are {len(distinct_powers)} distinct powers.")


if __name__ == "__main__":
    main()
