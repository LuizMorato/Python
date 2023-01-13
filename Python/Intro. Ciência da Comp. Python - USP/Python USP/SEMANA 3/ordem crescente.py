lista_num = [ ]

for x in range(0,3):

   user = int(input(f'Insira um número {x+1}/3: '))

   lista_num.append(user)

if lista_num[2] > lista_num[1]  and lista_num[1] > lista_num[0]:

   print('Crescente')

else:

   print('Não está em ordem crescente')