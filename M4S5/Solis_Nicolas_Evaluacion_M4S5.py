class Persona():
    def __init__(self, nombre: str, apellido: str, anno: int) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.anno = anno

class Departamento():
    def __init__(self, nombre_dpto: str, nombre_corto_dpto: str) -> None:
        self.nombre_dpto = nombre_dpto
        self.nombre_corto_dpto = nombre_corto_dpto

class Trabajador(Persona, Departamento): #si tuviese algo como get_nombre() en el orden T -> D -> P se ocuparía el de la clase departamento
    def __init__(self, nombre, apellido, anno, nombre_dpto, nombre_corto_dpto, salario: int) -> None:
        Persona.__init__(self, nombre, apellido, anno)
        Departamento.__init__(self, nombre_dpto, nombre_corto_dpto)
        self.salario = salario

trabajador = Trabajador('Juan', 'Perez', '2005', 'Ingenieria de software', 'IS', 20000)
print(trabajador.__dict__)
#perdón por el nombre poco creativo de variables
InsTrabajador = isinstance(trabajador, Trabajador)
InsDepartamento = isinstance(trabajador, Departamento)
InsPersona = isinstance(trabajador, Persona)
print(f'Es trabajador instancia de Persona: {InsPersona}')
print(f'Es trabajador instancia de Departamento: {InsDepartamento}')
print(f'Es trabajador instancia de Trabajador: {InsTrabajador}')