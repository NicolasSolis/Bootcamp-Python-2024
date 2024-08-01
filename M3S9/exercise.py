#Lectura
#Ejercicio 1: Invocando una función
def sumar(a:int, b:int) -> int: #se puede indicar el tipo de dato de los parámetros, solo estética
    '''
    Función para sumar dos números enteros

    Parámetros:
    a (int): Primer número de la suma.
    b (int): Segundo número de la suma.

    Devuelve:

    ''' #esto es para documentar

    resultado = a + b 
    return resultado

resultado = sumar(5,10) 
print(resultado)

