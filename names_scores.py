# Arjun Sarao

from tqdm import tqdm


def main():
    with open("names.txt", "r") as f:
        names = f.read().replace('"', "").split(",")

    names.sort()
    answer = 0

    for name in tqdm(names):
        name_score = 0
        for letter in name:
            name_score += ord(letter) - 64
        answer += name_score * (names.index(name) + 1)

    print(answer)


if __name__ == "__main__":
    main()
