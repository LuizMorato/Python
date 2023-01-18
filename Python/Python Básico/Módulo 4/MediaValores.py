qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while (valor > 0.00):
       soma = soma + valor
       qtd = qtd + 1
       # Entrada de valores
       valor = float(input("Digite um valor: "))

# Caso digite um valor negativo o laço encerra
media = soma / qtd
print("\n Total da Soma: ",soma)
print("\n Quantidade de valores digitados: ",qtd)
print("\n Média dos valores: ",media)
