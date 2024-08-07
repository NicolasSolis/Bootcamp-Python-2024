#Creando una clase

class Vehiculo():
    ruedas = 4
    def desplazamiento(self):
        print('El vehiculo se esta desplazando sobre 4 ruedas')

miAuto = Vehiculo()
print("Mi vehiculo tiene ", miAuto.ruedas, " ruedas")
miAuto.desplazamiento()

    #Con metodo constructor

""" def __init__(self, color, aceleracion):
    self.color = color
    self.aceleracion = aceleracion
    self.velocidad = 0

auto1 = Vehiculo('Azul', 30)
auto2 = Vehiculo('Balco', 50) """

#Metodos accesadores y mutadores: para acceder y alterar datos almacenados internamente

    #Mutadores

""" class Vehiculo:
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0
    def set_color(self, color):
        self.color = color
    def get_color(self):
        return self.color """

miCarro1 = Vehiculo('Negro', '20')
print (miCarro1.get_color())
miCarro1.set_color('Blanco')
print (miCarro1.get_color())

#Colaboración objetos

""" class Vehiculo:
    def __init__(self, marca, color, ruedas):
        self.marca = marca
        self.color = color
        self.ruedas = ruedas

class datosVehiculos:
    def __init__(self):
        self.vehiculo = Vehiculo('TOYOTA', 'Rojo', 4)
        print('Datos del vehiculo:')
        print('Marca: ', self.vehiculo.marca)
        print('Color: ', self.vehiculo.color)
        print('Ruedas: ', self.vehiculo.ruedas)

carro = datosVehiculos() """