import num


def main():
    def solve(pow_to):
        number = 2 ** pow_to
        print('2 ** 15 = {0}'.format(number))
        digits = num.digits(number, gen=False)
        s = tuple(map(str, digits))
        print("{} = {}".format(' + '.join(s), sum(digits)))
    solve(15)
    solve(1000)


if __name__ == '__main__':
    main()
