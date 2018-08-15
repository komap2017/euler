from num import fib, is_even


def main():
    seq = range(1, 51)
    seq = tuple(map(fib, seq))
    seq = [el for el in seq if el < 4000000 if is_even(el)]
    print(seq)
    print(sum(seq))


if __name__ == '__main__':
    main()
