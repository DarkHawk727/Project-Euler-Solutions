# Arjun Sarao

from tqdm import tqdm


def main():
    perimeters = {}
    p = 1000
    for a in tqdm(range(1, p)):
        for b in range(1, p):
            for c in range(1, p):
                if a + b + c <= 1000:
                    if a ** 2 + b ** 2 == c ** 2:
                        if a + b + c in perimeters:
                            perimeters[a + b + c].append((a, b, c))
                        else:
                            perimeters[a + b + c] = [(a, b, c)]

    max_perimeter = max(perimeters.keys())
    num_solutions = len(perimeters[max_perimeter])
    print(
        f"The perimeter of the right triangle with the largest number of solutions is {max_perimeter} with {num_solutions} solutions."
    )


if __name__ == "__main__":
    main()
