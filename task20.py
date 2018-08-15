import num


def main():
    number = 100
    f = num.factorial(number)
    print(f)
    print(sum(num.digits(f)))

if __name__ == '__main__':
    main()
