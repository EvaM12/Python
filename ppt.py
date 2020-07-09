import random
print("Hola, ¿cómo te llamas?")
name=input("Me llamo: ")
print("Encandad@",name,", vamos a jugar a piedra, papel y tijera \n"
                       "el mejor de tres gana. Suerte!!")

lista=["Piedra","Papel", "Tijera"]
ganar=0
perder=0
vidas=3
while vidas>0:
    tiro = random.randrange(1,3)
    print("Que eliges: \n 1)Piedra \n 2)Papel \n 3)Tijera")
    elec=int(input("Elijo:"))
    if elec<=3:
        vidas -= 1
        if tiro==elec:
            print("Acertaste!!")
            ganar+=1
        else:
            print("Fallaste!!")
            perder+=1
    else:
        print("Esa opcion no es valida")

if ganar>perder:
    print("Ganaste el juego!!")
else:
    print("Perdiste el juego!")