class NuestraExcepcion(Exception): #Prefiérase el sufijo Error
    def __init__(self, message):
        super().__init__(message)

message = "Este es el mensaje de Nuestra Excepción."
#la forma correcta de escribir un programa es primero poner las clases primero, después funciones, después lógica
def division_entera(x,y):
    if y == 0:
        raise NuestraExcepcion(message)
    else:
        dividendo = int(x)
        divisor = int(y)
        return dividendo/divisor
#idealmente ocupar el try...except