""" print(bool([1, 42, 'hola', -3.15]))

print((3 < 5) and (2 != 2) and (3 < 1))

print(3 > 5 or 2 == 2 and not 3 <= 4 and True and False and not 1 == 1) """

#Diapo 20
""" x = 42
y = 'Hola'

print(type(x) == int) #True
print(type(y) == str) #True
print(type(x) == str) #False
print(type(y) == int) #False """

#Diapo 22

""" j = 10
if j > 0:
    print('x es un número positivo')
elif j < 0:
    print('x es un número negativo')
else:
    print('x es igual a 0') """

#misma diapo, otro ej.

""" if x > 0:
    print('x es un nº positivo')
if x < 0:
    print('x es un nº negativo')
else:
    print('x es igual a 0') """

#Diapo 25

""" print(list(range(1,6,2))) """

#break
""" matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for i in matriz:
    print('Matriz')
    for j in i:
        if(j == 5):
            print('acá está el 5')
            break #este break me saca de ESTE for, del segundo
    print('ya recorrí la sublista')

print('hasta acá no llega el for') """

#continue

""" numbers = [-2, 4, -1, 6, 0, 3]

for num in numbers:
    if num <= 0:
        continue
    print(num) """

#Hay que cambiarle el end:'' para que salga para el lado, por defecto es un salto de linea
for char in 'Hola mundo':  
    print(char, end='')