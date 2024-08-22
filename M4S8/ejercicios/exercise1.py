from io import open #esto no es necesario en Python, va incorporado
#función que crea un archivo csv
#'x' y 'w' crean archivos, w los trunca (sobreescribe, elimina). ocupar 'x'
def crear_archivo():
#con manejo de excepciones
    try:    
        archivo = open('datos.csv', 'x') #'w' trunca (elimina) datos, se recomienda 'x'
        archivo.close()
    except FileExistsError: #como sabemos cuál es el error, podemos customizar el Error
        print("El archivo datos.cvs existe o ha sido creado previamente")
    except Exception as error:
        print('Se ha generado un error no previsto', type(error).__name__) 

crear_archivo()