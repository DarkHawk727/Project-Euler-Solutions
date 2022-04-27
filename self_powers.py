# Arjun Sarao


def main():
    def calculate_sum_of_self_powes(n: int) -> int:
        answer = 0
        for i in range(1, n + 1):
            answer += i**i
        return answer

    print(f"Sum of self powers: {calculate_sum_of_self_powes(1000)}")
    print(f"The last 10 digits: {calculate_sum_of_self_powes(1000) % 10000000000}")


if __name__ == "__main__":
    main()
