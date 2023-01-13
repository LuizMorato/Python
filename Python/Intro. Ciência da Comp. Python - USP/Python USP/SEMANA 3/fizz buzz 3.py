numero = float(input("Digite o número: "))
restodocinco = numero % 5
resto = numero % 3

if (restodocinco == 0 and resto == 0):
    print("FizzBuzz")

else:
    print(numero)