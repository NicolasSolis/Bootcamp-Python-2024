#M4S6 Ejercicio 1
""" contador = 0
calculo_suma = 0
print("Sumatoria de 4 numero enteros")
#si el numero es válido, pasa por las líneas 7, 9, 17, 18, 19, 20 y vuelve al 7.

while contador < 4: #bucle continúa hasta que contador alcanza 4
    try: #para atajar valores
        valor = int(input(f'Ingrese sus números enteros ({contador+1} de 4): '))
        calculo_suma += valor
        contador +=1
#ocupar CTRL + C, que debería ser una salida forzosa, no funciona.
#except por sí mismo es fuerte
    except: #exception de valores no numéricos enteros
        print("Valor Errado: ingrese un numero entero correcto")
    #else opcional, cuando está presente va después de el/los except
    else:
        print("No se capturaron excepciones, todo bien")
    finally:
        print("Finally se ejecuta al final de la ejecución con o sin excepciones")

print("El resultado de la suma es: {}".format(calculo_suma)) """

#M4S6 Ejercicio 2
#el ejercicio proponía otra cosa, pero tenía un solo ' / ' en vez de ' // '
""" def division_entera(x: int | float | str, y: int | float | str) -> int: #todo esto en rojo es notación, para otros dev
    try:
        dividendo = int(x) 
        divisor = int(y)
        return dividendo // divisor #esto ni siquiera debería estar acá, esto es una función y debería hacer una sola cosa

    except ZeroDivisionError:
        print('El divisor no puede ser cero')
    except ValueError:
        print('Valores ingresados no válidos')
    except Exception as error:
        print('Se ha generado un error no previsto', type(error).__name__)

resultado = division_entera(5, 6) """

#M4S6 Ejercicio 3. No muy bien diseñado
""" def division_entera(x, y):
    if y == 0:
        raise ZeroDivisionError('No se puede dividir por cero')
    dividendo = int(x)
    divisor = int(y)
    return dividendo/divisor

resultado = division_entera(1, 0)
print(resultado) """