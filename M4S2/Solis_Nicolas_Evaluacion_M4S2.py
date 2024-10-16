class Persona():
    def __init__(self, nombre, apellido, genero, edad: int, altura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.edad = edad
        self.altura = altura
        self.peso = peso

    def imprimir_nombre (self):
        print (self.nombre)

    def imprimir_apellido (self):
        print (self.apellido)

    def imprimir_genero (self):
        print (self.genero)

    def imprimir_altura (self):
        print (self.altura)

    def imprimir_peso (self):
        print (self.peso)

    #valores originales
    def get_edad(self):
            return self.edad

    def get_apellido(self):
            return self.apellido

    #para mutacion
    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_edad(self, edad):
        self.edad = edad

#para persona 1
persona_1 = Persona('Pedro', 'Vivas', 'Masculino', 20, '1.78 mts', '68 kg')

    #edad original persona 1
edad_falsa = persona_1.get_edad()
persona_1.set_edad(21)

print('La edad de {} indicaba {} años antes de que lo arrestaran con un carnet falso, ahora tiene {} años.'
    .format(persona_1.nombre, edad_falsa, persona_1.get_edad()))

#para Persona 2
persona_2 = Persona('Juan', 'Camargo', 'Masculino', 20, '1.8 mts', '75 kg')

    #apellido original persona 2
apellido_antiguo = persona_2.get_apellido()
persona_2.set_apellido('Santiago')

print('El apellido de {} era {} antes de cambiarlo en el registro civil, ahora es {}.'
    .format(persona_2.nombre, apellido_antiguo, persona_2.get_apellido()))