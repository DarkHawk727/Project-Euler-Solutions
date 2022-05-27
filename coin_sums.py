# Arjun Sarao


def main():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    arr = [1] + [0] * 200
    for i in range(8):
        for j in range(coins[i], 201):
            arr[j] += arr[j - coins[i]]

    print(f"There are {arr[200]} ways to make 200p with the given coins.")


if __name__ == "__main__":
    main()
