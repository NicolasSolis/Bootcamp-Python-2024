fichero = open('ejemplo.txt', encoding="utf-8")

# Linea por linea --> str
print(fichero.readline())
print(fichero.readline())

# Todas las lineas --> list(str)
print(fichero.readlines())

# Iteración para todas las lineas con readlines()
for line in fichero.readlines():
    print(line, end="") # --> a stdout