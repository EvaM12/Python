# -*- coding: utf-8 -*-

"""Para poder introducir numeros aleatorios y un reloj"""
import random
import time
import gtk

"""Variables Globales para construir el tablero"""
COE, CNS, CES, CSO, CNE, CON, COES, CNES, CONS, CONE, CSOM, BLANK = u'\u2500', u'\u2502', u'\u250C', u'\u2510', u'\u2514', u'\u2518', u'\u252C', u'\u251C', u'\u2524', u'\u2534', u'\u2593', u'\u00A0'
letracol, letrafil = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t",
                      "u", "v",
                      "w", "y", "z", "=", "+", "-", ":", "/"], ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                                                                "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                                                                "V", "W", "X", "Y", "Z", "@", "#", "$", "%", "&"]
coory1, coorx1 = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9,
                  "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18,
                  "t": 19, "u": 20, "v": 21, "w": 22, "y": 23, "z": 24, "=": 25, "+": 26, "-": 27,
                  ":": 28, "/": 29}, {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9,
                                      "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18,
                                      "T": 19, "U": 20, "V": 21, "W": 22, "Y": 23, "Z": 24, "@": 25, "#": 26, "$": 27,
                                      "%": 28, "&": 29}

class prueba():
    def __init__(self):
        self.glade=gtk.Builder()
        self.glade.add_from_file('Prueba.glade')
        self.ventana=self.glade.get_object('window1')
        self.pulsadores=self.glade.get_object('vbox1').get_children()
        self.glade.connect_signals(self)
        self.ventana.show()
    def on_window1_delete_event(self,widget,event):
        gtk.main_quit()
    def on_pulsador_clicked(self,widget):
        for i in range(len(self.pulsadores)):
            if self.pulsadores[i]==widget:
                i=i+1
                seleccion(i)

def menu():
    ''''Imprime en pantalla el menu con sus opciones, utiliza la variable modo (cuyo valor le da el usuario)'''
    print ("Menú \n----------")
    print (" 1. Principiante (9x9, 10 minas) \n 2. Intermedio (16x16, 40 minas) \n 3. Experto (16x30, 99 minas) \n 4. Leer de fichero \n 5. Salir")
    modo = int(raw_input('Escoja opcion: '))
    while modo == 0 or modo > 5:
        modo = int(raw_input("Valor no disponible, introduzca un valor entre 1 y 5: "))
    seleccion(modo)


def seleccion(modo):
    ''''Usa la variable modo para indicar la extensión del tablero o para leer de fichero (falta)/Sobra dibujar el segundo tablero/'''
    if modo == 1:
        fil, col, minas = 9, 9, 16
        iniciojuego(fil, col, minas)
    if modo == 2:
        fil, col, minas = 16, 16, 40
        iniciojuego(fil, col, minas)
    if modo == 3:
        fil, col, minas = 16, 30, 99
        iniciojuego(fil, col, minas)
    if modo == 4:
        tab2, minas, fil, col = leerarch()
        tab2 = estadoceldaini(fil, col, tab2)
        tab = creartab(fil, col)
        dibtab(fil, col, tab)
        t1 = time.time()
        jugada(fil, col, tab, tab2, minas, t1)


def seleccion(modo):
    ''''Usa la variable modo para indicar la extensión del tablero o para leer de fichero (falta)/Sobra dibujar el segundo tablero/'''
    if modo == 1:
        fil, col, minas = 9, 9, 16
        iniciojuego(fil, col, minas)
    if modo == 2:
        fil, col, minas = 16, 16, 40
        iniciojuego(fil, col, minas)
    if modo == 3:
        fil, col, minas = 16, 30, 99
        iniciojuego(fil, col, minas)
    if modo == 4:
        tab2, minas, fil, col = leerarch()
        tab2 = estadoceldaini(fil, col, tab2)
        tab = creartab(fil, col)
        dibtab(fil, col, tab)
        t1 = time.time()
        jugada(fil, col, tab, tab2, minas, t1)


def iniciojuego(fil, col, minas):
    """Realiza la creación de los tableros y el inicio del cronómetro"""
    tab = creartab(fil, col)
    dibtab(fil, col, tab)
    t1 = time.time()
    tab2 = mina(fil, col, minas)
    dibtab(fil, col, tab2)
    jugada(fil, col, tab, tab2, minas, t1)


