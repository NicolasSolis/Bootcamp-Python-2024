def eliminar_datos_archivo(): #es posible hacerlo con menos código
    try:
        archivo = open('datos.csv', 'w', encoding='utf-8')
        archivo.close()
    except FileNotFoundError:
        print('No se encuentra el archivo datos.csv')
    except Exception as error:
        print('Se ha generado un error no previsto', type(error).__name__)
    finally:
        print("Se ha eliminado todos los datos del archivo exitosamente")

eliminar_datos_archivo()