#área de un rectángulo
b = 30
h = 15

area = (b * h)
print(f'Área de rectángulo es: {area}')

#celsius a fahrenheit
c = 30
f = ((c * 9/5) + 32)

fahrenheit = f
print(f"{c} grados Celsius son {fahrenheit} grados Fahrenheit")

#calculadora propinas
cuenta = float(input("ingrese el total de su cuenta, solo números enteros porfs "))
propina = float(input("ingrese porcentaje de propina, solo el número "))

propina = cuenta * (propina/100)
total = (cuenta + propina)

print(f"El monto de su cuenta es ${cuenta:.2f}, más propina es ${total:.2f}")

##
""" print(sum([1, 2, 3, 4, 5])) """

#gestión de inventario, cantidad en cajas (10c/u)
inventario = {
    'libros':'40', 
    'escritorios':'20', 
    'estantes':'24', 
    'cuadernos':'83'
} 
#se compraron cosas random, pero se echaron a perder los libros (mojados), tragedia.
inventario.update({'sillas_gamer':'3'})
del inventario['libros']
print(inventario)

#lista de tareas
tareas = ['dormir', 'soñar', 'comer', 'despertar', 'bañarse', 'correr']
    #agregar tarea 
tareas.insert(1, 'despertar')
    #agregar tarea
tareas.append(tareas.pop(2))
    #eliminar tarea
tareas.remove("bañarse")

print(tareas)

#registro calificaciones
calificaciones = {
    "Juan": [85, 92, 78, 90],
    "María": [80, 85, 92, 88],
    "Pedro": [75, 82, 88, 91]
}

# Agregar una calificación a un estudiante
calificaciones["Juan"].append(88)

# Modificar una calificación
calificaciones["María"][2] = 90

# Eliminar una calificación
del calificaciones["Pedro"][1]

# Calcular el promedio de calificaciones de un estudiante
estudiante = "Juan"
promedio = sum(calificaciones[estudiante]) / len(calificaciones[estudiante])
print(f"El promedio de {estudiante} es: {promedio:.2f}")