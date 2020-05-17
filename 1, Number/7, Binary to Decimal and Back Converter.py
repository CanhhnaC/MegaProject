def bin_to_dec(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def dec_to_bin(n):
    if (n > 1):
        dec_to_bin(n // 2)

    print(n % 2, end='')


title = int(input('Chose convert:\n1, Convert bin to dec\n2, Convert dec to bin\nWhat you choose: '))


if title == 1:
    n = int(input('Enter bin: '))
    print(bin_to_dec(n))
elif title == 2:
    n = int(input('Enter dec: '))
    dec_to_bin(n)
    print()
