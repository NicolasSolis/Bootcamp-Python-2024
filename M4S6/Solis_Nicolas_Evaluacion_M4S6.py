usuarios = {'001': 'Marca', '002': 'Mónica', '003': 'Jacob'}

try:
    print(usuarios['004'])
except KeyError:
    print('La clave 004 no está en el diccionario. Añadiendo clave...')

usuarios['004'] = 'Ninguno'
print(usuarios)