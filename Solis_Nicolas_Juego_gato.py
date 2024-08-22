import random

#Establecer tablero, tipo numérico 0 - 9 (o range(8)). Saludos a P4HBionics 03/08/2024
def mostrar_tablero(tablero):
    print(f' {tablero[0]} | {tablero[1]} | {tablero[2]} ')
    print('---*---*---')
    print(f' {tablero[3]} | {tablero[4]} | {tablero[5]} ')
    print('---*---*---')
    print(f' {tablero[6]} | {tablero[7]} | {tablero[8]} ')

def verificar_ganador(tablero):
    # Verificando horizontales
    if tablero[0] == tablero[1] == tablero[2] != ' ':
        return tablero[0]
    if tablero[3] == tablero[4] == tablero[5] != ' ':
        return tablero[3]
    if tablero[6] == tablero[7] == tablero[8] != ' ':
        return tablero[6]

    # Verificando verticales
    if tablero[0] == tablero[3] == tablero[6] != ' ':
        return tablero[0]
    if tablero[1] == tablero[4] == tablero[7] != ' ':
        return tablero[1]
    if tablero[2] == tablero[5] == tablero[8] != ' ':
        return tablero[2]

    # Verificando diagonales
    if tablero[0] == tablero[4] == tablero[8] != ' ':
        return tablero[0]
    if tablero[2] == tablero[4] == tablero[6] != ' ':
        return tablero[2]

    return None

#Función inicio, fix: ahora con jugador aleatorio
def jugar_gato():
    while True:
        tablero = [' '] * 9
        jugador_actual = random.choice(['X', 'O'])

        while True:
            mostrar_tablero(tablero)
            while True:
                print(' ')
                print('---------------------')
                jugada = input(f'Jugador {jugador_actual}, ingresa tu jugada (1-9): ')
                try:
                    #Atrapar input inválidos
                    jugada = int(jugada)
                    if jugada < 1 or jugada > 9:
                        print('Error: Tu jugada debe ser un número entre 1 y 9!')
                        continue
                    break
                except ValueError:
                    print('Error: Tu jugada debe ser un número entre 1 y 9!')
                    continue
            jugada -= 1

            if tablero[jugada] != ' ':
                print(' ')
                print('---------------------')
                print('Error:\nCasilla ocupada, por favor intenta de nuevo.')
                continue

            tablero[jugada] = jugador_actual

            ganador = verificar_ganador(tablero)
            if ganador:
                mostrar_tablero(tablero)
                print(f'Ganóo, {ganador} gana todoo! Felicitaciones')
                break
            #Break si el tablero se completa en empate
            if ' ' not in tablero:
                print('Empate, en teoría ambos perdieron!')
                break

            jugador_actual = 'O' if jugador_actual == 'X' else 'X'
            #¿Jugar de nuevo? para gente entretenida
        revancha = input('¿Deseas jugar nuevamente (s/n): ')
        if revancha.lower() == 'n':
            break

jugar_gato()