def leerarch():
    """Se encarga de leer el tablero de un fichero, para usarlo como tablero de juego"""
    fil, col = 0, 0
    while fil > 30 or col > 30 or fil <= 0 or col <= 0:
        archivo = raw_input("Introduzca el nombre del archivo en el que se encuentra el tablero: ")
        archivo = open(str(archivo), "r")
        contenido = archivo.read()
        contenido3 = contenido.split()
        fil, col = int(contenido3[0]), int(contenido3[1])
    tablero, minas = creartab(fil, col), 0
    for i in range(0, fil):
        for j in range(0, col):
            if list(contenido3[i + 2])[j] == ".":
                tablero[i][j] = BLANK
            if list(contenido3[i + 2])[j] == "*":
                tablero[i][j], minas = "*", minas + 1
    return tablero, minas, fil, col


def creartab(fil, col):
    """Crea el tablero máscara, es decir el que tapa el tablero de juego"""
    tablero = [CSOM] * fil
    for i in range(0, fil):
        tablero[i] = [CSOM] * col
    return tablero


def dibmarco(col):
    ''' Dibujar el marco de coordenadas horizantal (a,b,c,d,e,f,g...) '''
    for i in range(0, col):
        if i == 0:
            print (BLANK * 5),
        else:
            print (BLANK * 2),
        if i < col - 1:
            print (letracol[i]),
        else:
            print (letracol[i])


def dibtab(fil, col, tablero):
    ''' Filas estandar para dibujo de una casilla '''
    sup, inf, inf2, cier = BLANK * 4 + CES + (COE * 3 + COES) * (col - 1) + COE * 3 + CSO, CES + COE + CONE + (
            COE + COES + COE + CONE) * (col - 1) + COE + COES + COE + CON, CNE + COE + COES + (
                                   COE + CONE + COE + COES) * (col - 1) + COE + CONE + COE + CSO, CNE + (
                                   COE * 3 + CONE) * (col - 1) + COE * 3 + CON
    dibmarco(col)
    """Dibuja el tablero en pantalla"""
    print (sup)
    for i in range(0, fil):
        print (letrafil[i] + BLANK),
        if i % 2 == 0:
            print (BLANK * 2),
        for j in range(0, col):
            print (CNS + BLANK + tablero[i][j] + BLANK),
            if j == col - 1:
                print (CNS)
        if i % 2 == 0 and i != fil - 1:
            print (BLANK * 2 + inf)
        elif i != fil - 1:
            print (BLANK * 2 + inf2)
        else:
            if i % 2 == 0:
                print (BLANK * 2),
            print (BLANK * 2 + cier)


def mina(fil, col, minas):
    ''' Nuevo tablero con las minas, 0: no hay mina, 1: hay mina '''
    campminas = [BLANK] * fil
    for i in range(0, fil):
        campminas[i] = [BLANK] * col
    '''Asignación de bombas, posicion de tablero aleatoria'''
    while minas > 0:
        i, j = random.randrange(fil), random.randrange(col)
        if campminas[i][j] == BLANK:
            campminas[i][j], minas = "*", minas - 1
    campminas = estadoceldaini(fil, col, campminas)
    return campminas


def estadoceldaini(fil, col, campminas):
    ''' Informa sobre la adyacencia de minas '''
    for i in range(0, fil):
        for j in range(0, col):
            if campminas[i][j] != "*" and campminas[i][j] != "X":
                cont = condiciones(i, j, fil, col, campminas, "*")
                if cont > 0:
                    campminas[i][j] = str(cont)
                else:
                    campminas[i][j] = BLANK
    return campminas


def estadocelda(fil, col, campminas, tabor):
    ''' Informa sobre la adyacencia de minas, y sobre la adyacencia de X '''
    for i in range(0, fil):
        for j in range(0, col):
            if campminas[i][j] != "*" and campminas[i][j] != "X":
                cont, cont2 = condiciones(i, j, fil, col, campminas, "*"), condiciones(i, j, fil, col, campminas, "X")
                if tabor[i][j] == BLANK:
                    tabor[i][j] = 0
                numero = int(tabor[i][j]) - cont2
                if numero > 0:
                    campminas[i][j] = str(cont)
                elif numero == 0:
                    campminas[i][j] = BLANK
                else:
                    campminas[i][j] = "?"
                if tabor[i][j] == 0:
                    tabor[i][j] = BLANK
    return campminas


def copia(tab2, fil, col):
    """Crea el tablero original, una copia de tablero 2"""
    tabor = creartab(fil, col)
    for i in range(0, fil):
        for j in range(0, col):
            tabor[i][j] = tab2[i][j]
    return tabor


def metodo(fil, col, tab, tab2):
    """tab es una mascara de tab2, esta funcion, si el valor esta destapado, copia al tablero visible los valores de
    juego """
    for i in range(0, fil):
        for j in range(0, col):
            if tab[i][j] != CSOM:
                tab[i][j] = tab2[i][j]
    return tab


