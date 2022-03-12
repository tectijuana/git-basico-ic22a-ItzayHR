import random
import re
Numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,0,00]
CasosFavorables = 16
CasosPosibles = 52
Probabilidad = 0
Ruleta = []
CasosExitos = 0
Completado = 0

print("")
print("")

for i in range(100):
    Ruleta.append(random.choice(Numeros))
    if Ruleta[0]%2 != 0:
        CasosExitos += 1
        print(Ruleta[0])
    Ruleta.clear()



print(F"La probabilidad es {CasosExitos/100}")


