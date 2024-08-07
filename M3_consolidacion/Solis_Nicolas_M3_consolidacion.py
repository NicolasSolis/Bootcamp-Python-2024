#lista nombres
nombres = [
            'Harry Houdini', #0, mago
            'Newton',       #1 cientifico
            'David Blaine', #2, mago
            'Hawking',      #3 cientifico
            'Messi',        #4 otro
            'Teller',       #5 mago
            'Einstein',     #6 cientifico
            'Pele',         #7 otro
            'Juanes'        #8 otro
]

#separando por categorías
magos = [nombre for i, nombre in enumerate(nombres) if i in [0, 2, 5]]
cientificos = [nombre for i, nombre in enumerate(nombres) if i in [1, 3, 6]]
otros = [nombre for i, nombre in enumerate(nombres) if i in [4, 7, 8]]

#función hacer grandioso
def hacer_grandioso(magos):
    return [f'El gran {mago}' for mago in magos]

grandes_magos = hacer_grandioso(magos)

#función imprimir lista completa
def imprimir_nombres(lista_completa):
    for nombres in lista_completa:
        print(f'Famoso: {nombres}')

#resultado
imprimir_nombres(nombres)

print(f'De estos famosos, los grandes magos son: {grandes_magos}')
print(f'De estos famosos, los científicos son: {cientificos}')
print(f'De estos famosos, los que no son magos ni científicos son: {otros}')