n = int(input('Enter the number: '))

step = 0
while n > 1:
    step += 1
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1

    print(n, end=' ')

print('\nTotal step: ', step)