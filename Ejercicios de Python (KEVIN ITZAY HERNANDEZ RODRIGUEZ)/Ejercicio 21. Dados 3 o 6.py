import random
Loop = True
Dado = [1, 2, 3, 4, 5, 6]
Probabilidad = 0
Numeros = []
Exitos = 0
Completado = 0

input("Presione ENTER para EMPEZAR a tirar los dados")

for i in range(1000):
    Exitos = 0
    Numeros.append(random.choice(Dado))
    if 3 == Numeros[0]:
        Exitos += 1

    Numeros.append(random.choice(Dado))
    if 6 == Numeros[1]:
        Exitos += 1
    if Exitos == 2:
        Completado += 1
        print(Numeros[0])
        print(Numeros[1])
        print("")
    Numeros.clear()


        
print("")
print("")
print("")
print("")
print("")
print(f"La probabilidad de que salga el 3 antes que el 6 es {Completado/1000}")
input("Presione ENTER para salir")
exit()

        
