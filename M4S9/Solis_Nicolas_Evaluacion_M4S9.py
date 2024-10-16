#funcion para cambiar un determinado string, por otro, imprime la cantidad de veces que la reemplaza
def reemplazar_datos_archivo(texto_viejo, texto_nuevo):
    try:
        reemplazos = 0
        with open('informacion.dat', 'r', encoding='utf-8') as info:
            reemplazo = ""
            for linea in info:
                linea = linea.strip()
                conteo = linea.count(texto_viejo)
                reemplazos += conteo
                cambio = linea.replace(texto_viejo, texto_nuevo)
                reemplazo = reemplazo + cambio + "\n"

        with open('informacion.dat', 'w', encoding='utf-8') as info_reemplazo:
            info_reemplazo.write(reemplazo)
        print (f'\nEl texto "{texto_viejo}" se reemplazó {reemplazos} veces por "{texto_nuevo}".')

    except FileNotFoundError:
        print('El archivo informacion.dat no ha sido encontrado.')
    except Exception as error:
        print('Se ha generado un error no previsto', type(error).__name__)
    finally:
        print("Se ha reemplazado satisfactoriamente.\n")

#funcion para leer el archivo
def leer_archivo():
    try:
        with open('informacion.dat', 'r', encoding='utf-8') as info:
            print(info.read())
    except FileNotFoundError:
        print('El archivo informacion.dat no ha sido encontrado.')
    except Exception as error:
        print('Se ha generado un error no previsto', type(error).__name__)

reemplazar_datos_archivo('información', 'procesamiento')
leer_archivo()