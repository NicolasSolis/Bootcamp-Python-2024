class RangoSalarioError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)

message = "ERROR: Salario no está dentro del rango (1000 a 2000)"

def pedir_salario_valido():
    while True: #bucle copiado de todas las veces anteriores, nuevamente
        try:
            salario = int(input('Ingrese su salario (entre 1000 y 2000): ')) 
            if salario < 1000 or salario > 2000:
                raise RangoSalarioError(message)
            else:
                return salario
        except ValueError:
            print('ERROR: Ingrese su salario en valor numérico nuevamente.')
#forzando el raise
"""         except RangoSalarioError as e:
            print(e) """

salario = pedir_salario_valido()
print(f'Usted debería tener {salario} en su cuenta')