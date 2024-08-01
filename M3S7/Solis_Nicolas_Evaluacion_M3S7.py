#robado para calcular nº primos
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

estudiantes = [ 
    {'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]},
    {'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]},
    {'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]},
    {'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]},
    {'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]},
]

for alumno in estudiantes:
    if alumno['edad'] > 18:
        #en este caso len calificaciones es 3 nomas
        promedio = sum(alumno['calificaciones']) / len(alumno['calificaciones']) 
        if promedio > 85:
                print(f'nombre: {alumno['nombre']}')
                print(f'edad: {alumno['edad']}')
                print(f'calificaciones: {alumno['calificaciones']}')
                print(f'promedio: {promedio:.2f}')
                print('-')

#solo 19 es nº primo, pero se puede extender a otros casos:
print('Estudiantes mayor a 18 y cuyas edades sean nº primos:')
for alumno in estudiantes:
    if alumno['edad'] > 18 and es_primo(alumno['edad']):
        promedio = sum(alumno['calificaciones']) / len(alumno['calificaciones'])
        print(f'nombre: {alumno['nombre']}')
        print(f'edad: {alumno['edad']}')
        print(f'calificaciones: {alumno['calificaciones']}')
        print(f'promedio: {promedio:.2f}')