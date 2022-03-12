import random
import re
#Diamantes = ['as♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'jota♦', 'reina♦', 'rey♦']
#Corazones = ['as♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'jota♥', 'reina♥', 'rey♥']
#Treboles = ['as♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'jota♣', 'reina♣', 'rey♣']
#Picas = ['as♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'jota♠', 'reina♠', 'rey♠']
Cartas = ['AS♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'jota♦', 'reina♦', 'rey♦', 'AS♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'jota♥', 'reina♥', 'rey♥', 'AS♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'jota♣', 'reina♣', 'rey♣', 'AS♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'jota♠', 'reina♠', 'rey♠']
Probabilidad = 0
Mano = []
CasosExitos = 0
Completado = 0

print("")
print("La probabildiad de que la primera carta sea un AS es del 7.693%")
print("La probabildiad de que la siguiente sea una CARA es del 23.529%")
print("")

for i in range(1000):
    CasosExitos = 0
    Mano.append(random.choice(Cartas))
    if re.match("AS",Mano[0]):
        CasosExitos += 1
    
    #Cartas.remove(Mano[0])
    
    Mano.append(random.choice(Cartas))
    if re.match("rey",Mano[1]):
        CasosExitos += 1
    elif re.match("reina",Mano[1]):
        CasosExitos += 1
    elif re.match("jota",Mano[1]):
        CasosExitos += 1
    if CasosExitos == 2:
        Completado += 1
        print(Mano[0])
        print(Mano[1])
    Mano.clear()



print(F"La probabilidad es {Completado/1000}")


