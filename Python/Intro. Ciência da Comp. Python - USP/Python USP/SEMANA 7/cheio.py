def PegarEntrada():
    return int(input("Forneça o um número inteiro: "))

# Desenha um retangulo de #, baseado na dimensões recebidas
def RetanguloCheio(dimensoes):
    largura, altura = dimensoes
    preencherVertical = 1

    while preencherVertical <= altura:
        preencherHorizontal = 1

        while preencherHorizontal <= largura:
            print("#", end="")
            preencherHorizontal += 1

        print("")
        preencherVertical += 1

# Função de entrada do programa
def Main():
    dimensoes = (PegarEntrada(), PegarEntrada())
    RetanguloCheio(dimensoes)

Main()