def jugada(fil, col, tab, tab2, minas, t1):
    """Efectúa la jugada/i,j,z hacen de separadores mayuscula, minuscula y operacion/num es la longitud de la cadena introducida
    por si se quiere introducir mas de una coordenada a la vez"""
    tabor, marcas, end, error, primera = copia(tab2, fil, col), minas, False, False, True
    while minas > 0 and end == False:
        coordenadas = raw_input('Indique la celda y accion (! marcar, *abrir): ')
        num = int(len(coordenadas) / 3)
        for x in range(0, num):
            i, j, z = coorx1[coordenadas[0 + 3 * x]], coory1[coordenadas[1 + 3 * x]], coordenadas[2 + 3 * x]
            if i > fil + 1 or j > col + 1:
                print ("\nCoordenadas incorectas, por favor vuelva a introducir coordenadas\n")
            else:
                if z == "*":
                    if primera == True and tab2[i][j] == "*":
                        tab2[i][j]=BLANK
                        for k in range(0, fil):
                            for l in range(0, col):
                                if tab2[k][l]==BLANK:
                                    tab2[k][l]="*"
                        tabor=copia(tab2, fil, col)
                        tab2 = estadocelda(fil, col, tab2, tabor)
                    else:
                        if tab[i][j] == "X":
                            print ("\nNO SE PUEDE ABRIR UNA CELDA MARCADA\n")
                        elif tab2[i][j] == "*":
                            end = True
                        elif tab[i][j] == CSOM or tab[i][j] == BLANK:
                            tab = blancosiono(i, j, fil, col, tab2, tab, 1)
                        else:
                            print ("\nCELDA YA ABIERTA. NO SE PUEDEN ABRIR LAS CELDAS VECINAS POR NUMERO INSUFICIENTE DE MARCAS\n")
                elif z == "!":
                    if marcas == 0:
                        print ("\nNO SE PUEDE MARCAR MAS CELDAS QUE MINAS\n")
                    else:
                        if tab[i][j] == "X":
                            tab[i][j], tab2[i][j] = CSOM, tabor[i][j]
                            tab2 = estadocelda(fil, col, tab2, tabor)
                            metodo(fil, col, tab, tab2)
                            minas, marcas = minas + 1, marcas + 1
                        elif tab[i][j] == BLANK:
                            print ("\nNO SE PUEDE MARCAR UNA CELDA ABIERTA\n")

                        else:
                            tab2[i][j], tab[i][j] = "X", "X"
                            tab2, minas, marcas = estadocelda(fil, col, tab2, tabor), minas - 1, marcas - 1
                            metodo(fil, col, tab, tab2)
                else:
                    print ("\nENTRADA ERRONEA\n")
            tab2 = estadocelda(fil, col, tab2, tabor)
            primera=False
        t2 = time.time()
        tiempo = t2 - t1
        if end == False:
            print ("MINAS RESTANTES: " + str(minas) + " | MARCADAS: " + str(marcas) + "| TIEMPO: " + str(
                tiempo) + " seg")
            dibtab(fil, col, tab)
    fin(end, tiempo)
    print ("MINAS RESTANTES: " + str(minas) + " | MARCADAS: " + str(marcas) + "| TIEMPO: " + str(tiempo) + " seg")
    dibtab(fil, col, tab)
    tabor = imptabsol(fil, col, tabor, tab)
    dibtab(fil, col, tabor)
    print ("\n\n")
    menu()


def fin(end, tiempo):
    """Mensaje de fin de programa"""
    if end is True:
        print ("\n --------------------Game over--------------------\n")
    else:
        print ("\n --------------------¡Enhorabuena!--------------------\n", "Ha tardado: " + tiempo + "segundos en completar el tablero")


