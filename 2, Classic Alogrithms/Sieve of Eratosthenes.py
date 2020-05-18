def sieveOfEratosthenes(n):
    arr = []
    for i in range(2, n + 1):
        if i not in arr:
            print(i)
            for j in range(i * i, n + 1, i):
                arr.append(j)


if __name__ == "__main__":
    n = int(input('n= '))
    sieveOfEratosthenes(n)
