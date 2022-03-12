import random
Dados = 5
Tiradas = 0
Loop = True
Numeros = []

input("Presione ENTER para EMPEZAR a tirar los dados")

while Loop == True:
    if Dados > 0:
        Tiradas += 1
        for i in range(Dados):
            Numeros.append(random.randint(1,6))
            print(Numeros[i])
        for i in range(Dados):
            if Numeros[i] == 4:
                Dados -= 1
            if Dados == 0:
                break
        Numeros.clear()
        input("Presione ENTER para seguir tirando los dados")
    else:
        Loop = False
        print("")
        print("")
        print("")
        print("SE ACABARON LOS DADOS")
        input("Presione ENTER para mostrar los resulados")

print("")
print("")
print("")
print("")
print("")
print(f"Fueron necesarios {Tiradas} tiradas de dados para descartar todos los dados.")
input("Presione ENTER para salir")
exit()

        
