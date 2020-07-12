#3 en raya
import random

def dibujarTablero(tablero):
    '''Esta función dibuja el tablero recibido como argumento. "tablero" es una lista de 10 cadenas representando la pizarra (ignora índice 0)'''
    print('   |   | ')
    print(' ' + tablero[7] + ' | ' + tablero[8] + ' | ' + tablero[9])
    print('   |   | ')
    print('-----------')
    print('   |   | ')
    print(' ' + tablero[4] + ' | ' + tablero[5] + ' | ' + tablero[6])
    print('   |   | ')
    print('-----------')
    print('   |   | ')
    print(' ' + tablero[1] + ' | ' + tablero[2] + ' | ' + tablero[3])
    print('   |   | ')

def ingresaLetraJugador():
    '''Permite al jugador escoger letra desea ser.'''
    # Devuelve una lista con dos letras, de las cuales la 1aes del juador y la 2a del ordenador.
    letra = ''
    while not (letra == 'O' or letra == 'X'):
        print('¿Deseas ser X o O?')
        letra = input().upper()
    if letra == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def quienComienza(): # Elije al azar que jugador comienza.
    if random.randint(0, 1) == 0:
        return 'La computadora'
    else:
        return 'El jugador'

def otraVez(): # Esta funcion devuelve True (Verdadero) si el jugador desea volver a jugar, de lo contrario devuelve False (Falso).
    print('¿Quieres jugar de nuevo? (sí/no)?')
    return input().lower().startswith('s')

def hacerJugada(tablero, letra, jugada):
    tablero[jugada] = letra

def Ganar(pos, letra): # Utilizamos pos para la posicion y letra para la letra jugada
    return ((pos[7] == letra and pos[8] == letra and pos[9] == letra) or # linea horizontal superior
        (pos[4] == letra and pos[5] == letra and pos[6] == letra) or # linea horizontal medio
        (pos[1] == letra and pos[2] == letra and pos[3] == letra) or # linea horizontal inferior
        (pos[7] == letra and pos[4] == letra and pos[1] == letra) or # linea vertical izquierda
        (pos[8] == letra and pos[5] == letra and pos[2] == letra) or # linea vertical medio
        (pos[9] == letra and pos[6] == letra and pos[3] == letra) or # linea vertical derecha
        (pos[7] == letra and pos[5] == letra and pos[3] == letra) or # linea diagonal
        (pos[9] == letra and pos[5] == letra and pos[1] == letra)) # linea diagonal

def obtenerDuplicadoTablero(tablero): # Duplica la lista del tablero y devuelve el duplicado.
    dupTablero = []
    for i in tablero:
        dupTablero.append(i)
    return dupTablero

def hayEspacioLibre(tablero, jugada): #Comprueba si esa posicion no ha sido usada
    return tablero[jugada] == ' '

def obtenerJugadaJugador(tablero): #Recoge la jugada del jugador
    jugada = ' '
    while jugada not in '9 8 7 6 5 4 3 2 1'.split() or not hayEspacioLibre(tablero, int(jugada)):
        print('¿Cuál es tu próxima jugada? (1-9)')
        jugada = input()
    return int(jugada)

def elegirAzarDeLista(tablero, listaJugada): # Devuelve si una jugada es valida
    jugadasPosibles = []
    for i in listaJugada:
        if hayEspacioLibre(tablero, i):
            jugadasPosibles.append(i)

    if len(jugadasPosibles) != 0:
        return random.choice(jugadasPosibles)
    else:
        return None

def obtenerJugadaComputadora(tablero, letraComputadora): # Dado un tablero y la letra de la computadora, determina que jugada efectuar.
    if letraComputadora == 'X':
        letraJugador = 'O'
    else:
        letraJugador = 'X'
    # Aquí está nuestro algoritmo para nuestra IA (Inteligencia Artifical) del 3 en raya.
    # Primero, verifica si podemos ganar en la próxima jugada
    for i in range(1, 10):
        copia = obtenerDuplicadoTablero(tablero)
        if hayEspacioLibre(copia, i):
            hacerJugada(copia, letraComputadora, i)
            if Ganar(copia, letraComputadora):
                return i
    # Verifica si el jugador podría ganar en su próxima jugada, y lo bloquea.
    for i in range(1, 10):
        copia = obtenerDuplicadoTablero(tablero)
        if hayEspacioLibre(copia, i):
            hacerJugada(copia, letraJugador, i)
            if Ganar(copia, letraJugador):
                return i
    # Intenta ocupar una de las esquinas de estar libre.
    jugada = elegirAzarDeLista(tablero, [1, 3, 7, 9])
    if jugada != None:
        return jugada
    # De estar libre, intenta ocupar el centro.
    if hayEspacioLibre(tablero, 5):
        return 5
    # Ocupa alguno de los lados.
    return elegirAzarDeLista(tablero, [2, 4, 6, 8])

def tableroCompleto(tablero):   # Devuelve True si cada espacio del tablero fue ocupado, caso contrario devuele False.
    for i in range(1, 10):
        if hayEspacioLibre(tablero, i):
            return False
    return True

print('¡Bienvenido al 3 en Raya!')

while True: # Resetea el tablero
    elTablero = [' '] * 10
    letraJugador, letraComputadora = ingresaLetraJugador()
    turno = quienComienza()
    print(turno + ' irá primero.')
    juegoEnCurso = True

    while juegoEnCurso:
        if turno == 'El jugador': # Turno del jugador
            dibujarTablero(elTablero)
            jugada = obtenerJugadaJugador(elTablero)
            hacerJugada(elTablero, letraJugador, jugada)
            if Ganar(elTablero, letraJugador):
                dibujarTablero(elTablero)
                print('¡Felicidades, has ganado!')
                juegoEnCurso = False
            else:
                if tableroCompleto(elTablero):
                    dibujarTablero(elTablero)
                    print('¡Es un empate!')
                    break
                else:
                    turno = 'La computadora'
        else: # Turno de la computadora
            jugada = obtenerJugadaComputadora(elTablero, letraComputadora)
            hacerJugada(elTablero, letraComputadora, jugada)
            if Ganar(elTablero, letraComputadora):
                dibujarTablero(elTablero)
                print('¡La computadora te ha vencido! Has perdido.')
                juegoEnCurso = False
            else:
                if tableroCompleto(elTablero):
                    dibujarTablero(elTablero)
                    print('¡Es un empate!')
                    break
                else:
                    turno = 'El jugador'
    if not otraVez():
            break