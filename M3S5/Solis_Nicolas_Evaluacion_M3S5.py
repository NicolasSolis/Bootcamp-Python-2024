palabra = 'paralelepipedo'
#vocales excluidas por iterar palabra en vez de replace()
vocales = 'aeiou'

#era para contar las letras xd
""" print(len(palabra)) """

#iterar caracteres de palabra
for i, letra in enumerate(palabra):
    if letra.lower() not in vocales:
        print(f'La letra {letra} en la posición (índice) {i} es una consonante')