# Arjun Sarao


def main():
    largest_product = 0
    with open("associated_files/p008_series.txt", "r") as f:
        lines = f.read().splitlines()

    NUM = str(lines[0])
    for i in range(len(NUM) - 13):
        product = 1
        for j in range(13):
            product *= int(NUM[i + j])
        if product > largest_product:
            largest_product = product
    print(largest_product)


if __name__ == "__main__":
    main()
