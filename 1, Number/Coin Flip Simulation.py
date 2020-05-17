import random

n = int(input('number of coin tosses: '))

tails = 0
heads = 0

for i in range(0, n):
    status = random.randint(0,1)
    if status == 0:
        tails += 1
        print(status, end=' ')
    else:
        heads += 1
        print(status, end=' ')

print('\nTotal:\nTails = ', tails,'\nHeads = ', heads)