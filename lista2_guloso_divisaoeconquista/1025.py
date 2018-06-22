def buscaBinaria(lista, valor, ini, fim):
	if ini > fim:
		return -1
	meio = (ini+fim)/2
	if lista[meio] == valor:
		return meio
	elif lista[meio] < valor:
		return buscaBinaria(lista, valor, meio+1, fim)
	else:
		return buscaBinaria(lista, valor, ini, meio-1) 

case = 1
while True:	
	inp = map(int, raw_input().split())
	if inp[1] == 0 and inp[0] == 0: break	
	marmores = []

	for i in xrange(inp[0]):
		entrada = int(raw_input())
		marmores.append(entrada)
	
	chutes = []
	for i in xrange(inp[1]):
		marmoreChute = int(raw_input())
		chutes.append(marmoreChute)

	marmores.sort()
	print "CASE# %d:" % (case)
	for i in xrange(len(chutes)):

		resultado = buscaBinaria(marmores, chutes[i], 0, len(marmores)-1)
		if resultado != -1:
			for j in xrange(resultado,-1,-1):
				if marmores[resultado] == chutes[i]:
					resultado -= 1
				if marmores[resultado] < chutes[i]:
					break
			print "%d found at %d" % (chutes[i], resultado+2)
		else:
			print "%d not found" % chutes[i]	
	case += 1 
