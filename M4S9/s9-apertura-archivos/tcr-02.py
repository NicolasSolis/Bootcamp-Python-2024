# LECTURA CON read()
archivo = open("lista_compras.txt")
print(archivo.read())
print(archivo.tell())


print(archivo.tell()) #pos final - ya leído el archivo

archivo.seek
# LECTURA CON read(size)
archivo = open("lista_compras.txt")
print(archivo.read(5))