def blancosiono(i, j, fil, col, tab2, tab, control):
    """funcion recursiva, destapa las casillas blancas adyacentes"""
    if tab2[i][j] != BLANK and tab2[i][j] != "*":
        tab[i][j] = tab2[i][j]
    if tab2[i][j] == BLANK and (tab[i][j] != BLANK or control == 1):
        tab[i][j] = tab2[i][j]
        if i != fil - 1 and i != 0 and j != 0 and j != col - 1:
            if tab2[i + 1][j] != "*":
                blancosiono(i + 1, j, fil, col, tab2, tab, 0)
            if tab2[i - 1][j] != "*":
                blancosiono(i - 1, j, fil, col, tab2, tab, 0)
            if tab2[i][j - 1] != "*":
                blancosiono(i, j - 1, fil, col, tab2, tab, 0)
            if tab2[i][j + 1] != "*":
                blancosiono(i, j + 1, fil, col, tab2, tab, 0)
            if i % 2 == 0:
                if tab2[i + 1][j + 1] != "*":
                    blancosiono(i + 1, j + 1, fil, col, tab2, tab, 0)
                if tab2[i - 1][j + 1] != "*":
                    blancosiono(i - 1, j + 1, fil, col, tab2, tab, 0)
            else:
                if tab2[i + 1][j - 1] != "*":
                    blancosiono(i + 1, j - 1, fil, col, tab2, tab, 0)
                if tab2[i - 1][j - 1] != "*":
                    blancosiono(i - 1, j - 1, fil, col, tab2, tab, 0)
        if i == 0 and j == 0:
            if tab2[i + 1][j] != "*":
                blancosiono(i + 1, j, fil, col, tab2, tab, 0)
            if tab2[i][j + 1] != "*":
                blancosiono(i, j + 1, fil, col, tab2, tab, 0)
            if tab2[i + 1][j + 1] != "*":
                blancosiono(i + 1, j + 1, fil, col, tab2, tab, 0)
        if i == 0 and j != 0 and j != col - 1:
            if tab2[i + 1][j] != "*":
                blancosiono(i + 1, j, fil, col, tab2, tab, 0)
            if tab2[i][j - 1] != "*":
                blancosiono(i, j - 1, fil, col, tab2, tab, 0)
            if tab2[i][j + 1] != "*":
                blancosiono(i, j + 1, fil, col, tab2, tab, 0)
            if tab2[i + 1][j + 1] != "*":
                blancosiono(i + 1, j + 1, fil, col, tab2, tab, 0)
        if i == 0 and j == col - 1:
            if tab2[i + 1][j] != "*":
                blancosiono(i + 1, j, fil, col, tab2, tab, 0)
            if tab2[i][j - 1] != "*":
                blancosiono(i, j - 1, fil, col, tab2, tab, 0)
        if i != 0 and j == col - 1 and i != fil - 1:
            if tab2[i][j - 1] != "*":
                blancosiono(i, j - 1, fil, col, tab2, tab, 0)
            if tab2[i - 1][j] != "*":
                blancosiono(i - 1, j, fil, col, tab2, tab, 0)
            if tab2[i + 1][j] != "*":
                blancosiono(i + 1, j, fil, col, tab2, tab, 0)
            if i % 2 != 0:
                if tab2[i + 1][j - 1] != "*":
                    blancosiono(i + 1, j - 1, fil, col, tab2, tab, 0)
                if tab2[i - 1][j - 1] != "*":
                    blancosiono(i - 1, j - 1, fil, col, tab2, tab, 0)
        if i != 0 and j == 0 and i != fil - 1:
            if tab2[i][j + 1] != "*":
                blancosiono(i, j + 1, fil, col, tab2, tab, 0)
            if tab2[i - 1][j] != "*":
                blancosiono(i - 1, j, fil, col, tab2, tab, 0)
            if tab2[i + 1][j] != "*":
                blancosiono(i + 1, j, fil, col, tab2, tab, 0)
            if i % 2 == 0:
                if tab2[i + 1][j + 1] != "*":
                    blancosiono(i + 1, j + 1, fil, col, tab2, tab, 0)
                if tab2[i - 1][j + 1] != "*":
                    blancosiono(i - 1, j + 1, fil, col, tab2, tab, 0)
        if i == fil - 1 and j == col - 1:
            if tab2[i][j - 1] != "*":
                blancosiono(i, j - 1, fil, col, tab2, tab, 0)
            if tab2[i - 1][j] != "*":
                blancosiono(i - 1, j, fil, col, tab2, tab, 0)
            if i % 2 != 0:
                if tab2[i - 1][j - 1] != "*":
                    blancosiono(i - 1, j - 1, fil, col, tab2, tab, 0)
        if i == fil - 1 and j == 0:
            if tab2[i][j + 1] != "*":
                blancosiono(i, j + 1, fil, col, tab2, tab, 0)
            if tab2[i - 1][j] != "*":
                blancosiono(i - 1, j, fil, col, tab2, tab, 0)
            if i % 2 == 0:
                if tab2[i - 1][j + 1] != "*":
                    blancosiono(i - 1, j + 1, fil, col, tab2, tab, 0)
        if i == fil - 1 and j != 0 and j != col - 1:
            if tab2[i - 1][j] != "*":
                blancosiono(i - 1, j, fil, col, tab2, tab, 0)
            if tab2[i][j + 1] != "*":
                blancosiono(i, j + 1, fil, col, tab2, tab, 0)
            if tab2[i][j - 1] != "*":
                blancosiono(i, j - 1, fil, col, tab2, tab, 0)
            if i % 2 == 0:
                if tab2[i - 1][j + 1] != "*":
                    blancosiono(i - 1, j + 1, fil, col, tab2, tab, 0)
            else:
                if tab2[i - 1][j - 1] != "*":
                    blancosiono(i - 1, j - 1, fil, col, tab2, tab, 0)
    return tab


