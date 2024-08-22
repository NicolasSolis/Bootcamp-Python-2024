class Persona:
    def __init__(self, nombre: str, apellidos: str, cedula: str) -> None:
        self.nombre = nombre
        self.apellidos = apellidos
        self.cedula = cedula

    def get_tipo(self):
        print("Soy del tipo Persona")

    def imprimir_datos(self):
        print (f'Nombre: {self.nombre} \nApellidos: {self.apellidos}\nCédula: {self.cedula}')

#Método recomendado
    def __str__(self):
        #está bien que salga con error, devuelve el interior del paréntesis en print
        return f'Nombre: {self.nombre} \nApellidos: {self.apellidos}\nCédula: {self.cedula}'

class Supervisor(Persona):
    def __init__(self, nombre: str, apellidos: str, cedula: str, zona: str):
        #la superclase de la clase Supervisor es Persona
        super().__init__(nombre, apellidos, cedula)
        self.zona = zona
        
    def get_tipo(self):
        print("Soy del tipo Supervisor")

    def imprimir_supervisor(self):
        super().imprimir_datos()
        print('Zona:',self.zona)

    def __str__(self):
        return super().__str__() + f'\nZona: {self.zona}'

class Cliente(Persona):
    def __init__(self, nombre, apellidos, cedula, descuento ):
        super().__init__(nombre, apellidos, cedula)
        self.descuento = descuento

    def get_tipo(self):
        print("Soy del tipo Cliente")

    def imprimir_cliente(self):
        super().imprimir_datos()
        print('Descuento: ', self.descuento)

    def __str__(self):
        return super().__str__() + f'\nDescuento: {self.descuento}'

class Capacidades:
    def __init__(self, ncertificados, raiting):
        self.ncertificados = ncertificados
        self.raiting = raiting

    def imprimir_capacidades(self):
        print(f'Nro Certificados: {self.ncertificados} \nRaiting: {self.raiting}')

    def __str__(self):
        return f'Numero de Certificados: {self.ncertificados}\nRaiting: {self.raiting}'
    
class SupervisorZona(Supervisor, Capacidades):
    def __init__(self, nombre, apellidos, cedula, zona,
    ncertificados, raiting, promedio):
        Supervisor.__init__(self, nombre, apellidos, cedula, zona)
        Capacidades.__init__(self, ncertificados, raiting)
        self.promedio = promedio

    def imprimir_supervisor_zona(self):
        Supervisor.imprimir_supervisor(self)
        Capacidades.imprimir_capacidades(self)
        print('Promedio:', self.promedio)