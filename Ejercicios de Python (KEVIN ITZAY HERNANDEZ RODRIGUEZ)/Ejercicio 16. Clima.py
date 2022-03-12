import random
Numeros = []
Lluvia = 0
Soleado = 0
Nieve = 0


for i in range(100):
    Numeros.append(int(random.uniform(1, 100)))

for i in range(100):
    if Numeros[i] == 1:
        Lluvia += 1
    elif Numeros[i] == 2:
        Soleado += 1
    else:
        Nieve += 1

print(f"Llovio {Lluvia} dias con una probabilidad de {Lluvia / 100}: ")
print(f"Hubo sol {Soleado} dias con una probabilidad de {Soleado / 100}: ")
print(f"Nevo {Nieve} dias con una probabilidad de {Nieve / 100}: ")

