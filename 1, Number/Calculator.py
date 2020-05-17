a = float(input('Input a: '))
b = float(input('Input b: '))
print('Cac phep tinh:')
print('1, Addition')
print('2, Subtraction')
print('3, Multiplication')
print('4, Division')
choose = int(input('Choose: '))
if choose == 1:
    print(a, ' + ', b, ' = ', a+b)
elif choose == 2:
    print(a, ' - ', b, ' = ', a-b)
elif choose == 3:
    print(a, ' * ', b, ' = ', a*b)
elif choose == 4:
    print(a, ' : ', b, ' = ', a/b)
else:
    print('Error, you can choose a true caculator')
