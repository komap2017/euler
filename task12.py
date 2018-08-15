import numpy as np
import num
import seq


def triangular(n):
    return np.sum(range(1, n + 1))


def main():
    arr = []
    start = 12
    a = seq.Array([1, 2, 3])
    print(a)
    print(a[-1])
    while len(arr) == 0:
        arr = seq.Array(np.arange(start * 1000, (start + 1) * 1000))
        print(arr)
        arr.map(triangular)
        print(arr)
        arr.filter(lambda x: len(tuple(num.dividers(x))) > 500)
        print(arr)
        start += 1
    print(arr[0])


if __name__ == '__main__':
    main()
