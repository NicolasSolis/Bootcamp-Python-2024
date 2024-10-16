def agregar_datos_archivo():
    try:
        archivo = open('datos.csv', 'a', encoding= 'utf-8') # 'a' no devuelve excepción al crear archivo ni insertar contenido
        archivo.write('\nLínea 6 agregada')
        archivo.close()
    except FileNotFoundError:
        print('No se encuentra el archivo datos.csv')
    except Exception as error:
        print('Se ha generado un error no previsto', type(error).__name__)

agregar_datos_archivo()