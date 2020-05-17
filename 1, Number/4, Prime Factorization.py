from math import sqrt


def is_Prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    n = int(input('N = '))

    for i in range(2, n + 1):
        if is_Prime(i):
            print(i, end=' ')
