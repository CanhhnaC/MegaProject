
def Fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib


if __name__ == "__main__":
    n = int(input('Enter the number: '))
    for i in Fibonacci(n):
        if i <= n:
            print(i, end=' ')
