import random
Contador = 1
Numero = 0
Exito = 0

def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

while Contador <= 1000:
    Numero = int(random.uniform(2, 101))
    if es_primo(Numero):
        Exito += 1
    Contador += 1

print(f"La probabilidad de que salga un primo es {Exito/1000}. ")
        
        
