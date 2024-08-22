#función para leer en modo texto (strings) datos.csv
#encoding es importante para escribir en español y otros idiomas en general.
#si ocurre una excepción, el archivo se cierra de todas maneras
def lectura_archivo():
    try:
        archivo = open('datos.csv', 'r', encoding = 'utf-8') #r está por defecto, no es necesario. mode = "r" == "rt"
    except FileNotFoundError:
        print("Archivo no encontrado")
    except Exception as error:
        print('Se ha generado un error no previsto', type(error).__name__) 
    else:   #cuando manejamos excepciones, idealmente todo el resto al else, excepto el open obviamente
        contenido = archivo.read()
        archivo.close()
        print(contenido)

lectura_archivo()