# Atributos de un archivo abierto en python
archivo = open('remeras.txt')
contenido = archivo.read(15)
nombre = archivo.name
modo = archivo.mode
encoding = archivo.encoding
print(archivo.seek())

archivo.close()
if archivo.closed:
    print('El archivo se ha cerrado correctamente')
else:
    print('El archivo permanece abierto')
    
print(nombre)
print(modo)
print(encoding)
print(contenido)