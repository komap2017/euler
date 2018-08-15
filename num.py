import math


def dividers(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def divides_on(first, second):
    return first % second == 0


def is_even(number):
    return divides_on(number, 2)


def is_prime(n):
    """Returns True if n is prime."""
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


def fib(n):
    return pow(2 << n, n + 1, (4 << 2 * n) - (2 << n) - 1) % (2 << n)


def digits(number, gen=True):
    res = map(int, str(number))
    if gen:
        return res
    return tuple(res)


def factorial(number):
    if number < 0:
        raise ValueError('number {} is less than zero'.format(number))
    if not isinstance(number, int):
        raise TypeError('number has type {} not int'.format(type(number)))
    res = 1
    for i in range(2, number + 1):
        res *= i
    return res


def main():
    number = 151310
    print(dividers(number))


if __name__ == '__main__':
    main()
