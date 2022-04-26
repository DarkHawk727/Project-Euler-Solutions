# Arjun Sarao

from tqdm import tqdm


def main():
    factorials_dict = {
        "0": 1,
        "1": 1,
        "2": 2,
        "3": 6,
        "4": 24,
        "5": 120,
        "6": 720,
        "7": 5040,
        "8": 40320,
        "9": 362880,
    }
    factorials_list = []
    for i in tqdm(range(10, 1000000)):
        if i == sum([factorials_dict[j] for j in str(i)]):
            print(f"{i} is a digit factorial!")
            factorials_list.append(i)

    print(f"The sum of these numbers is {sum(factorials_list)}.")


if __name__ == "__main__":
    main()
