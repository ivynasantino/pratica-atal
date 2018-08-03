def mochilaPD(p, v, n, N):
	p.insert(0,0)
	v.insert(0,0)
	
	m = []
	
	for i in xrange(0, n+1):
		m.append([0]*(N+1))
	
	for i in xrange(1, n+1):
		for j in xrange(1, N+1):
			if j - p[i] < 0:
				m[i][j] = m[i-1][j]
			else:
				m[i][j] = max(m[i-1][j], v[i] + m[i-1][j-p[i]])
				
	
	coube = m[n][N]
	itens = []
	i = n
	j = N
	aux = m[i][j]
	
	while aux != 0:
		if m[i][j] != m[i-1][j]:
			itens.append(i)
			j = j - p[i]
		
		i = i - 1
		aux = m[i][j]
		
	peso = 0
	for a in itens:
		peso += p[a]
		
	return (coube, peso, n - len(itens))
	
capacidadeMochila = 50
entrada = int(raw_input())

for i in xrange(entrada):
	p = []
	v = []
	
	pac = int(raw_input())
	for i in xrange(pac):
		num, peso = map(int, raw_input().split())
		p.append(peso)
		v.append(num)
	
	saida = mochilaPD(p, v, pac, capacidadeMochila)
	
	print "%d brinquedos" % saida[0]
	print "Peso: %d kg" % saida[1]
	print "sobra(m) %d pacote(s)" % saida[2]
	print
	
	
