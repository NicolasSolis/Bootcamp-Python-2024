"""
Ok, disculpen por enviar el mismo archivo en rebound y drilling, es que justamente me di cuenta
que la evaluación me pide exactamente lo mismo que estaba haciendo acá, puedo enviarlo así?
"""
def crear_archivo():
    '''Crea un archivo llamado informacion.dat, en caso de existir, lo lee'''
    try:
        archivo = open('informacion.dat', 'x', encoding='utf-8')
        archivo.write(
                    'Datos de información en la línea 1.\n'
                    'Datos de información en la línea 2.\n'
                    'Datos de información en la línea 3.\n'
                    'Datos de información en la línea 4.\n'
                    'Datos de información en la línea 5.\n'
)        
        archivo.close()
    except FileExistsError:
        print('El archivo informacion.dat ya existe o ha sido creado previamente y contiene lo siguiente:\n')
        
#evaluacion M4S8
def leer_archivo():
    '''Función ocupada para leer informacion.dat'''
    try:
        archivo = open("informacion.dat", encoding='utf-8') #no olvidar encoding de nuevo xd
    except FileNotFoundError:
        print("El archivo informacion.dat no se encuentra")
    else:
        contenido = archivo.read()
        archivo.close()
        print(contenido)

crear_archivo()
leer_archivo()