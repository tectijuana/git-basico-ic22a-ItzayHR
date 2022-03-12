import random
Dia = 0
Exito = 0

for i in range(1000):
    Dia = random.randint(1, 8)
    if Dia == 5:
        Exito += 1

        
print("")
print("")
print("")
print("")
print("")
print(f"La probabilidad de que un año no bisiesto tenga 53 viernes es {Exito/1000}")
input("Presione ENTER para salir")
exit()

        
