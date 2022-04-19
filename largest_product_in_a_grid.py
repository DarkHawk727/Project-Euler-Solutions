# Arjun Sarao
import numpy as np


def main():
    grid = np.loadtxt("grid.txt", dtype=int, delimiter=" ")

    def find_largest_row_product(grid: np.array, size: int) -> int:
        for row in grid:
            # CFind the largest product of 4 adjacent numbers in the same row
            largest_product_row = 1
            for i in range(len(row) - size + 1):
                product = 1
                for j in range(i, i + size):
                    product *= row[j]
                largest_product_row = max(largest_product_row, product)
            return largest_product_row

    def find_largest_column_product(grid: np.array, size: int) -> int:
        for i in range(len(grid)):
            # Find the largest product of 4 adjacent numbers in the same column
            largest_product_column = 1
            for j in range(len(grid[i]) - size + 1):
                product = 1
                for k in range(j, j + size):
                    product *= grid[i][k]
                largest_product_column = max(largest_product_column, product)
            return largest_product_column

    def find_largest_diagonal_product(grid: np.array, size: int) -> int:
        # Find the largest product of 4 adjacent numbers in the same diagonal
        largest_product_diagonal = 1
        for i in range(len(grid) - size + 1):
            for j in range(len(grid[i]) - size + 1):
                product = 1
                for k in range(i, i + size):
                    product *= grid[k][j + k - i]
                largest_product_diagonal = max(largest_product_diagonal, product)
        return largest_product_diagonal

    def find_largest_anti_diagonal_product(grid: np.array, size: int) -> int:
        # Find the largest product of 4 adjacent numbers in the same anti-diagonal
        largest_product_anti_diagonal = 1
        for i in range(len(grid) - size + 1):
            for j in range(len(grid[i]) - size + 1):
                product = 1
                for k in range(i, i + size):
                    product *= grid[k][j + size - 1 - (k - i)]
                largest_product_anti_diagonal = max(
                    largest_product_anti_diagonal, product
                )
        return largest_product_anti_diagonal

    largest_product_row = find_largest_row_product(grid, 4)
    largest_product_column = find_largest_column_product(grid, 4)
    largest_product_diagonal = find_largest_diagonal_product(grid, 4)
    largest_product_anti_diagonal = find_largest_anti_diagonal_product(grid, 4)
    print(
        max(
            largest_product_row,
            largest_product_column,
            largest_product_diagonal,
            largest_product_anti_diagonal,
        )
    )


if __name__ == "__main__":
    main()
