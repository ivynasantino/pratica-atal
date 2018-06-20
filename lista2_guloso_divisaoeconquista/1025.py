inp = map(int, raw_input().split())

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


for case in range(inp[1]):	
	if inp[1] == 0: break	
	marmores = []

	for i in range(inp[0]):
		entrada = int(raw_input())
		marmores.append(entrada)
	
	marmore = int(raw_input())

	marmores.sort()

	print "CASE# %d" % (case+1)

	resultado = buscaBinaria(marmores, marmore, 0, len(marmores)-1)
	if resultado == -1:
		print "%d not found" % marmore
	else:
		print "%d found at %d" % (marmore, resultado+1)		
