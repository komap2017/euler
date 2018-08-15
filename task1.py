import numpy as np


def main():
    seq = np.arange(1000)
    print(seq)
    seq = seq[np.logical_or(seq % 5 == 0, seq % 3 == 0)]
    print(seq)
    print(np.sum(seq))


if __name__ == '__main__':
    main()
