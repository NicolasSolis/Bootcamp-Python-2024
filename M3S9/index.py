# Archivo.py
""" mi_variable = 5

def mi_funcion():
    mi_variable = 10

print(mi_variable) # ¿Qué valor imprime?
mi_funcion()
print(mi_variable) # ¿Qué valor imprime? """

#ej. 2

""" def suma(a, b):
    return a + b

d = suma(4,5)
print("4 + 5 =",d) """

#ej argumento *args

""" def suma(*args):
    sum_ = 0
    for i in args:
        sum_ += i
    return sum_

print(suma(1,2,3,4,5,6,7)) """

#Más ejemplos parámetros

""" def procesar_datos(nombre, edad, *args, ciudad="Nueva York", pais="Estados Unidos", **kwargs):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")
    print(f"País: {pais}")
    if args:
        print("Datos adicionales:")
        for dato in args:
            print(f"- {dato}")
    if kwargs:
        print("Información adicional:")
        for clave, valor in kwargs.items():
            print(f"{clave}: {valor}")
    # Llamando a la función
procesar_datos("Juan", 35, "Casado", "Programador", "Deportista", ciudad="Los Ángeles", telefono="555-1234", hobbies=["Leer", "Viajar"]) """

#Ej, ppt

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = int(input('Ingresa un número: '))
if (es_primo(numero)): print(f'El número {numero} es primo')
else: print(f'El número {numero} no es primo')