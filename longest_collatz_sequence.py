# Arjun Sarao
from tqdm import tqdm


def main():
    def calculate_collatz_sequence_length(n: int) -> int:
        sequence_length = 0
        while True:
            if n == 1:
                break
            elif n % 2 == 0:
                n = n // 2
                sequence_length += 1
            else:
                n = 3 * n + 1
                sequence_length += 1
        return sequence_length

    longest_sequence_length = 2
    longest_sequence_number = 2
    for i in tqdm(range(1, 1000000)):
        sequence_length = calculate_collatz_sequence_length(i)
        if sequence_length > longest_sequence_length:
            longest_sequence_length = sequence_length
            longest_sequence_number = i
    print(longest_sequence_number)


if __name__ == "__main__":
    main()
