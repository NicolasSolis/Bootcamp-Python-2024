class Persona:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def movimiento(self):
        return 'caminando' #no estaba devolviendo nada xd

class Maratonista(Persona):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
    def movimiento(self):
        return 'trotando'

class Ciclista(Persona):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
    def movimiento(self):
        return 'rodando'

persona = Persona('Pedro')
maratonista = Maratonista('Juan')
ciclista = Ciclista('Diego')

perMov = persona.movimiento()
marMov = maratonista.movimiento()
ciMov = ciclista.movimiento()

print(f'{persona.nombre} está {perMov} a su trabajo')
print(f'{maratonista.nombre} está {marMov} al estadio')
print(f'{ciclista.nombre} está {ciMov} en su bicicleta con un celular')