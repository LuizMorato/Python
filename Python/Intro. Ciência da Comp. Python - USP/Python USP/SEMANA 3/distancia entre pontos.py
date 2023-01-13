import math

# Retorna o valor númerico fornecido pelo usuário
def PegarEntrada(planoCartesiano, coordenada):
    return float(input("Forneça a coordenada {} para o Plano Cartesiano {}: ".format(coordenada, planoCartesiano)))

planoCartesianoA = PegarEntrada("A", "X"), PegarEntrada("A", "Y")
planoCartesianoB = PegarEntrada("B", "X"), PegarEntrada("B", "Y")

preCalculo = (planoCartesianoA[0]-planoCartesianoB[0])**2 + (planoCartesianoA[1]-planoCartesianoB[1])**2
distancia = math.sqrt(preCalculo)

print("longe" if distancia >= 10 else "perto")