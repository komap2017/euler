import num
import seq
import numpy as np


def main():
    array = np.arange(2000000)
    print(array)
    array = seq.filter_seq(array, num.is_prime)
    print(array)
    print(np.sum(array))


if __name__ == '__main__':
    main()
