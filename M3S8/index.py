#Ejemplo 1
    # Constructor set()
""" a = set('abracadabra')
b = set('alacazam') """

    # Algebra de conjuntos en Python
""" print(a) # Letras únicas en a
print(b) # Letras únicas en b
print(a - b) # Letras únicas en a pero no en b
print(b - a) # Letras únicas en b pero no en a
print(a | b) # Letras en a, en b o en ambas
print(a & b) # Letras que a y b tienen en común
print(a ^ b) # Letras en a y b pero no en ambas """

#Ejemplo 2
""" st = {9,-1,3}
print(9 in st) # True
print(3 not in st) # False
st.add(6) # añade un 6 a st
st.update([3,4,5]) # añade solo el 4 y el 5
print(st)
st.discard(7) # remueve el 7 si está
st.remove(7) # si no está el 7: Error """

#Ejemplo 3
""" mi_set = set("palabra")
print("mi_set =",mi_set)

mi_set.pop()
print("mi_set =",mi_set)

mi_set.clear()
print("mi_set =",mi_set) """

#Ejemplo 4 tipo Dict.

""" song = {
    "name":"Viva la vida",
    "artist":"Coldplay",
    "year":2008,
    "duration":242 # in seconds
}
    # <class 'dict'> tiene formato de
    # texto definido en print
print(song)
    # Se accede al valor por su clave
print(song["name"])
    # Se puede eliminar un valor con del()
del song["year"]
print(song)

    # Podemos añadir un nuevo par clave:valor
song["album"] = "Viva La Vida or Death and All His Friends"
print(song)
    # Es posible verificar si una clave se encuentra (o no)
    # en el diccionario
print("name" in song)
print("duration" not in song)
print(song.get("name")) """

#Otros ejemplos

""" vals = range(5) # range (0, 5, 1) - 0, 1, 2, 3, 4
print(list(vals)) """

    #range(start, end, steps
        #start: valor inicial de la secuencia
        #end: valor final (exluyente = '-1') de la secuencia
""" steps: número de pasos con los que se avanza 
        a partir de inicio para crear nuevos valores """

""" vals = range(2, 3, 3) # 2
print(list(vals)) """

#Más ejemplos

""" print(tuple(range(-8, -20, -1)))
print(tuple(range(-8, -4, 1)))
print(tuple(range(10, -1, -1)))

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_2 = list(range(11))
print(lista)
print(lista_2) """

#Lectura
""" lista = [10, 50, 75, 83] """

#acá recorre rango, posición 0, 1, 2 y 3
""" for x in range(len(lista)):
    print(lista[x]) """

""" for x in range(1,len(lista)): # x = 1, 2, 3 <--- recorro el range()
    lista[x] += 2
    print(lista[x]) #empieza desde list [1] """

#esta recorre valores, toma el 10, 50, 75, 83
#formas son válidas, varían en utilidad
""" for x in lista: 
    print(x) """

#ej. bucle while
#x no está definida en el ejemplo de lectura

""" x = 0
lista = [10, 50, 75, 83] 

while x < len(lista): 
    print(lista[x]) 
    x = x+1 """

#ej. enumerate

""" lista = [10, 50, 75, 83] 

for x, val in enumerate(lista): 
    print (val) """

#ej. set
#conjuntos siempre están desordenados, no sabemos cuál va a tomar.
#Son iterables, pero evitan los duplicados y desordenan los datos.
""" mi_set = {'london', 'new york', 'seattle', 'sydney'} 

for item in iter(mi_set): 
    print(item) """

#ej. dictionary

""" paises_y_capitales = {
    'Japon': 'Tokio',
    'Inglaterra': 'Londres',
    'Francia': 'Paris',
    'Alemania': 'Berlin'
}

keys = paises_y_capitales.keys() """

""" for clave in keys :
    print(f"{clave} - {paises_y_capitales[clave]}") """

""" for pais in paises_y_capitales: 
    print(f"{pais} - {paises_y_capitales[pais]}") """

""" for capital in paises_y_capitales.values():
    print(capital) """


#otros

    #Ejercicio 12:

""" mi_lista = [1, 2, 3, 4, 5]
print(mi_lista[3]) """

    #Ejercicio 13:
""" tup1 = (1, 2, 3, 4, 5, 6, 7)
#Si se omite inicio, defecto 0. Si se omite nº de pasos, por defecto es 1.
print ("tup1[1:5]:",tup1[1:5])  """