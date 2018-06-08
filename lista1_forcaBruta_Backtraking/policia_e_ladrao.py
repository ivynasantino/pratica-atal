n = int(raw_input())
cont = 0

def caminha(m, l, c):
	if m[l][c] == 1:
		return
	
	m[l][c] = -1
	
	if l == 4 and c == 4:
		return
	
	if c + 1 < 5 and (m[l][c+1]) == 0:
		caminha(m, l, c+1)
	if c - 1 >= 0 and (m[l][c-1]) == 0:
		caminha(m, l, c-1)
	
	if l + 1 < 5 and (m[l+1][c]) == 0:
		caminha(m, l+1, c)
	if l - 1 >= 0 and (m[l-1][c]) == 0:
		caminha(m, l-1, c)
	
while cont < n: 
	tabuleiro = []
	entrada = map(int,raw_input().split())
	
	if (len(entrada)==0):
		c = 5
	else:
		c = 4
		tabuleiro.append(entrada)
	
	for i in range(c):
		aux = map(int,raw_input().split())
		tabuleiro.append(aux)
		
	caminha(tabuleiro,0,0)
	
	if(tabuleiro[4][4] == -1):
		print "COPS"
	else:
		print "ROBBERS"
	cont += 1
