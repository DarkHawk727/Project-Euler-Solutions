# Arjun Sarao

from tqdm import trange


def main():
    convert = lambda n: sorted((str(n)))

    for i in trange(1, 200_000):
        if (
            convert(i)
            == convert(i * 2)
            == convert(i * 3)
            == convert(i * 4)
            == convert(i * 5)
            == convert(i * 6)
        ):
            print(f"{i} is a permuted multiple.")
            break


if __name__ == "__main__":
    main()
