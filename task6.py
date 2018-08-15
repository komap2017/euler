import numpy as np


def main():
    sequence = np.arange(101)
    sum_of_squares = np.sum(sequence ** 2)
    print(sum_of_squares)
    square_of_sum = np.sum(sequence) ** 2
    print(square_of_sum)
    print('{} - {} = {}'.format(square_of_sum, sum_of_squares, square_of_sum - sum_of_squares))


if __name__ == '__main__':
    main()
