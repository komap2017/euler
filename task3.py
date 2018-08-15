import num
import numpy as np

import seq


def main():
    number = 600851475143
    sequence = np.array(tuple(num.dividers(number)))
    mask = seq.map_seq(sequence, num.is_prime)
    sequence = sequence[mask]
    print(sequence)
    print(np.max(sequence))


if __name__ == '__main__':
    main()
