#usualmente no es así, no copiar.
#Código malo
class NuestroError(Exception): #nuevamente, ocupar sufijo Error
    def __init__(self, message):
        super().__init__(message)

class NumeroFormatoExcepcion(Exception):
    def __init__(self, value):
        self.message = f'{value} no es un número' #esta es otra variable, también llamada message, mal
        super().__init__(self.message)

def division_entera(x, y):
    if not isinstance (x, int):
        raise NumeroFormatoExcepcion(x)
    elif type(y) != int:
        raise NumeroFormatoExcepcion(y)
    elif y == 0:
        raise NuestroError('Ha ocurrido una excepción')
    else:
        dividendo = int(x)
        divisor = int(y)
        return dividendo/divisor

try:
    resultado = division_entera(11, 'q')
    print(resultado)
except NuestroError:
    print('Error en división por 0')