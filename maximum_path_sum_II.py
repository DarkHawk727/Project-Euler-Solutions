# Arjun Sarao

from tqdm import tqdm


def main():
    with open("associated_files/triangle.txt", "r") as f:
        pyramid = [[int(x) for x in line.split()] for line in f.read().split("\n")]

    for i in tqdm(range(len(pyramid) - 2, -1, -1)):
        for j in range(len(pyramid[i])):
            pyramid[i][j] += max(pyramid[i + 1][j], pyramid[i + 1][j + 1])

    print(pyramid[0][0])


if __name__ == "__main__":
    main()
