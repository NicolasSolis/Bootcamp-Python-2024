lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in lista:
    if (num % 2 == 0) and num != 0:
        print(f'{num} es par')
    elif(num % 2 != 0):
        print(f'{num} es impar')
    else:
        print('0 es cero')