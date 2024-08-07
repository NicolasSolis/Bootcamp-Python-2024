class Vehiculo:
    modelo = ''
    marca = ''
    color = ''
    velocidad = 0
    nro_puertas = 0
    kilometraje = 0
    encendido = False
    def encender(self):
        if not self.encendido:
            print('Encendiendo el vehiculo')
            self.encendido = True
        else:
    # Dale al encendido estando el coche arrancado y escucha...
            print('vehiculo encendido suena el arranque')
    def apagar(self):
        self.encendido = False
    def acelerar(self):
        if self.encendido:
            self.velocidad = self.velocidad + 1
    def frenar(self):
        if self.velocidad > 0:
            self.velocidad = self.velocidad - 1
    def get_velocidad(self):
        return self.velocidad
    def get_kilometraje(self):
        return self.kilometraje
    def set_kilometraje(self, kilometraje):
        self.kilometraje = kilometraje

def __init__(self, modelo, marca, color, nro_puertas, kilometraje):
    self.modelo = modelo
    self.marca = marca
    self.color = color
    self.velocidad = 0
    self.nro_puertas = nro_puertas
    self.kilometraje = kilometraje
    self.encendido = False

obj_carro1 = Vehiculo('Duro','Toyota', 'Blanco', 2, 2000)
obj_carro2 = Vehiculo('Uno','Fiat', 'Gris', 5, 100000)