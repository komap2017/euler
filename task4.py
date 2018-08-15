import palin
import numpy as np

import seq


def main():
    numbers = np.arange(100, 1000)
    sequence = np.tile(numbers, (999 - 100 + 1, 1))
    vertical = seq.vertical(numbers)
    sequence = sequence * vertical
    print(sequence)
    sequence = seq.filter_seq(sequence, palin.is_palindrome)
    print(sequence)
    print(np.max(sequence))


if __name__ == '__main__':
    main()
