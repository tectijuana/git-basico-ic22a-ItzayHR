import random
Numero = 0
Resultado = 0
Factoriales = []
Contador = 0

def factorial(n):
    if n == 0 or n == 1:
        Resultado = 1
    elif n > 1:
        Resultado = n * factorial(n - 1)
    return Resultado

Numero = int(input("Escribe tu numero: "))
while Contador <= Numero:
    print(f"!{Contador}: ", factorial(Contador))
    Contador += 1
