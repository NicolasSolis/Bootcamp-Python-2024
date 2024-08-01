#1.- Acceder a datos de una list, es lo mismo con tuplas

""" mi_lista = [1, 2, 3, 4, 5]
print(mi_lista[3]) """

#2.- Accediendo a datos de tupla

""" tup1 = (1, 2, 3, 4, 5, 6, 7)

#resulta en otra tupla, solo que con los datos pedidos
#listas hacen lo mismo, solo que devuelven otra lista
print(f'esta es la tup1: {tup1[1:5]}') """

#3.- Accediendo a elementos de un set

""" set1 = set(['Esto', 'es', 'un', 'Ejercicio'])

for i in set1:
    print(i, end=' ')
print()

#True, porque está
# #Sale desordenado porque set no tiene orden.
print('Ejercicio' in set1) """


#4.- Accediendo a los datos de un diccionario

""" dict = {'Nombre':'Luis',
        'Apellido':'Gonzalez',
        'Edad':21
}
#esta es la forma correcta ocupando f, no necesario
print(f'Nombre: {dict['Nombre']}')
print(f'Edad: {dict['Edad']}') """

#5.- Datos en distintas estructuras de datos

""" mi_lista = [10, 20, 14]
mi_tupla = [1, 2, 4, 6]
mi_set = [1000, 2000, 3000, 4000, 5000]

print(f'Lista: {len(mi_lista)}')
print(f'Tupla: {len(mi_tupla)}')
print(f'Set: {len(mi_set)}') """

#6.- Conociendo la cantidad de datos en un diccionario

""" nro_frutas = {'Manzanas':100, 'Peras':120, 'Naranjas':50}
variedad_frutas = nro_frutas.keys() #cantidad de llaves, ej.:'Manzanas' en un dictionary

print(f'Variedad de frutas: {len(variedad_frutas)}') """