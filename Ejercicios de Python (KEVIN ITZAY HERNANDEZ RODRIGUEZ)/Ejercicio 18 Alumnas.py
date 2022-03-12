import random
import re
AlumnosTotal = 31
Mujeres = 18
Hombres = 13
Numero = 0
Fila = []
Exitos = 0
Temp = ""
SalioMujer = 0

for i in range(31):
    Numero = int(random.uniform(1, 3))
    if Numero == 1:
        if Mujeres != 0:
            Fila.append("Mujer")
            Mujeres -= 1
        else:
            Fila.append("Hombre")
            Hombres -= 1
    else:
        if Hombres != 0:
            Fila.append("Hombre")
            Hombres -= 1
        else:
            Fila.append("Mujer")
            Mujeres -= 1

for i in range(100):
    Exitos = 0
    for j in range(5):
        Temp = random.choice(Fila)

        if Temp == "Mujer":
            Exitos += 1

    if Exitos == 5:
        SalioMujer += 1
print(F"La probabilidad de que salgan 5 mujeres es {SalioMujer/100}")





