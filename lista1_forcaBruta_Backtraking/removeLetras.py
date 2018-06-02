def remove(inicio, resto):
	temp = []
	
	lista.append(inicio)
	
	for i in range (len(resto)):
		if(resto[i] not in temp):
			atual = inicio + resto[i]
			temp.append(resto[i])
			remove(atual, resto[i+1:])

while True:
	try:
		lista = []
		entrada = raw_input()
		remove(entrada[0], entrada[1:])
		
		for i in range(len(lista)):	
			if(len(lista[i]) > 1):
				lista.append(lista[i][1:])
				
		aux = list(set(lista))
		lista = aux
		
		lista.sort()
		
		for i in lista:
			print i
		print 
	except EOFError:
		break
