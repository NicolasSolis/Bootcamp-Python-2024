def pedir_edad():
    while True: #bucle copiado de todas las veces anteriores
        try:
            edad = int(input('Por favor ingrese cúantos años tiene: '))
        except ValueError:
            print('ERROR: Por favor ingrese edad válida.')
        else:
            if edad >= 18 and edad < 65:
                print(f'Al tener {edad} años, en Chile usted es un adulto.')
            elif edad >= 65:
                print(f'Al tener {edad} años, en Chile usted es un adulto mayor.')
            else:
                print(f'Al tener {edad} años, eres considerado un niño.')
            break

pedir_edad()