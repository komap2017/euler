import num


def is_palindrome(number):
    digits = tuple(num.digits(number))
    return tuple(reversed(digits)) == digits


def main():
    print(is_palindrome(9009))


if __name__ == '__main__':
    main()
