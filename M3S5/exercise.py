# Si el número es positivo, imprimimos un mensaje apropiado.

""" num = 0
if (num > 0) :
    print(num, "es un número positivo.")
elif num < 0: #se sale del bloque al primer elif que sea válido
    print(num, 'es un número negativo.')

elif (opcion == 2):
    print('hola')
elif (opcion == 3):
    print('mundo')
elif (opcion == 4):
    print('en python')
else:   #else solo se ejecuta si el resultado para if no se ejecuta.
    print(num, 'es un 0.') """

#ejercicio 4
""" numeros = [6, 5, 3, 8, 4, 2, 5, 4, 11]
suma = 0
for num in numeros:
    suma += num
print ('suma =', suma)
"""
#ejercicio 4 alt con range
""" numeros = [3, -6, 0, 13, 3.4]
suma = 0
for i in range(len(numeros)):
    suma += numeros[i]
print('suma = ', suma) """

#Ejercicio 5 Usando for else
""" digitos = [0, 1, 5]

for i in digitos:
    print(i)
else:
    print('Ya no quedan más dígitos.')
"""

#Ejercicio 6 Conociendo While

""" suma = 0
i = 1

while i <= 10:
    suma += i
    i += 1  #Esta actualiza el contador
#antes estaba imprimiendo la operatoria como tal, no el resultado total de la suma
print(f'La suma es {suma}')  """

#Ejercicio 7 Sentencia Break

""" for batman in "murcielago":
    if batman == 'c':
        break
    print(batman)
print('final')
"""
#Ejercicio 8 Sentencia continue

for val in 'cadena':
    if val == 'a':
        continue
    print(val)
print('final')