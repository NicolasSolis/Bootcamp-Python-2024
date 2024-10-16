# Abrimos el fichero
fichero = open("datos_guardados.txt", 'w', encoding= 'utf-8') # 'w' trunca y sobreescribe el texto / no tenía encoding

# Tenemos unos datos que queremos guardar
lista = ["Manzana", "Pera", "Plátano"]

# Guardamos la lista en el fichero
for linea in lista:
    fichero.write(linea + "\n")
    
# Cerramos el fichero
fichero.close()