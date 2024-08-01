def suma(a, b):
    resultado_suma = a + b
    return resultado_suma

def resta(a, b):
    resultado_resta = a - b
    return resultado_resta

def multi(a, b):
    resultado_multi = a * b
    return resultado_multi

def div(a, b):
    resultado_div = a / b
    return resultado_div

#este while es uno de los loop que más he usado xd
while True:
    try:
        a = int(input("por favor ingrese su primer número "))
        b = int(input("por favor ingrese su segundo número "))
    except ValueError:
        print('ERROR: Por favor ingrese sus números nuevamente')
    else:
        break
""" no entendí muy bien lo de 'función que acepte dos números 
    como parámetros y regrese el resultado en forma de tupla de su suma, 
    resta, multiplicación y división.' esto?:
"""
def operaciones(a, b):
    return (suma(a,b), resta(a,b), multi(a,b), div(a,b))
# luego se pide un diccionario
def operaciones_dict(a, b):
    resultado = {
        "suma": suma(a, b),
        "resta": resta(a, b),
        "multiplicacion": multi(a, b),
        "division": div(a, b)
    }
    return resultado
#print individuales ocupando dict y de operaciones
resultado = operaciones_dict(a, b)
print(f"Suma: {resultado['suma']}")
print(f"Resta: {resultado['resta']}")
print(f"Multiplicación: {resultado['multiplicacion']}")
print(f"División: {resultado['division']}")

print(f'Operaciones: {operaciones(a, b)}') #me salía el error porque llamando a la función
print(f'Diccionario operaciones: {resultado}')