def imptabsol(fil, col, tabor, tab2):
    """Añade al tablero solucion el caracter:#, casilla abierta, marcada y no contiene mina"""
    for i in range(0, fil):
        for j in range(0, col):
            if tab2[i][j] == "X":
                if tabor[i][j] != "*":
                    tabor[i][j] = "#"
                else:
                    tabor[i][j] = "X"
    return tabor


def condiciones(i, j, fil, col, tab, valor):
    """Hace de contador de tablero basado en la adyacencia en base a un valor dado"""
    cont = 0
    if i != fil - 1 and i != 0 and j != 0 and j != col - 1:
        if tab[i + 1][j] == valor:
            cont = cont + 1
        if tab[i - 1][j] == valor:
            cont = cont + 1
        if tab[i][j - 1] == valor:
            cont = cont + 1
        if tab[i][j + 1] == valor:
            cont = cont + 1
        if i % 2 == 0:
            if tab[i + 1][j + 1] == valor:
                cont = cont + 1
            if tab[i - 1][j + 1] == valor:
                cont = cont + 1
        else:
            if tab[i + 1][j - 1] == valor:
                cont = cont + 1
            if tab[i - 1][j - 1] == valor:
                cont = cont + 1
    if i == 0 and j == 0:
        if tab[i + 1][j] == valor:
            cont = cont + 1
        if tab[i][j + 1] == valor:
            cont = cont + 1
        if tab[i + 1][j + 1] == valor:
            cont = cont + 1
    if i == 0 and j != 0 and j != col - 1:
        if tab[i + 1][j] == valor:
            cont = cont + 1
        if tab[i][j - 1] == valor:
            cont = cont + 1
        if tab[i][j + 1] == valor:
            cont = cont + 1
        if tab[i + 1][j + 1] == valor:
            cont = cont + 1
    if i == 0 and j == col - 1:
        if tab[i + 1][j] == valor:
            cont = cont + 1
        if tab[i][j - 1] == valor:
            cont = cont + 1
    if i != 0 and j == col - 1 and i != fil - 1:
        if tab[i][j - 1] == valor:
            cont = cont + 1
        if tab[i - 1][j] == valor:
            cont = cont + 1
        if tab[i + 1][j] == valor:
            cont = cont + 1
        if i % 2 != 0:
            if tab[i + 1][j - 1] == valor:
                cont = cont + 1
            if tab[i - 1][j - 1] == valor:
                cont = cont + 1
    if i != 0 and j == 0 and i != fil - 1:
        if tab[i][j + 1] == valor:
            cont = cont + 1
        if tab[i - 1][j] == valor:
            cont = cont + 1
        if tab[i + 1][j] == valor:
            cont = cont + 1
        if i % 2 == 0:
            if tab[i + 1][j + 1] == valor:
                cont = cont + 1
            if tab[i - 1][j + 1] == valor:
                cont = cont + 1
    if i == fil - 1 and j == col - 1:
        if tab[i][j - 1] == valor:
            cont = cont + 1
        if tab[i - 1][j] == valor:
            cont = cont + 1
        if i % 2 != 0:
            if tab[i - 1][j - 1] == valor:
                cont = cont + 1
    if i == fil - 1 and j == 0:
        if tab[i][j + 1] == valor:
            cont = cont + 1
        if tab[i - 1][j] == valor:
            cont = cont + 1
        if i % 2 == 0:
            if tab[i - 1][j + 1] == valor:
                cont = cont + 1
    if i == fil - 1 and j != 0 and j != col - 1:
        if tab[i - 1][j] == valor:
            cont = cont + 1
        if tab[i][j + 1] == valor:
            cont = cont + 1
        if tab[i][j - 1] == valor:
            cont = cont + 1
        if i % 2 == 0:
            if tab[i - 1][j + 1] == valor:
                cont = cont + 1
        else:
            if tab[i - 1][j - 1] == valor:
                cont = cont + 1
    return cont

# Para lanzar la aplicación...
if __name__=='__main__':
    # Instanciamos la interfaz
    app=prueba()
    # Lanzamos el bucle de gestión de eventos
    gtk.main()
    print ("Termina el programa")


def main():
    menu()





main()
