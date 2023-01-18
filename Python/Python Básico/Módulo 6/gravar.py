arquivo = open("arqText.txt", 'w')

arquivo.write('Curso Python \n')
arquivo.write('Aula prática')
arquivo.close()

#leitura do arquivo texto

leitura= open('arqText.txt')
print(leitura.read())
leitura.close



