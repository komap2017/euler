import numpy as np
from itertools import product
import seq as s


def is_pif(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


def main():
    seq = np.arange(100)
    print(seq)
    seq = np.tile(seq, (3, 1))
    print(seq)
    seq = np.array(tuple(product(*seq)))
    print(seq)
    res = []
    for el in seq:
        if is_pif(*el):
            res.append(el)
    print(res)
    print(res == [95, 0, 96])


if __name__ == '__main__':
    main()
