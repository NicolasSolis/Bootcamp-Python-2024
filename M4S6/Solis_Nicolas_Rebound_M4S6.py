suma = 3000
contador = 0

def division(x, y):
    return x / y

try:
    resultado = division(suma, contador)
except ZeroDivisionError:
    print('División por cero.')