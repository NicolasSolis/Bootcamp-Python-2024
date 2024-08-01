#factorial de un nº, con input y bucle
while True:
    try:
        num = int(input('Ingrese un número positivo '))
        if num < 0:
            print('Por favor ingrese un número mayor a 0')
        else:
            break
#estaba buscando la forma de obligar a que se ponga un número
    except ValueError: 
        print('Ingrese un número positivo ')

factorial = 1

if num == 0:
    print('El factorial del número 0 es 1')
#factorial via range, inicia en 1, termina justo antes de num, num+1 para incluirlo
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f'El factorial del número {num} es {factorial}')