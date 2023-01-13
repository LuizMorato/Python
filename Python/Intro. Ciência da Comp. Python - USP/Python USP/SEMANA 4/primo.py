n = int(input("Digite um número inteiro: "))

cont = 2
ehNroPrimo = True

while (cont < n and ehNroPrimo):

    ehNroPrimo = not ((n % cont) == 0)
    cont += 1


if (ehNroPrimo):
    print("primo")
else:
    print("não primo")