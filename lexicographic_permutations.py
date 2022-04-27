# Arjun Sarao

from itertools import permutations


def main():
    perms = list(permutations(range(10)))

    perms.sort()
    millionth = "".join([str(i) for i in perms[1000000 - 1]])
    print(f"The 1,000,000th lexographic permutation is: {millionth}.")


if __name__ == "__main__":
    main()
