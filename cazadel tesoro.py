#Caza del tesoro

import random
import sys

def dibTablero(tablero): #Estuctura del tablero
    lineah='   '
    for i in range(1,6):
        lineah+=(' '*9)+str(i)
        print('   '+('0123456789'*6))
        print()
        for i in range(15): #Imprime las 15 filas del tablero
            if i<10:
                espExtra=' '
            else:
                espExtra=''
            print('%s%s %s %s' % (espExtra, i, obtFila(tablero,i)))
        print()
        print('   '+('0123456789'*6))
        print(lineah)

def obtFila(tablero, fila):
    filaTab=''
    for i in range(60):
        filaTab+= tablero[i][fila]
    return filaTab

def obtNuevoTab():
    tablero=[]
    for x in range(60):
        tablero.append([])
        for y in range(15): #se utilizaran catacteres para simular el mar
            if random.randint(0,1)==0:
                tablero[x].append('~')
            else:
                tablero[x].append('´')
    return tablero

def obtCofresAl(): #crea posiciones aleatorias de posicion del cofre
    cofres=[]
    for i in range(numCofres):
        cofres.append([random.randint(0,59), random.randint(0,14)])
    return cofres

def movVal(x,y): #Comprueba si la jugada es valida
    return x>=0 and x<=59 and y>=0 and y<=14

def hacerMov(board, chests, x, y):
    if not movVal(x,y):
        return False
    minDist=100 #la distancia desde el sonar hasta el cofre no sera mayor a 100

    for cx, cy in cofres:
        if abs(cx-x) > abs(cy-y):
            dist= abs(cx-x)
        else:
            dist=abs(cy-y)
        if dist < minDist:
            minDist=dist
    if minDist==0: #estar encima de un tablero
        tablero.remove([x,y])
        return "Has encontrado el cofre del tesoro"
    else:
        if minDist < 10:
            tablero[x][y]=str(minDist)
            return "El tesoro esta a %s del sonar." %(minDist)
        else:
            tablero[x][y]='0'
            return "No se ha encontrado nada"

def meterMov(): #recoge la coordenada ofrecida por el jugador
    print("¿Que coordenada quieres introducir? (0-59) (0-14) ¿O prefieres salir? ")
    while True:
        movida=input()
        if movida.lower()=='salir':
            print("Hasta pronto!")
            sys.exit()
        movida=movida.split()
        if len(movida)==2 and movida[0].isdigit() and movida[1].isdigit() and movVal(int(movida[0]), int(movida[1])):
            return [int(movida[0]), int(movida[1])]
        print("Ingresa la posicion x (0-59) y luego la posicion y (0-14)")

def otraVez():
    print("¿Quieres jugar de nuevo? si/no")
    return input().lower().startswith('s')

def instrucciones():
    print('''Intrucciones: \n Eres el capitán de Simón, un buque cazador de tesoros. \nTu misión actual es encontrar los tres cofres con tesoros perdidos que se hallan ocultos en la parte del océano en que te encuentras y recogerlos.")
    Para jugar, ingresa las coordenadas del punto del océano en que quieres colocar un dispositivo sonar. \n El sonar puede detectar cuál es la distancia al cofre más cercano.")
    Por ejemplo, la de abajo indica dónde se ha colocado el dispositivo, \n y los números 2 representan los sitios a una distancia 2 del dispositivo. \nLos números 4 representan los sitios a una distancia 4 del dispositivo.")
    444444444
    4       4
    4 22222 4
    4 2   2 4
    4 2 d 2 4
    4 2   2 4
    4 22222 4
    4       4
    444444444''')

    print("Pulsa enter para continuar...")
    input()

    print('''Por ejemplo, aquí hay un cofre del tesoro (la c) ubicado a una distancia
    2 del dispositivo sonar (la d):
    22222
    c   2
    2 d 2
    2   2
    22222

    El punto donde el dispositivo fue colocado se indicará con una d.
    Los cofres del tesoro no se mueven. Los dispositivos sonar pueden detectar cofres hasta una distancia 9.
    Si todos los cofres están fuera del alcance, el punto se indicará con un O.

    Si un dispositivo es colocado directamente sobre un cofre del tesoro, has descubierto la ubicación del cofre,
    y este será recogido. El dispositivo sonar permanecerá allí.

    Cuando recojas un cofre, todos los dispositivos sonar se actualizarán para
    localizar el próximo cofre hundido más cercano.

    Pulsa enter para continuar...''')
    input()
    print()
    print('¡ S O N A R !')
    print()
    print('¿Te gustaría ver las instrucciones? (sí/no)')
    if input().lower().startswith('s'):
        instrucciones()

while True: #configuración del juego
    dispositivosSonar = 16
    elTablero = obtNuevoTab()
    losCofres = obtCofresAl(3)
    dibTablero(elTablero)
    movidasPrevias = []

    while dispositivosSonar > 0:
        #Comienzo de un turno:

        # mostrar el estado de los dispositivos sonar / cofres
        if dispositivosSonar > 1:
            extraSsonar = 's'
        else:
            extraSsonar = ''
        if len(losCofres) > 1:
            extraScofre = 's'
        else:
            extraScofre = ''
        print('Aún tienes %s dispositivos%s sonar. Falta encontrar %scofre%s.' % (dispositivosSonar, extraSsonar, len(losCofres), extraScofre))

        x, y = ingresarMovidaJugador()
        movidasPrevias.append([x, y]) # debemos registrar todas las movidas para que los dispositivos sonar puedan ser actualizados.

        resultadoMovida = realizarMovida(elTablero, losCofres, x, y)
        if resultadoMovida == False:
            continue
        else:
            if resultadoMovida == '¡Has encontrado uno de los cofres del tesoro!':
        #actualizar todos los dispositivos sonar presentes en el mapa.
                for x, y in movidasPrevias:
                    realizarMovida(elTablero, losCofres, x, y)
            dibujarTablero(elTablero)
            print(resultadoMovida)

        if len(losCofres) == 0:
            print('¡Has encontrado todos los cofres del tesoro! ¡Felicitaciones y buena partida!')
            break

        dispositivosSonar -= 1

    if dispositivosSonar == 0:
        print('¡Nos hemos quedado sin dispositivos sonar! ¡Ahora tenemos que dar la vuelta y dirigirnos')
        print('de regreso a casa dejando tesoros en el mar! Juego terminado.')
        print(' Los cofres restantes estaban aquí:')
        for x, y in losCofres:
            print(' %s, %s' % (x, y))

    if not otraVez():
        sys.exit()