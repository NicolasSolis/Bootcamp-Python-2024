#copiado de mi entrega anterior
while True:
    try:
        num_1 = int(input("por favor ingrese su primer número "))
        num_2 = int(input("por favor ingrese su segundo número "))
        num_3 = int(input("por favor ingrese su tercer número "))
    except ValueError:
        print('ERROR: Por favor ingrese sus números nuevamente')
    else:
        break

#creo que no se hacía con sorted, perdón
""" numeros = [num_1, num_2, num_3]
numeros_orden = sorted(numeros)

print(f'Sus números, de menor a mayor son: {numeros_orden}') """

if num_1 <= num_2 and num_2 <= num_3:
    print(f'Sus números, de menor a mayor son: {num_1, num_2, num_3}')
elif num_1 <= num_3 and num_3 <= num_2:
    print(f'Sus números, de menor a mayor son: {num_1, num_3, num_2}')
elif num_2 <= num_1 and num_1 <= num_3:
    print(f'Sus números, de menor a mayor son: {num_2, num_1, num_3}')
elif num_2 <= num_3 and num_3 <= num_1:
    print(f'Sus números, de menor a mayor son: {num_2, num_3, num_1}')
elif num_3 <= num_1 and num_1 <= num_2:
    print(f'Sus números, de menor a mayor son: {num_3, num_1, num_2}')
else:
    print(f'Sus números, de menor a mayor son: {num_3, num_2, num_1}')