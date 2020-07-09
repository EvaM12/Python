import random

print("Adivina el numero entre 1 y 25 con 3 intentos")
num=random.randrange(1,25)
vidas=3
while vidas>0:
    intro=int(input("Estoy pensando en el numero: "))
    if intro==num:
        print("¡Has acertado!!!")
        break
    else:
        print("Has fallado! \n")
        vidas-=1
        print("Has perdido una vida, te quedan", vidas)
