entrada = int(raw_input())
cont = 0

def caminha(m, l, c):
	if m[l][c] == 1:
		return
	
	m[l][c] = -1
	
	if l == 4 and c == 4:
		return
	
	if c + 1 < 5 and (m[l][c+1]) == '0':
		caminha(m, l, c+1)
	if c - 1 >= 0 and (m[l][c-1]) == '0':
		caminha(m, l, c-1)
	
	if l + 1 < 5 and (m[l+1][c]) == '0':
		caminha(m, l+1, c)
	if l - 1 >= 0 and (m[l-1][c]) == '0':
		caminha(m, l-1, c)
	
def geraMatriz():
	matriz = []
	for m in range(5):
		linha = raw_input().split()
		matriz.append(linha)

	return matriz
	
	
while cont < entrada:	
	tabuleiro = geraMatriz()
	
	caminha(tabuleiro, 0, 0)
	
	if tabuleiro[4][4] == -1:
		print "COPS"
	else:
		print "ROBBERS"

	cont += 1
	print
