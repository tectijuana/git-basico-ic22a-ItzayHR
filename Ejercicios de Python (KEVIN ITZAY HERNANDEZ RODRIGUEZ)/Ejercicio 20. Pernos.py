import random
import re
Compra = 100
Defectuoso = 1
Resultado = 0

Resultado = float(((1/1000)*(Defectuoso/Compra))*100)

print(f"La probabilidad de que salga uno defectuoso en la compra de {Compra} pernos es {Resultado}")

