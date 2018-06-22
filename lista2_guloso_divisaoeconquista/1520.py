while True:
	try:
		entrada = raw_input()
		if entrada != "":
			n = int(entrada)
			p = []
			for i in xrange(n):
					ini, fim = map(int, raw_input().split())
					for j in range(ini, fim+1):
							p.append(j)
			inp = int(raw_input())
			p.sort()
			index = []
			for j in xrange(len(p)):
				if inp == p[j]:
					index.append(j)
			
			if inp not in p:
				print "%d not found" % inp
			else:
				print "%d found from %d to %d" % (inp, index[0], index[-1])
	except EOFError:
		break
		
