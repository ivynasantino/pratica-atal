entrada = int(raw_input())

def caminha(matriz, l, c):
	if matriz[l][c] == 0:
		matriz[l][c] = "visitado"
	


# forma matriz a partir da entrada
def geraMatriz(cont, entrada):
	while cont < entrada:
		matriz = []
		for m in range(5):
			linha = raw_input().split()
			matriz.append(linha)
		cont += 1
		
		# chamar aqui o caminha
		# caminha(matriz, 0, 0)
		print
		
	return matriz
	
print geraMatriz(0, entrada)
