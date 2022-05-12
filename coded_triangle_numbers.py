# Arjun Sarao

from tqdm import tqdm


def main():
    def generate_triangle_numbers(n: int) -> list:
        """
        Returns a list of triangle numbers up to n.
        params: n - an integer to find triangle numbers up to
        returns: a list of triangle numbers up to n
        """
        triangle_numbers = []
        for i in range(1, n + 1):
            triangle_numbers.append(i * (i + 1) // 2)
        return triangle_numbers

    def word_value_calculator(word: str) -> int:
        """
        Returns the value of a word.
        params: word - a string to find the value of
        returns: the value of a word
        """
        value = 0
        for letter in word:
            value += ord(letter) - 64
        return value

    triangle_words = []
    with open("associated_files/p042_words.txt") as f:
        words = f.read().replace('"', "").split(",")
    triangle_numbers = generate_triangle_numbers(200)
    for word in tqdm(words):
        if word_value_calculator(word) in triangle_numbers:
            triangle_words.append(word)
            print(f"{word} is a triangle word.")
    print(f"There are {len(triangle_words)} triangle words.")


if __name__ == "__main__":
    main()
