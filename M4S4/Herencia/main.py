from persona import Persona
from persona import Supervisor, Cliente

persona1 = Persona('Juan', 'Perez','123456')
persona2 = Persona('José', 'Sanchez','456789')

persona1.imprimir_datos()
print(persona1)
persona2.imprimir_datos()
print(persona2)

#sale 2 veces porque estamos imprimiendo 2 veces

supervisor1 = Supervisor('Juan', 'Perez','123456', 'Sur')
print("******")
supervisor1.imprimir_datos()
print("******")
supervisor1.imprimir_supervisor()
print("******")
print(supervisor1)

""" imprimir datos lo hereda de Persona, porque es un método público y su clase padre
    también heredaría los protegidos"""

cliente1 = Cliente('Juan', 'Perez','123456', 20)
print("******")
cliente1.imprimir_datos()
print("******")
cliente1.imprimir_cliente()
print("******")
print(cliente1)