def dividers(number):
    return [i for i in range(1, number + 1) if number % i == 0 ]


def main():
    number = 151310
    print(dividers(number))


if __name__ == '__main__':
    main()
