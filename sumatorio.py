#Creacion de un sumatorio
x=int(input("Introduce el numero de inicio: "))
fin=int(input("Introduce el numero de fin: "))
suma=0

for i in range(x,fin+1):
    suma=suma+i
print("El resultado es:",suma)