#funcion para crear un archivo informacion.dat con determinados datos
def crear_archivo():
    try:
        with open('informacion.dat', 'x', encoding='utf-8') as info:
            print(' ')
            info.write('Datos de información en la línea 1.\n')
            info.write('Datos de información en la línea 2.\n')
            info.write('Datos de información en la línea 3.\n')
            info.write('Datos de información en la línea 4.\n')
            info.write('Datos de información en la línea 5.\n')
    except FileExistsError:
        print('El archivo informacion.dat ya existe o ha sido creado previamente.')
    except Exception as error:
        print('Se ha generado un error no previsto', type(error).__name__)

#funcion para agregar datos al archivo
def agregar_datos_archivo():
    try:
        with open('informacion.dat', 'a', encoding='utf-8') as info:
            info.write('\nHola Mundo en archivo.dat\n')
            info.write('Esta es una nueva línea en el archivo.\n')
            info.write('Agregando una segunda línea al archivo.\n')
            info.write('Finalizando las líneas agregadas.')
    except FileNotFoundError:
        print('El archivo informacion.dat no ha sido encontrado.')
    except Exception as error:
        print('Se ha generado un error no previsto', type(error).__name__)

#funcion para leer el archivo
def leer_archivo():
    try:
        with open('informacion.dat', 'r', encoding='utf-8') as info:
            print(info.read())
    except FileNotFoundError:
        print('El archivo informacion.dat no ha sido encontrado.')
    except Exception as error:
        print('Se ha generado un error no previsto', type(error).__name__)

#ojo: no tiene método de comprobar si las líneas ya existen antes de añadirlas nuevamente
crear_archivo()
agregar_datos_archivo()
leer_archivo()