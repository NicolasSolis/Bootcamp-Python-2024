#Obtener número y solo número
while True:
    try:
        num = int(input("Ingrese un número "))
    except ValueError:
        print('Por favor ingrese un número')
    else:
        break

#Evaluar nº
if num > 0:
    if num % 2 == 0:
        print('Su número es positivo y par')
    else:
        print('Su número es positivo e impar')
elif num < 0:
    if num % 2 == 0:
        print('Su número es negativo y par')
    else:
        print('Su número es negativo e impar')
else:
    print('Su número es 0')