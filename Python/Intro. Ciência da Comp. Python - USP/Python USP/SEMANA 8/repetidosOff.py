def remove_repetidos(lista):
	listaOrdenada = []
	listaDeNumerosUnicos = []

	# gera uma lista de números únicos
	for numeroCorrente in lista:
		# se a listaDeNumerosUnicos não possuir o número corrente, adiciona-o
		if numeroCorrente not in listaDeNumerosUnicos:
			listaDeNumerosUnicos.append(numeroCorrente)

	# ordenando os números únicos
	while len(listaDeNumerosUnicos) > 0:
		# reconhe o menor número e adiciona-o na lista ordenada
		numeroMinimo = min(listaDeNumerosUnicos)
		listaOrdenada.append(numeroMinimo)

		# remove o número adicionado
		index = listaDeNumerosUnicos.index(numeroMinimo)
		del listaDeNumerosUnicos[index]

	return listaOrdenada