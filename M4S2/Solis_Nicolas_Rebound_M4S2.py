class Animal():
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso

    def imprimir_nombre (self):
        print (self.nombre)
    def imprimir_raza (self):
        print (self.raza)
    def imprimir_edad (self):
        print (self.edad)
    def imprimir_peso (self):
        print (self.peso)

#Estaba probando las funciones, no ocupé estas en este archivo.
    def get_nombre(self):
            return self.nombre
    def get_raza(self):
            return self.raza
    def get_edad(self):
            return self.edad
    def get_peso(self):
            return self.peso

caballo = Animal('Zeus', 'Pura sangre', '5 años', '450 kg')

leon = Animal('Boulder', 'Atlas', '10 años', '130 kg')

caballo.imprimir_nombre()
caballo.imprimir_raza()
caballo.imprimir_edad()
caballo.imprimir_peso()

print('\nExiste un caballo llamado {}, su raza es {}, tiene {} años de edad y pesa {}.'
    .format(caballo.nombre, caballo.raza, caballo.edad, caballo.peso))

print('----------')

leon.imprimir_nombre()
leon.imprimir_raza()
caballo.imprimir_edad()
caballo.imprimir_peso()

print('\nExiste un leon llamado {}, su raza es {}, tiene {} años de edad y pesa {}.'
    .format(leon.nombre, leon.raza, leon.edad, leon.peso))