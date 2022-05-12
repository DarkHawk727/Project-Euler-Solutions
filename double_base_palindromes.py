# Arjun Sarao

from tqdm import tqdm


def main():
    def is_palindrome(n: int) -> bool:
        """
        Checks if n is a palindrome.
        params: n - an integer to check if it is a palindrome
        returns: True if n is a palindrome, False otherwise
        """
        return str(n) == str(n)[::-1]

    answer = 0
    for i in tqdm(range(1, 1000001)):
        if is_palindrome(i) and is_palindrome(bin(i)[2:]):
            answer += i
            # print(f"{i} and {bin(i)[2:]} are both palindromes.")
    print(f"The sum of all the double-base palindromes is: {answer}.")


if __name__ == "__main__":
    main()
