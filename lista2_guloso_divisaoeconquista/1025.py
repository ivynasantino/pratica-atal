def buscaBinaria(lista, valor, ini, fim):
	if valor not in lista:
		return -1
	meio = (ini+fim)/2
	if lista[meio] == valor:
		return meio
	elif lista[meio] < valor:
		return buscaBinaria(lista, valor, meio+1, fim)
	else:
		return buscaBinaria(lista, valor, ini, meio) 


def primeiroMarmore(result, lista):
	primeiroIndice = result-1
	for i in range(len(lista)-1,-1,-1):
		if lista[result] == lista:
			primeiroIndice -= 1
			
	return primeiroIndice


case = 1

while True:	
	inp = map(int, raw_input().split())
	if inp[1] == 0 and inp[0] == 0: break	
	marmores = []

	for i in range(inp[0]):
		entrada = int(raw_input())
		marmores.append(entrada)
	
	marmoreChute = int(raw_input())

	marmores.sort()

	resultado = buscaBinaria(marmores, marmoreChute, 0, len(marmores)-1)
	if resultado == -1:
		print "CASE# %d" % (case)
		print "%d not found" % marmoreChute
		marmoreChute = int(raw_input())
		resultado = buscaBinaria(marmores, marmoreChute, 0, len(marmores)-1)
		chance = inp[1]-1
		while chance != 0:
			if marmoreChute == marmores[resultado]:
				print "%d found at %d" % (marmoreChute, resultado+1)
			chance -= 1
		
	else:
		print "CASE# %d" % (case)
		result = primeiroMarmore(resultado, marmores)
		print "%d found at %d" % (marmoreChute, result+2)	
	
	case += 1	

