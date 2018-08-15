from num import is_prime
import numpy as np
from seq import filter_seq


def main():
    seq = np.arange(200000)
    print(seq)
    seq = filter_seq(seq, is_prime)
    print(seq)
    print(seq[10000])


if __name__ == '__main__':
    main()
